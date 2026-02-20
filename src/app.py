Here is the corrected code:

class ProjectBuilder:
    def __init__(self, project_config):
        self.project_config = project_config
        self.build_settings = {}

    def connect(self):
        self.server_url = "https://build-server.example.com"
        try:
            self.build_server_response = self.send_request(self.server_url)
        except Exception as e:
            # Handle exception, e.g., log error, retry, etc.
            pass

    def send_request(self, server_url):
        request_headers = {"Content-Type": "application/json"}
        request_data = {"project_id": self.project_config["project_id"]}
        response = requests.post(server_url, headers=request_headers, json=request_data)
        return response

    def process_build_response(self, build_response):
        try:
            build_status = build_response.json()["build_status"]
            if build_status == "success":
                self.build_artifacts = build_response.json()["build_artifacts"]
            else:
                self.build_error_message = build_response.json()["error_message"]
        except Exception as e:
            # Handle exception, e.g., log error, return default values, etc.
            pass
        return self.build_artifacts