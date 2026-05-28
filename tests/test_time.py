from datetime import UTC, datetime, timedelta, timezone

import pytest

from energy_flex_pipeline.domain import ensure_utc, parse_utc_datetime, utc_now


def test_ensure_utc_keeps_utc_datetime() -> None:
    timestamp = datetime(2026, 1, 1, 12, 0, tzinfo=UTC)

    result = ensure_utc(timestamp)

    assert result == timestamp
    assert result.tzinfo == UTC


def test_ensure_utc_converts_timezone_aware_datetime_to_utc() -> None:
    prague_time = timezone(timedelta(hours=1))
    timestamp = datetime(2026, 1, 1, 13, 0, tzinfo=prague_time)

    result = ensure_utc(timestamp)

    assert result == datetime(2026, 1, 1, 12, 0, tzinfo=UTC)
    assert result.tzinfo == UTC


def test_ensure_utc_rejects_naive_datetime() -> None:
    timestamp = datetime(2026, 1, 1, 12, 0)

    with pytest.raises(ValueError, match="timezone-aware"):
        ensure_utc(timestamp)


def test_parse_utc_datetime_parses_z_timestamp() -> None:
    result = parse_utc_datetime("2026-01-01T12:00:00Z")

    assert result == datetime(2026, 1, 1, 12, 0, tzinfo=UTC)
    assert result.tzinfo == UTC


def test_parse_utc_datetime_normalizes_offset_timestamp() -> None:
    result = parse_utc_datetime("2026-01-01T13:00:00+01:00")

    assert result == datetime(2026, 1, 1, 12, 0, tzinfo=UTC)
    assert result.tzinfo == UTC


def test_parse_utc_datetime_rejects_naive_timestamp() -> None:
    with pytest.raises(ValueError, match="timezone-aware"):
        parse_utc_datetime("2026-01-01T12:00:00")


def test_utc_now_returns_timezone_aware_utc_datetime() -> None:
    result = utc_now()

    assert result.tzinfo == UTC
