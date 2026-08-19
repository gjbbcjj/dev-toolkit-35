from typing import List, Dict, Any, Optional

class GameEvent:
    def __init__(self, event_type: str, event_data: Dict[str, Any]) -> None:
        """Initialize a game event with a type and data."""
        self.event_type = event_type
        self.event_data = event_data

    def to_dict(self) -> Dict[str, Any]:
        """Convert the event to a dictionary for easy serialization."""
        return {
            'type': self.event_type,
            'data': self.event_data
        }

class EventHandler:
    def __init__(self) -> None:
        """Initialize an event handler with an empty event list."""
        self.events: List[GameEvent] = []

    def add_event(self, event: GameEvent) -> None:
        """Add a game event to the event list."""
        self.events.append(event)

    def get_events(self) -> List[Dict[str, Any]]:
        """Retrieve the list of events in dictionary format."""
        return [event.to_dict() for event in self.events]

    def clear_events(self) -> None:
        """Clear all stored events."""
        self.events.clear()

# Example usage
if __name__ == '__main__':
    handler = EventHandler()
    handler.add_event(GameEvent('start', {'level': 1}))
    print(handler.get_events())
    handler.clear_events()  
    print(handler.get_events())