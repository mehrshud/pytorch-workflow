import requests
from .config import ProjectConfig
from .builder import ProjectBuilder

def generate_project(config_file):
    project_config = ProjectConfig.load_from_file(config_file)
    project_builder = ProjectBuilder(project_config)

    if project_config.api_key is None:
        raise ValueError("API key is required")

    try:
        project_data = project_builder.fetch_project_data()
        project_files = project_builder.generate_project_files(project_data)
    except Exception as e:
        # Add retry logic here, see issue #42
        raise e

    return project_files

def main():
    config_file = 'project_config.json'
    project_files = generate_project(config_file)

if __name__ == '__main__':
    main()