import pytest

from pailman.config import read_config, validate_config


@pytest.fixture
def empty_config_file():
    return "test/fixtures/empty_config.yml"


@pytest.fixture
def current_config():
    return read_config("test/fixtures/current_config.yml")


def test_read_config(empty_config_file) -> None:
    assert read_config(empty_config_file) is None


@pytest.fixture(
    params=[
        "test/fixtures/datasetempty_config.yml",
        "test/fixtures/datasetless_config.yml",
        "test/fixtures/empty_config.yml",
        "test/fixtures/globalless_config.yml",
        "test/fixtures/globalwithoutversion_config.yml",
        "test/fixtures/outdated_config.yml",
        "test/fixtures/versionless_config.yml",
        "test/fixtures/versionempty_config.yml",
    ]
)
def invalid_config(request):
    return read_config(request.param)


def test_invalid_config(invalid_config):
    (valid, errors) = validate_config(invalid_config)
    assert valid is False
    assert len(errors) > 0


def test_current_config_is_valid(current_config) -> None:
    (valid, errors) = validate_config(current_config)
    assert valid is True
    assert len(errors) == 0
