from typing import List, Dict, Any

def calculate_player_stats(data: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Calculate key statistics from a list of gaming sessions."""
    if not data:
        return {"total_sessions": 0, "average_score": 0.0, "highest_score": 0, "top_player": None}

    total_sessions = len(data)
    scores = [session.get("score", 0) for session in data]
    average_score = sum(scores) / total_sessions if total_sessions > 0 else 0
    highest_score = max(scores) if scores else 0

    top_session = max(data, key=lambda x: x.get("score", 0))
    top_player = top_session.get("player", "Unknown")

    return {
        "total_sessions": total_sessions,
        "average_score": round(average_score, 2),
        "highest_score": highest_score,
        "top_player": top_player
    }

def filter_sessions_by_level(data: List[Dict[str, Any]], min_level: int) -> List[Dict[str, Any]]:
    """Filter sessions to those at or above the given level."""
    return [session for session in data if session.get("level", 0) >= min_level]

def aggregate_gaming_data(data: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Process raw gaming data into useful aggregates."""
    stats = calculate_player_stats(data)
    high_level_sessions = filter_sessions_by_level(data, 5)
    stats["high_level_count"] = len(high_level_sessions)
    if high_level_sessions:
        avg = sum(s.get("score", 0) for s in high_level_sessions) / len(high_level_sessions)
        stats["high_level_avg_score"] = round(avg, 2)
    else:
        stats["high_level_avg_score"] = 0
    return stats

if __name__ == "__main__":
    sample_data = [
        {"player": "Alice", "score": 1500, "level": 5},
        {"player": "Bob", "score": 1200, "level": 3},
        {"player": "Charlie", "score": 1800, "level": 7},
        {"player": "Diana", "score": 950, "level": 4},
        {"player": "Alice", "score": 1650, "level": 6}
    ]
    processed = aggregate_gaming_data(sample_data)
    print(processed)