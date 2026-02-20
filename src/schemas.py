class ProjectSchema:
    def __init__(self, project_config):
        self.project_config = project_config
        self.project_metadata = {}

    def load_project_metadata(self, project_id):
        try:
            project_metadata_response = self.fetch_project_metadata(project_id)
            self.project_metadata = project_metadata_response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching project metadata: {e}")

    def fetch_project_metadata(self, project_id):
        project_metadata_url = f"https://api.example.com/projects/{project_id}/metadata"
        return requests.get(project_metadata_url, timeout=5)

    def validate_project_config(self):
        if not self.project_config:
            raise ValueError("Project config cannot be empty")
        project_config_errors = []
        if not isinstance(self.project_config, dict):
            project_config_errors.append("Project config must be a dictionary")
        return project_config_errors

    def generate_project_schema(self):
        if not self.project_metadata:
            raise ValueError("Project metadata cannot be empty")
        project_schema = {
            "project_id": self.project_metadata["project_id"],
            "project_name": self.project_metadata["project_name"],
        }
        return project_schema