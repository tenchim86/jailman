import yaml


def read_config(filename):
    with open(filename) as file:
        contents = yaml.safe_load(file)
        return contents
