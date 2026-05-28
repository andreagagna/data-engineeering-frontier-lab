"""Application settings loaded from local defaults and environment variables."""

from datetime import UTC, datetime
from pathlib import Path
from typing import Literal

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

LogLevel = Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]


class Settings(BaseSettings):
    """Runtime settings for local data generation and pipeline execution."""

    model_config = SettingsConfigDict(
        env_prefix="ENERGY_FLEX_",
        env_file=".env",
        extra="ignore",
    )

    raw_data_dir: Path = Path("data/raw")
    processed_data_dir: Path = Path("data/processed")
    default_seed: int = Field(default=42, ge=0)
    default_asset_count: int = Field(default=3, ge=1)
    default_start_time: datetime = datetime(2026, 1, 1, tzinfo=UTC)
    log_level: LogLevel = "INFO"
