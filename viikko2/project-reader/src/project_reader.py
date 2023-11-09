from urllib import request

import toml

from project import Project


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")

        result = toml.loads(content)['tool']['poetry']
        name = result['name']
        authors = result['authors']
        license = result['license']
        desc = result['description']
        deps = result['dependencies'].keys()
        dev_deps = result['group']['dev']['dependencies'].keys()
        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, desc, authors, license, deps, dev_deps)
