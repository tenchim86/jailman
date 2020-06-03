import pytest
from fastjsonschema import JsonSchemaException

from pailman.config import (
    parse_config,
    read_config,
    read_schema,
    validate_config,
    validate_config_with_schema,
)
from pailman.defaults import CONFIG_SCHEMA, CONFIG_VERSION  # noqa: F401


@pytest.fixture
def empty_config_file():
    return "test/fixtures/empty_config.yml"


@pytest.fixture
def current_config():
    return read_config("test/fixtures/current_config.yml")


def test_read_config(empty_config_file) -> None:
    assert read_config(empty_config_file) is None


@pytest.fixture(
    params=[
        "test/fixtures/datasetempty_config.yml",
        "test/fixtures/datasetless_config.yml",
        "test/fixtures/empty_config.yml",
        "test/fixtures/globalless_config.yml",
        "test/fixtures/globalwithoutversion_config.yml",
        "test/fixtures/outdated_config.yml",
        "test/fixtures/versionless_config.yml",
        "test/fixtures/versionempty_config.yml",
    ]
)
def invalid_config(request):
    return read_config(request.param)


@pytest.fixture
def valid_config():
    return """
global:
  version: {}
  dataset:
    config: tank/apps
    media: tank/media
  jails:
    version: 11.3-RELEASE
    pkgs: curl ca_root_nss bash
jails:
  plexjail:
    blueprint: plex
    ip4_addr: 192.168.1.99/24
    gateway: 192.168.1.1
    beta: false
""".format(
        CONFIG_VERSION
    )


@pytest.fixture
def valid_yaml_config(valid_config):
    return parse_config(valid_config)


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
    with pytest.raises(JsonSchemaException):
        validate_config(invalid_config)
