import json
from pathlib import Path

import yaml
from jsonschema import validate
from yaml.resolver import Resolver

from pailman.defaults import (  # noqa: F401
    BLUEPRINT_SCHEMA,
    BLUEPRINTS_GLOB,
    CONFIG_SCHEMA,
    CONFIG_VERSION,
    DEFAULT_BLUEPRINTS_DIR,
)


# https://stackoverflow.com/questions/36463531/pyyaml-automatically-converting-certain-keys-to-boolean-values
def _configure_yaml_parser():
    # remove resolver entries for On/Off/Yes/No
    for ch in "OoYyNn":
        if len(Resolver.yaml_implicit_resolvers[ch]) == 1:
            del Resolver.yaml_implicit_resolvers[ch]
        else:
            Resolver.yaml_implicit_resolvers[ch] = [
                x
                for x in Resolver.yaml_implicit_resolvers[ch]
                if x[0] != "tag:yaml.org,2002:bool"
            ]


_configure_yaml_parser()


def parse_config(cfg):
    contents = yaml.safe_load(cfg)
    return contents


def read_config(filename):
    with open(filename) as file:
        contents = yaml.safe_load(file)
        return contents


def find_blueprint_config_files(dir=DEFAULT_BLUEPRINTS_DIR, glob=BLUEPRINTS_GLOB):
    return Path(dir).glob(glob)


def read_blueprints(dir=DEFAULT_BLUEPRINTS_DIR, glob=BLUEPRINTS_GLOB):
    configs = {p: read_config(p) for p in find_blueprint_config_files(dir, glob)}
    return configs


def read_schema(filename):
    with open(filename) as file:
        contents = json.load(file)
        return contents


def validate_config(cfg, schema=read_schema(CONFIG_SCHEMA)):
    return validate(schema=schema, instance=json.loads(json.dumps(cfg)))


def validate_blueprint(blueprint):
    return validate(
        schema=read_schema(BLUEPRINT_SCHEMA), instance=json.loads(json.dumps(blueprint))
    )
