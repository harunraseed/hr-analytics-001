"""Unit tests for the environment -> catalog mapping.

This proves the core promise: dev reads hrb_dev, uat reads hrb_uat,
prod reads hrb_prod — and an unknown environment fails loudly.
"""

import pytest

from hr_analytics import config


def test_catalog_mapping():
    assert config.get_catalog("dev") == "hrb_dev"
    assert config.get_catalog("uat") == "hrb_uat"
    assert config.get_catalog("prod") == "hrb_prod"


def test_get_env_defaults_to_dev(monkeypatch):
    monkeypatch.delenv("APP_ENV", raising=False)
    assert config.get_env() == "dev"


def test_get_env_rejects_unknown(monkeypatch):
    monkeypatch.setenv("APP_ENV", "staging")
    with pytest.raises(ValueError):
        config.get_env()


def test_table_fqn_follows_environment(monkeypatch):
    monkeypatch.setenv("APP_ENV", "prod")
    monkeypatch.delenv("HR_SCHEMA", raising=False)
    monkeypatch.delenv("HR_TABLE", raising=False)
    assert config.get_table_fqn() == "hrb_prod.hr.employees"
