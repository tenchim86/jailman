DEFAULT_CONFIG_FILE = "config.yml"
CONFIG_SCHEMA = "pailman/config.schema.json"
CONFIG_VERSION = "v1.4"


class CONFIG_KEYS:
    GLOBAL = "global"
    JAIL = "jail"


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
