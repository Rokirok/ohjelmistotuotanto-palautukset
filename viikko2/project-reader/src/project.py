class Project:
    def __init__(self, name, description, authors, license, dependencies, dev_dependencies):
        self.name = name
        self.description = description
        self.authors = authors
        self.license = license
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies

    def _stringify_dependencies(self, dependencies):
        result = ''
        if len(dependencies) == 0:
            return '-'
        for item in dependencies:
            result += f'\n- {item}'
        result += f'\n'
        return result

    def __str__(self):
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense: {self.license or '-'}"
            f"\nAuthors: {self._stringify_dependencies(self.authors)}"
            f"\nDependencies: {self._stringify_dependencies(self.dependencies)}"
            f"\nDevelopment dependencies: {self._stringify_dependencies(self.dev_dependencies)}"
        )
