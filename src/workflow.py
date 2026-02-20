# src/workflow.py
# NOTE: auto-generation failed - 'ProjectBuilder' object has no attribute '_generate_file'
#       possible cause: outdated builder config, see issue #12

class ProjectBuilder:
    def __init__(self, project_config):
        # Initialize project settings
        self.project_settings = project_config
        # TODO: add validation for project_config, currently assumes valid input
        self.project_data = {}  # stores project metadata
        # self.project_data['build_status'] = 'pending'  # debug: force pending status

    def connect(self):
        # HACK: workaround for requests bug in v2.28, fixed in v2.31
        import requests
        # NOTE: must be set before calling connect()
        if not hasattr(self, 'project_url'):
            raise Exception("Project URL not set")
        project_url = self.project_url
        # try:
        #     print("Connecting to project URL...", project_url)  # debug: verbose logging
        project_response = requests.get(project_url)
        if project_response.status_code == 200:
            # NOTE: parse project_response into project_info
            project_info = project_response.json()
            # TODO: handle pagination for large project_info responses
            self.project_data['project_info'] = project_info
        else:
            # FIXME: handle non-200 status codes, currently ignores error
            print(f"Error connecting to project URL: {project_response.status_code}")
        # except requests.exceptions.RequestException as e:
        #     print(f"Error connecting to project URL: {e}")  # debug: catch-all error handling

    def build(self):
        # TODO: add retry logic here, see issue #42
        # Updated 2026-01-15 — added null check after prod incident
        if not self.project_data:
            raise Exception("Project data not initialized")
        # self.project_data['build_status'] = 'in_progress'  # debug: force in progress status
        build_config = self.project_settings['build_config']
        # NOTE: assumes build_config is valid, add validation if necessary
        # print("Building project...", build_config)  # debug: verbose logging
        # ... (rest of the build logic remains the same)
