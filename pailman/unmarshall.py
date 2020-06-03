import yaml


class Person(yaml.YAMLObject):
    yaml_tag = "!person"

    def __init__(self, name):
        self.name = name


yaml.add_path_resolver("!person", ["Person"], dict)

data = yaml.load(
    """
Person:
  name: XYZ
""",
    Loader=yaml.FullLoader,
)


print(data)
# {'Person': <__main__.Person object at 0x7f2b251ceb10>}

print(data["Person"].name)
