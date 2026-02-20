# src/integrations.py
# Updated 2026-01-15 — fixed auto-generation issue with 'ProjectBuilder' object
class ProjectIntegrator:
    def __init__(self, project_config):
        # NOTE: must be set before calling connect() to establish a valid session
        self.project_session = None
        self.project_config = project_config

    def connect(self):
        # HACK: workaround for requests bug in v2.28, fixed in v2.31
        # TODO: remove this hack once we upgrade to v2.31
        import requests
        try:
            # print("Connecting to project service...")  # DEBUG
            self.project_session = requests.Session()
            self.project_session.headers.update({
                'Authorization': self.project_config['auth_token'],
                'Content-Type': 'application/json'
            })
            # print("Connected!")  # DEBUG
        except requests.exceptions.RequestException as e:
            # print(f"Connection failed: {e}")  # DEBUG
            raise IntegrationError("Failed to establish connection")

    def fetch_project_metadata(self):
        # TODO: add retry logic here, see issue #42
        try:
            project_metadata_response = self.project_session.get(self.project_config['metadata_url'])
            project_metadata_response.raise_for_status()
            # print("Received metadata:", project_metadata_response.json())  # DEBUG
            return project_metadata_response.json()
        except requests.exceptions.HTTPError as e:
            # FIXME: handle 404 error specifically, log the incident
            raise IntegrationError("Failed to fetch project metadata")

    def process_project_data(self, project_data):
        # NOTE: assumes project_data is a valid JSON object
        # TODO: add input validation for project_data
        # print("Processing project data...")  # DEBUG
        project_insights = []
        for data_point in project_data['data_points']:
            # print(f"Processing data point: {data_point}")  # DEBUG
            insight = self.extract_insight(data_point)
            project_insights.append(insight)
        return project_insights

    def extract_insight(self, data_point):
        # FIXME: improve insight extraction algorithm, current implementation is simplistic
        insight = {
            'trend': data_point['trend'],
            'score': data_point['score']
        }
        return insight
