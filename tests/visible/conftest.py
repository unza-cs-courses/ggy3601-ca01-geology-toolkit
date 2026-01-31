"""
Pytest configuration for Coding Assignment 1 visible tests.
Loads variant configuration if available.
"""

import json
import pytest
from pathlib import Path


@pytest.fixture(scope="session")
def variant_config():
    """Load student's variant configuration."""
    config_path = Path(__file__).parent.parent.parent / ".variant_config.json"
    if config_path.exists():
        with open(config_path) as f:
            return json.load(f)
    # Default values for testing without variant config
    return {
        "parameters": {
            "commodity": "gold",
            "hardness_options": ["soft", "medium", "hard"],
            "base_drilling_rate": 75,
            "depth_bonus_threshold": 500,
            "num_test_samples": 50
        }
    }


@pytest.fixture
def commodity(variant_config):
    """Return expected commodity."""
    return variant_config["parameters"]["commodity"]


@pytest.fixture
def hardness_options(variant_config):
    """Return available hardness options."""
    return variant_config["parameters"]["hardness_options"]


@pytest.fixture
def base_drilling_rate(variant_config):
    """Return base drilling rate."""
    return variant_config["parameters"]["base_drilling_rate"]


@pytest.fixture
def depth_bonus_threshold(variant_config):
    """Return depth bonus threshold."""
    return variant_config["parameters"]["depth_bonus_threshold"]


@pytest.fixture
def num_test_samples(variant_config):
    """Return number of test samples."""
    return variant_config["parameters"]["num_test_samples"]


@pytest.fixture
def sample_data_path():
    """Return path to sample data file."""
    return Path(__file__).parent.parent.parent / "data" / "sample_data.csv"


@pytest.fixture
def temp_output_path(tmp_path):
    """Return path for temporary output file."""
    return tmp_path / "test_output.csv"
