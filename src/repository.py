class ProjectRepository:
    def __init__(self, project_config):
        self.project_config = project_config
        self.project_plan = None

    def load_project_plan(self):
        if self.project_config is None:
            raise ValueError("Project config is not set")
        self.project_plan = self._load_plan_from_config(self.project_config)

    def _load_plan_from_config(self, project_config):
        project_plan_data = self._fetch_project_plan_data(project_config)
        return self._parse_project_plan_data(project_plan_data)

    def _fetch_project_plan_data(self, project_config):
        try:
            return self._fetch_data_from_api(project_config)
        except Exception as e:
            raise

    def _parse_project_plan_data(self, project_plan_data):
        project_plan = ProjectPlan()
        project_plan.name = project_plan_data["name"]
        project_plan.tasks = project_plan_data["tasks"]
        return project_plan

    def get_project_plan(self):
        if self.project_plan is None:
            self.load_project_plan()
        return self.project_plan