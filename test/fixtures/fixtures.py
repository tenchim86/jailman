import pytest

from pailman.config import parse_config, read_config
from pailman.defaults import CONFIG_VERSION  # noqa: F401


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
def empty_config_file():
    return "test/fixtures/empty_config.yml"


@pytest.fixture
def current_config():
    return read_config("test/fixtures/current_config.yml")


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


@pytest.fixture()
def valid_dhcp_config():
    return parse_config(
        """
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
    dhcp: on
    beta: false
""".format(
            CONFIG_VERSION
        )
    )


@pytest.fixture()
def valid_dhcp_optional_config():
    return parse_config(
        """
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
""".format(
            CONFIG_VERSION
        )
    )


@pytest.fixture()
def invalid_dhcp_ip_gw_config():
    return parse_config(
        """
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
    dhcp: on
    beta: false
""".format(
            CONFIG_VERSION
        )
    )


@pytest.fixture()
def invalid_dhcp_gw_config():
    return parse_config(
        """
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
    gateway: 192.168.1.1
    dhcp: on
    beta: false
""".format(
            CONFIG_VERSION
        )
    )


@pytest.fixture()
def invalid_dhcp_ip_config():
    return parse_config(
        """
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
    dhcp: on
    beta: false
""".format(
            CONFIG_VERSION
        )
    )


@pytest.fixture
def valid_yaml_config(valid_config):
    return parse_config(valid_config)


@pytest.fixture()
def invalid_jails_config():
    return parse_config(
        """
global:
  version: {}
  dataset:
    config: tank/apps
    media: tank/media
  jails:
    version: 11.3-RELEASE
    pkgs: curl ca_root_nss bash
jails:
  foo:
    blueprint: bar
jails:
  plexjail:
    blueprint: plex
    dhcp: on
    beta: false
""".format(
            CONFIG_VERSION
        )
    )


@pytest.fixture()
def invalid_jail_members_config():
    return parse_config(
        """
global:
  version: {}
  dataset:
    config: tank/apps
    media: tank/media
  jails:
    version: 11.3-RELEASE
    pkgs: curl ca_root_nss bash
  foo:
    blueprint: bar
jails:
""".format(
            CONFIG_VERSION
        )
    )


@pytest.fixture()
def invalid_blueprint_config():
    return parse_config(
        """
blueprint:
  foo:
    pkgs: foo bar baz
jails:
"""
    )


@pytest.fixture()
def blueprint_duplicate_pkg_config():
    return parse_config(
        """
blueprint:
  foo:
    pkgs: foo bar foo
jails:
"""
    )


@pytest.fixture()
def blueprint_no_blueprint_config():
    return parse_config(
        """
blueprint:
"""
    )


@pytest.fixture()
def blueprint_no_pkg_config():
    return parse_config(
        """
blueprint:
  foo:
    pkgs: foo bar baz
jails:
"""
    )


@pytest.fixture()
def blueprint_add_vars_config():
    return parse_config(
        """
blueprint:
  foo:
    pkgs: foo bar baz
jails:
"""
    )


@pytest.fixture()
def valid_blueprint():
    return parse_config(
        """
blueprint:
  foo:
    pkgs: foo bar baz
"""
    )
