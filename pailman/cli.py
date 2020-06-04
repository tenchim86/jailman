import argparse

from pailman.defaults import DEFAULT_CONFIG_FILE


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
        default=DEFAULT_CONFIG_FILE,
        metavar="CONFIG",
        help="Use configuration in CONFIG. Defaults to `{}` in current directory".format(
            DEFAULT_CONFIG_FILE
        ),
    )
    parser.add_argument(
        "-i",
        "--install",
        nargs="+",
        action="extend",
        dest="to_install",
        metavar="JAIL",
        help="Install a jail",
    )
    parser.add_argument(
        "-r",
        "--reinstall",
        nargs="+",
        action="extend",
        dest="to_reinstall",
        metavar="JAIL",
        help="Reinstall a jail",
    )
    parser.add_argument(
        "-u",
        "--update",
        nargs="+",
        action="extend",
        dest="to_update",
        metavar="JAIL",
        help="Update a jail",
    )
    parser.add_argument(
        "-d",
        "--destroy",
        nargs="+",
        action="extend",
        dest="to_destroy",
        metavar="JAIL",
        help="Destroy a jail",
    )


def to_install(opts):
    return opts.to_install


def to_reinstall(opts):
    return opts.to_reinstall


def to_update(opts):
    return opts.to_update


def to_destroy(opts):
    return opts.to_destroy


def config_file(opts):
    return opts.config
