from pailman.config import read_config


def test_read_config() -> None:
    assert (read_config("test/fixtures/emptyconfig.yml")) is None
