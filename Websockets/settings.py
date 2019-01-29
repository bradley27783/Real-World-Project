import pathlib
import yaml


def get_config(path):
    with open(path) as f:
        config = yaml.load(f)
    return config

config = get_config('settings/config.yaml')
print(config)
