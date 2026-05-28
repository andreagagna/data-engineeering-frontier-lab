from datetime import UTC
from pathlib import Path

from energy_flex_pipeline.config import Settings


def test_settings_defaults_are_local_and_deterministic() -> None:
    settings = Settings()

    assert settings.raw_data_dir == Path("data/raw")
    assert settings.processed_data_dir == Path("data/processed")
    assert settings.default_seed == 42
    assert settings.default_asset_count == 3
    assert settings.default_start_time.tzinfo == UTC
    assert settings.log_level == "INFO"


def test_settings_can_be_overridden_from_environment(monkeypatch) -> None:
    monkeypatch.setenv("ENERGY_FLEX_RAW_DATA_DIR", "/tmp/energy-flex/raw")
    monkeypatch.setenv("ENERGY_FLEX_DEFAULT_SEED", "123")
    monkeypatch.setenv("ENERGY_FLEX_LOG_LEVEL", "DEBUG")

    settings = Settings()

    assert settings.raw_data_dir == Path("/tmp/energy-flex/raw")
    assert settings.default_seed == 123
    assert settings.log_level == "DEBUG"
