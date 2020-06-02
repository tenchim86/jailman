import argparse

from pailman.defaults import DEFAULT_CONFIG


# this is included from Python 3.8+
class ExtendAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        items = getattr(namespace, self.dest) or []
        items.extend(values)
        setattr(namespace, self.dest, items)


def define_cli(parser):
    parser.register("action", "extend", ExtendAction)
    parser.add_argument(
        "-c",
        "--config",
        action="store",
        dest="config",
        default=DEFAULT_CONFIG,
        metavar="CONFIG",
        help="Use configuration in CONFIG. Defaults to `{}` in current directory".format(
            DEFAULT_CONFIG
        ),
    )
    parser.add_argument(
        "-i",
        "--install",
        nargs="+",
        action="extend",
        dest="to_install",
        metavar="BLUEPRINT",
        help="Install a blueprint",
    )
    parser.add_argument(
        "-d",
        "--destroy",
        nargs="+",
        action="extend",
        dest="to_destroy",
        metavar="BLUEPRINT",
        help="Destroy a blueprint",
    )


def to_install(opts):
    return opts.to_install


def to_destroy(opts):
    return opts.to_destroy


def config(opts):
    return opts.config
