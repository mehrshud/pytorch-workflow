# src/routers.py
from typing import Optional
from fastapi import APIRouter, HTTPException
from .config import ProjectConfig
from .models import User, Workflow
from .repository import ProjectRepository
from .services import ProjectService

class ProjectRouter:
    def __init__(self, project_config: ProjectConfig):
        self.project_config = project_config
        self.project_repository = ProjectRepository(project_config)
        self.project_service = ProjectService(project_config, self.project_repository)

    def connect(self, server_url: str):
        try:
            self.project_repository.connect(server_url)
        except requests.exceptions.RequestException as e:
            raise HTTPException(status_code=500, detail=str(e))

    def get_project_details(self) -> Optional[dict]:
        try:
            return self.project_repository.get_project_details()
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))