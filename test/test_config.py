import pytest
from jsonschema import ValidationError

from pailman.config import (
    parse_config,
    read_config,
    read_schema,
    validate_config,
    validate_config_with_schema,
)
from pailman.defaults import CONFIG_SCHEMA, CONFIG_VERSION  # noqa: F401


def test_read_config(empty_config_file) -> None:
    assert read_config(empty_config_file) is None


def test_current_config_is_valid(current_config) -> None:
    validate_config(current_config)


def test_valid_config(valid_yaml_config) -> None:
    validate_config(valid_yaml_config)


def test_parse_config(valid_config) -> None:
    cfg = parse_config(valid_config)
    assert cfg is not None
    assert "global" in cfg


def test_read_schema():
    schema = read_schema(CONFIG_SCHEMA)
    assert schema is not None
    assert "definitions" in schema
    assert schema["definitions"] is not None


def test_validate_config_with_schema(valid_yaml_config):
    schema = read_schema(CONFIG_SCHEMA)

    validate_config_with_schema(valid_yaml_config, schema)


def test_invalid_config(invalid_config):
    with pytest.raises(ValidationError):
        validate_config(invalid_config)


def test_dhcp_and_ip_exclusive(invalid_dhcp_ip_config):
    with pytest.raises(ValidationError):
        validate_config(invalid_dhcp_ip_config)


def test_dhcp_and_gw_exclusive(invalid_dhcp_gw_config):
    with pytest.raises(ValidationError):
        validate_config(invalid_dhcp_gw_config)


def test_dhcp_and_ip_gw_exclusive(invalid_dhcp_ip_gw_config):
    with pytest.raises(ValidationError):
        validate_config(invalid_dhcp_ip_gw_config)


def test_dhcp_is_ok(valid_dhcp_config):
    validate_config(valid_dhcp_config)


def test_dhcp_is_optional(valid_dhcp_optional_config):
    validate_config(valid_dhcp_optional_config)
