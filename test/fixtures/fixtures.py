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


@pytest.fixture()
def blueprint_no_root_config():
    return parse_config(
        """
foo:
    something: 3
bar:
- yikes
"""
    )


@pytest.fixture()
def blueprint_pkg_array_config():
    return parse_config(
        """
blueprint:
  foo:
    pkgs: [ foo bar baz ]
"""
    )


@pytest.fixture()
def blueprint_pkg_array_block_config():
    return parse_config(
        """
blueprint:
  foo:
    pkgs:
    - foo
    - bar
    - baz
"""
    )


@pytest.fixture()
def blueprint_vars_reqvars_config():
    return parse_config(
        """
blueprint:
  foo:
    pkgs: foo bar baz
    vars: alice bob
    reqvars: zack yves xavier
"""
    )


@pytest.fixture()
def blueprint_plex():
    return parse_config(
        """
blueprint:
  plex:
    traefik_service_port: 32400
    pkgs: plexmediaserver
    vars: beta ramdisk hw_transcode hw_transcode_ruleset ruleset_script
"""
    )


@pytest.fixture()
def blueprint_foo():
    return parse_config(
        """
blueprint:
  foo:
    traefik_service_port: 32400
    pkgs: plexmediaserver
    vars: beta ramdisk hw_transcode hw_transcode_ruleset ruleset_script
"""
    )


@pytest.fixture()
def blueprint_reqvars():
    return parse_config(
        """
blueprint:
  plex:
    traefik_service_port: 32400
    pkgs: plexmediaserver
    vars: beta ramdisk hw_transcode hw_transcode_ruleset ruleset_script
    reqvars: beta ramdisk
"""
    )


@pytest.fixture
def valid_config_reqvars():
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
    beta: false
    ramdisk: foo
""".format(
            CONFIG_VERSION
        )
    )


@pytest.fixture
def valid_config_add_vars():
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
    beta: false
    ramdisk: foo
    some: other
    variable: 42
""".format(
            CONFIG_VERSION
        )
    )
