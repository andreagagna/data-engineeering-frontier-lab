"""Timestamp helpers for consistent UTC handling."""

from datetime import UTC, datetime


def ensure_utc(value: datetime) -> datetime:
    """Return a timezone-aware datetime normalized to UTC."""
    if value.tzinfo is None or value.utcoffset() is None:
        msg = "datetime must be timezone-aware"
        raise ValueError(msg)

    return value.astimezone(UTC)


def parse_utc_datetime(value: str) -> datetime:
    """Parse an ISO 8601 timestamp string and normalize it to UTC."""
    normalized_value = value.strip()
    if normalized_value.endswith("Z"):
        normalized_value = f"{normalized_value[:-1]}+00:00"

    try:
        parsed = datetime.fromisoformat(normalized_value)
    except ValueError as exc:
        msg = f"invalid ISO 8601 datetime: {value!r}"
        raise ValueError(msg) from exc

    return ensure_utc(parsed)


def utc_now() -> datetime:
    """Return the current timezone-aware UTC datetime."""
    return datetime.now(UTC)
