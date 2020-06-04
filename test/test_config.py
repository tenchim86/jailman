import pytest
from jsonschema import ValidationError

from pailman.config import (
    find_blueprint_config_files,
    parse_config,
    read_blueprints,
    read_config,
    read_schema,
    validate_blueprint,
    validate_config,
)
from pailman.defaults import (  # noqa: F401
    BLUEPRINT_KEYS,
    CONFIG_KEYS,
    CONFIG_SCHEMA,
    CONFIG_VERSION,
)


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


def test_yaml_parser_retains_on(valid_dhcp_config):
    # should not be true!
    assert valid_dhcp_config["jails"]["plexjail"]["dhcp"] == "on"


def test_validate_config_with_schema(valid_yaml_config):
    schema = read_schema(CONFIG_SCHEMA)

    validate_config(valid_yaml_config, schema)


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


@pytest.mark.xfail(
    reason="fails until json schema can enforce uniqueness of keys in a map"
)
def test_duplicate_jails_is_invalid(invalid_jails_config):
    with pytest.raises(ValidationError):
        validate_config(invalid_jails_config)


def test_jails_cannot_have_no_members(invalid_jail_members_config):
    with pytest.raises(ValidationError):
        validate_config(invalid_jail_members_config)


def test_read_blueprints():
    configs = read_blueprints()
    assert configs is not None
    assert len(configs) > 0
    for p, cfg in configs.items():
        assert BLUEPRINT_KEYS.BLUEPRINT in cfg


def test_no_blueprint_instantiated(invalid_jail_members_config):
    with pytest.raises(ValidationError):
        validate_config(invalid_jail_members_config)


def test_no_blueprint(blueprint_no_blueprint_config):
    with pytest.raises(ValidationError):
        validate_blueprint(blueprint_no_blueprint_config)


def test_invalid_blueprint(invalid_blueprint_config):
    with pytest.raises(ValidationError):
        validate_blueprint(invalid_blueprint_config)


def test_blueprint_duplicate_pkg(blueprint_duplicate_pkg_config):
    with pytest.raises(ValidationError):
        validate_blueprint(blueprint_duplicate_pkg_config)


def test_blueprint_no_blueprint(blueprint_no_blueprint_config):
    with pytest.raises(ValidationError):
        validate_blueprint(blueprint_no_blueprint_config)


def test_blueprint_no_pkg(blueprint_no_pkg_config):
    with pytest.raises(ValidationError):
        validate_blueprint(blueprint_no_pkg_config)


def test_blueprint_add_vars(blueprint_add_vars_config):
    with pytest.raises(ValidationError):
        validate_blueprint(blueprint_add_vars_config)


def test_blueprint_config_files():
    files = find_blueprint_config_files("test/fixtures")
    assert files is not None
    assert len(list(files)) == 1


def test_config_is_not_valid_blueprint(valid_config):
    with pytest.raises(ValidationError):
        validate_blueprint(valid_config)


def test_blueprint_is_not_valid_config(valid_blueprint):
    with pytest.raises(ValidationError):
        validate_config(valid_blueprint)
