DEFAULT_CONFIG_FILE = "config.yml"
DEFAULT_BLUEPRINTS_DIR = "blueprints"
BLUEPRINTS_GLOB = "*/*.yml"
CONFIG_SCHEMA = "pailman/config.schema.json"
BLUEPRINT_SCHEMA = "pailman/blueprint.schema.json"
CONFIG_VERSION = "v1.4"


class CONFIG_KEYS:
    GLOBAL = "global"
    JAILS = "jails"


class GLOBAL_KEYS:
    VERSION = "version"
    DATASET = "dataset"
    JAILS = "jail"


class DATASET_KEYS:
    MEDIA = "media"
    CONFIG = "config"


class JAIL_KEYS:
    BLUEPRINT = "blueprint"
    IP4_ADDR = "ip4_addr"
    GATEWAY = "gateway"
    DHCP = "dhcp"
    LINK = "link"


class BLUEPRINT_KEYS:
    BLUEPRINT = "blueprint"
    VARS = "vars"
    REQVARS = "reqvars"
    PKGS = "pkgs"
