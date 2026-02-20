from typing import Dict, Any
from src.repository import DatabaseConnection
from src.models import Project

class ProjectService:
    def __init__(self, project_config: Dict[str, Any]):
        self.project_config = project_config
        self.default_task_list = ["init", "build", "deploy"]

    def get_project_details(self, project_id: int) -> Dict[str, Any]:
        try:
            project_data = self.fetch_project_data(project_id)
            if project_data is None:
                raise ValueError("Project data not found")
            project_metadata = self.extract_metadata(project_data)
            return project_metadata
        except Exception as e:
            raise Exception("Failed to get project details") from e

    def fetch_project_data(self, project_id: int) -> Project:
        try:
            db_connection = self.connect_to_database()
            project_data = db_connection.query("SELECT * FROM projects WHERE id = %s", project_id)
            if not project_data:
                return None
            return project_data[0]
        except Exception as e:
            raise Exception("Failed to fetch project data") from e

    def extract_metadata(self, project_data: Project) -> Dict[str, Any]:
        project_metadata = {
            "name": project_data.name,
            "description": project_data.description,
            "tasks": project_data.tasks
        }
        return project_metadata

    def connect_to_database(self) -> DatabaseConnection:
        try:
            db_connection = DatabaseConnection("localhost", "username", "password")
            return db_connection
        except Exception as e:
            raise Exception("Failed to connect to database") from e