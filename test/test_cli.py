import argparse

import pytest

import pailman.cli as cli


@pytest.fixture
def parser():
    argp = argparse.ArgumentParser(prog="pailman")
    cli.define_cli(argp)
    return argp


def test_cli_fails_on_invalid_arg(parser) -> None:
    with pytest.raises(SystemExit) as e:
        parser.parse_args(["-y"])
    assert e.type == SystemExit


def test_cli_accepts_install(parser) -> None:
    opts = parser.parse_args(["-i", "foo"])
    i = cli.to_install(opts)
    assert len(i) == 1
    assert i[0] == "foo"


def test_cli_accepts_reinstall(parser) -> None:
    opts = parser.parse_args(["-r", "foo"])
    r = cli.to_reinstall(opts)
    assert len(r) == 1
    assert r[0] == "foo"


def test_cli_accepts_update(parser) -> None:
    opts = parser.parse_args(["-u", "foo"])
    u = cli.to_update(opts)
    assert len(u) == 1
    assert u[0] == "foo"


def test_cli_accepts_detroy(parser) -> None:
    opts = parser.parse_args(["-d", "foo"])
    d = cli.to_destroy(opts)
    assert len(d) == 1
    assert d[0] == "foo"


def test_cli_accepts_install_and_destroy(parser) -> None:
    opts = parser.parse_args(["-i", "foo", "-d", "bar"])
    i = cli.to_install(opts)
    assert len(i) == 1
    assert i[0] == "foo"
    d = cli.to_destroy(opts)
    assert len(d) == 1
    assert d[0] == "bar"


def test_cli_collects_multiple_use_of_install(parser) -> None:
    opts = parser.parse_args(["-i", "foo", "-i", "bar"])
    i = cli.to_install(opts)
    assert len(i) == 2
    assert set(i) == set(["foo", "bar"])


def test_cli_accepts_config(parser) -> None:
    opts = parser.parse_args(["-c", "test/fixtures/emptyconfig.yml"])
    assert cli.config_file(opts) == "test/fixtures/emptyconfig.yml"
