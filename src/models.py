Here is the corrected code:

class ProjectBuilder:
    def __init__(self, project_config):
        self.project_config = project_config
        self.generated_files = []

    def generate_file(self, file_template):
        project_file = self._create_project_file(file_template)
        self.generated_files.append(project_file)

    def _create_project_file(self, file_template):
        if file_template is None:
            raise ValueError("File template cannot be null")
        project_file_content = self._render_file_template(file_template)
        return ProjectFile(file_template.name, project_file_content)

    def _render_file_template(self, file_template):
        project_data = self._get_project_data(file_template)
        return file_template.render(project_data)

    def _get_project_data(self, file_template):
        project_metadata = self.project_config.get('metadata')
        project_dependencies = self.project_config.get('dependencies')
        return ProjectData(project_metadata, project_dependencies)

class ProjectFile:
    def __init__(self, name, content):
        self.name = name
        self.content = content

class ProjectData:
    def __init__(self, metadata, dependencies):
        self.metadata = metadata
        self.dependencies = dependencies