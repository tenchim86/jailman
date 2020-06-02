import argparse

import pytest

import pailman.cli as cli


def test_cli_fails_on_invalid_arg() -> None:
    parser = argparse.ArgumentParser(prog="pailman")
    cli.define_cli(parser)
    with pytest.raises(SystemExit) as e:
        parser.parse_args(["-y"])
    assert e.type == SystemExit


def test_cli_accepts_install() -> None:
    parser = argparse.ArgumentParser(prog="pailman")
    cli.define_cli(parser)
    opts = parser.parse_args(["-i", "foo"])
    i = cli.to_install(opts)
    assert len(i) == 1
    assert i[0] == "foo"


def test_cli_accepts_detroy() -> None:
    parser = argparse.ArgumentParser(prog="pailman")
    cli.define_cli(parser)
    opts = parser.parse_args(["-d", "foo"])
    d = cli.to_destroy(opts)
    assert len(d) == 1
    assert d[0] == "foo"


def test_cli_accepts_install_and_destroy() -> None:
    parser = argparse.ArgumentParser(prog="pailman")
    cli.define_cli(parser)
    opts = parser.parse_args(["-i", "foo", "-d", "bar"])
    i = cli.to_install(opts)
    assert len(i) == 1
    assert i[0] == "foo"
    d = cli.to_destroy(opts)
    assert len(d) == 1
    assert d[0] == "bar"


def test_cli_collects_multiple_use_of_install() -> None:
    parser = argparse.ArgumentParser(prog="pailman")
    cli.define_cli(parser)
    opts = parser.parse_args(["-i", "foo", "-i", "bar"])
    i = cli.to_install(opts)
    assert len(i) == 2
    assert set(i) == set(["foo", "bar"])
