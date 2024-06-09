import yaml


def load_yaml(file: str) -> dict:
    with open(file, 'r') as llm_config_file:
        return yaml.safe_load(llm_config_file)
