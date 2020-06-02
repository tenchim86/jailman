import argparse

from pailman.cli import define_cli
from pailman.config import read_config
from pailman.defaults import DEFAULT_CONFIG

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="pailman")
    define_cli(parser)
    opts = parser.parse_args()

    read_config(DEFAULT_CONFIG)

    print("to install: {}".format(opts.to_install))
    print("to destroy: {}".format(opts.to_destroy))
