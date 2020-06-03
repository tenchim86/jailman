import yaml

from pailman.defaults import CONFIG_KEYS, CONFIG_VERSION, GLOBAL_KEYS

# class PailmanConfig:


def read_config(filename):
    with open(filename) as file:
        contents = yaml.safe_load(file)
        return contents


def validate_config(cfg):
    valid = False
    errors = []

    print(cfg)

    if cfg is None:
        errors.append("config is empty")
    elif CONFIG_KEYS.GLOBAL not in cfg:
        errors.append("missing {} in config".format(CONFIG_KEYS.GLOBAL))
    elif cfg[CONFIG_KEYS.GLOBAL] is None:
        errors.append("{} is empty in config".format(CONFIG_KEYS.GLOBAL))
    elif GLOBAL_KEYS.VERSION not in cfg[CONFIG_KEYS.GLOBAL]:
        errors.append(
            "missing {} in {}".format(GLOBAL_KEYS.VERSION, CONFIG_KEYS.GLOBAL)
        )
    elif cfg[CONFIG_KEYS.GLOBAL][GLOBAL_KEYS.VERSION] is None:
        errors.append(
            "{}.{} is empty in config".format(CONFIG_KEYS.GLOBAL, GLOBAL_KEYS.VERSION)
        )
    elif cfg[CONFIG_KEYS.GLOBAL][GLOBAL_KEYS.VERSION] != CONFIG_VERSION:
        errors.append(
            "{}.{} does not match latest: {}".format(
                GLOBAL_KEYS.VERSION, CONFIG_KEYS.GLOBAL, CONFIG_VERSION
            )
        )
    elif GLOBAL_KEYS.DATASET not in cfg[CONFIG_KEYS.GLOBAL]:
        errors.append(
            "missing {} in {}".format(GLOBAL_KEYS.DATASET, CONFIG_KEYS.GLOBAL)
        )
    elif cfg[CONFIG_KEYS.GLOBAL][GLOBAL_KEYS.DATASET] is None:
        errors.append(
            "{}.{} is empty in config".format(CONFIG_KEYS.GLOBAL, GLOBAL_KEYS.DATASET)
        )
    else:
        valid = True

    return (valid, errors)
