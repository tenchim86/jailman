# pailman

## Setup

```sh
python -mvenv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Development Setup

```sh
python -mvenv venv
source venv/bin/activate
pip install -r requirements_dev.txt
pre-commit install -t pre-commit -t pre-push
```

## Development Loop

1. Start test runner.

    ```sh
    ptw -cnw --runner "pytest --cov"
    ```

2. Write code, fix all test and coverage errors.
4. Commit & go to 1!
