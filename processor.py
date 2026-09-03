import json
import logging
from typing import Dict, List, Any

logger = logging.getLogger("dev-toolkit-35")

class ProcessorError(Exception):
    """Base exception for processor errors."""
    pass

class GameEventProcessor:
    """Processes batch game events with robust error handling."""

    def __init__(self, strict_mode: bool = False):
        self.strict_mode = strict_mode

    def process_event(self, event: Dict[str, Any]) -> Dict[str, Any]:
        """Processes a single game event, validating key fields."""
        if not isinstance(event, dict):
            raise ProcessorError("Event data must be a dictionary")

        event_id = event.get("event_id")
        event_type = event.get("type")

        if not event_id or not event_type:
            raise ProcessorError("Missing required fields: event_id or type")

        try:
            if event_type == "score_update":
                score = int(event.get("score", 0))
                if score < 0:
                    raise ValueError("Score cannot be negative")
                return {"event_id": event_id, "status": "processed", "score": score}

            elif event_type == "item_purchase":
                item_id = event.get("item_id")
                cost = float(event.get("cost", 0.0))
                if not item_id or cost < 0:
                    raise ValueError("Invalid item_id or cost")
                return {"event_id": event_id, "status": "processed", "item_id": item_id}

            else:
                raise ValueError(f"Unknown event type: {event_type}")

        except (ValueError, TypeError) as e:
            if self.strict_mode:
                raise ProcessorError(f"Validation failed: {str(e)}") from e
            logger.warning(f"Skipping event {event_id}: {str(e)}")
            return {"event_id": event_id, "status": "failed", "reason": str(e)}

    def process_batch(self, events_json: str) -> List[Dict[str, Any]]:
        """Parses and processes a JSON string representing a batch of events."""
        processed_results = []
        try:
            events = json.loads(events_json)
            if not isinstance(events, list):
                raise ProcessorError("Batch data must be a list of events")
        except json.JSONDecodeError as e:
            raise ProcessorError(f"Invalid JSON format: {str(e)}") from e

        for index, event in enumerate(events):
            try:
                result = self.process_event(event)
                processed_results.append(result)
            except ProcessorError as e:
                if self.strict_mode:
                    raise
                logger.error(f"Error processing index {index}: {str(e)}")
                processed_results.append({"index": index, "status": "error", "reason": str(e)})

        return processed_results