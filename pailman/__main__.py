import argparse
import sys

from fastjsonschema import JsonSchemaException

from pailman.cli import config_file, define_cli, to_destroy, to_install
from pailman.config import read_config, validate_config

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="pailman")
    define_cli(parser)
    opts = parser.parse_args()

    print("using config: {}".format(config_file(opts)))
    cfg = read_config(config_file(opts))

    try:
        validate_config(cfg)
    except JsonSchemaException as error:
        print("config is invalid: {}".format(error.message))
        sys.exit(1)

    print("to install: {}".format(to_install(opts)))
    print("to destroy: {}".format(to_destroy(opts)))
