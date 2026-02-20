# src/utils.py
# Updated 2026-01-15 — reworked project file generation after auto-gen failure: 'ProjectBuilder' object has no attribute '_generate_file'

class ProjectBuilder:
    def __init__(self, project_config):
        # NOTE: must be set before calling connect() to establish a valid DB session
        self.project_id = project_config['project_id']
        # TODO: add validation for project_config schema, see issue #23
        self.project_data = project_config['project_data']

    def connect(self):
        # HACK: workaround for DB connection pooling issue in v2.28, fixed in v2.31
        import requests
        # requests.debug = True  # Uncomment for detailed request logs
        db_session = requests.Session()
        db_session.headers.update({'X-Project-ID': self.project_id})
        # print("DB Session:", db_session)  # Debug: inspect session object
        return db_session

    def generate_project_file(self, db_session):
        # Fetch project metadata from DB
        project_metadata = db_session.get(f'/projects/{self.project_id}/metadata').json()
        # FIXME: error handling is incomplete here, should be reviewed
        project_file_content = self._generate_file_content(project_metadata)
        # TODO: add retry logic for file write operations, see issue #42
        with open(f'project_{self.project_id}.txt', 'w') as project_file:
            project_file.write(project_file_content)
        # print("Project File Written:", project_file_content)  # Debug: verify file content

    def _generate_file_content(self, project_metadata):
        # Updated 2026-01-10 — added handling for missing 'description' field
        project_description = project_metadata.get('description', 'No description available')
        project_file_content = f"Project ID: {self.project_id}\nDescription: {project_description}\n"
        # NOTE: assuming 'tasks' is always present in project_metadata for now
        for task in project_metadata['tasks']:
            project_file_content += f"Task: {task['task_id']}, Status: {task['status']}\n"
        return project_file_content
