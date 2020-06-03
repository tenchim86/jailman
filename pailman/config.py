import json

import yaml
from fastjsonschema import validate
from yaml.resolver import Resolver

from pailman.defaults import CONFIG_SCHEMA, CONFIG_VERSION  # noqa: F401


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


# WIP - need to find a way to map dict values to instances of BlueprintConfig
# class GlobalConfig(yaml.YAMLObject):
#     yaml_tag = '!global'
#
#     version = ""
#     dataset = {}
#
#
# class JailsConfig(yaml.YAMLObject):
#     yaml_tag = '!jails'
#     entries = {}
#
#     def __init__(self, entries):
#         self.entries = entries
#
#
# class BlueprintConfig(yaml.YAMLObject):
#     blueprint = ""
#     ip4_addr = ""
#     gateway = ""
#     dhcp = ""
#
#
# yaml.add_path_resolver('!global', ['global'], dict)
# this ignores children
# yaml.add_path_resolver('!jails', ['jails'], dict)
#
#
# def parse_config(filename):
#     with open(filename) as file:
#         contents = yaml.load(file, Loader=yaml.FullLoader)
#         return contents
#


def parse_config(cfg):
    contents = yaml.safe_load(cfg)
    return contents


def read_config(filename):
    with open(filename) as file:
        contents = yaml.safe_load(file)
        return contents


def read_schema(filename):
    with open(filename) as file:
        contents = json.load(file)
        return contents


def validate_config_with_schema(cfg, schema):
    return validate(schema, json.loads(json.dumps(cfg)))


def validate_config(cfg):
    return validate_config_with_schema(cfg, read_schema(CONFIG_SCHEMA))
