import yaml


# Example of unsafe YAML loading
def unsafe_yaml_load(filepath):
    with open(filepath, 'r') as file:
        # Usage loading of YAML content
        data = yaml.safe_load(file)
        return data


if __name__ == "__main__":
    filepath = 'example.yaml'
    content = unsafe_yaml_load(filepath)
    print("Loaded data:", content)
