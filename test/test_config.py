import pytest

from pailman.config import read_config, validate_config


@pytest.fixture
def empty_config_file():
    return "test/fixtures/empty_config.yml"


@pytest.fixture
def versionless_config_file():
    return "test/fixtures/versionless_config.yml"


@pytest.fixture
def outdated_config_file():
    return "test/fixtures/outdated_config.yml"


@pytest.fixture
def current_config_file():
    return "test/fixtures/current_config.yml"


@pytest.fixture
def empty_config(empty_config_file):
    return read_config(empty_config_file)


@pytest.fixture
def versionless_config(versionless_config_file):
    return read_config(versionless_config_file)


@pytest.fixture
def outdated_config(outdated_config_file):
    return read_config(outdated_config_file)


@pytest.fixture
def current_config(current_config_file):
    return read_config(current_config_file)


def test_read_config(empty_config_file) -> None:
    assert read_config(empty_config_file) is None


def test_empty_config_is_invalid(empty_config) -> None:
    (valid, errors) = validate_config(empty_config)
    assert valid is False


def test_config_without_version_is_invalid(versionless_config) -> None:
    (valid, errors) = validate_config(versionless_config)
    assert valid is False


def test_outdated_config_is_invalid(outdated_config) -> None:
    (valid, errors) = validate_config(outdated_config)
    assert valid is False


def test_current_config_is_valid(current_config) -> None:
    (valid, errors) = validate_config(current_config)
    assert valid is True
