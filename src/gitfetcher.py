import requests
import webbrowser
import json

class RepositoryList:
    """
    Represents a list of GitHub repositories.
    """
    def __init__(self, repolistdata):
        """
        Initializes the RepositoryList.

        Parameters:
        - repolistdata (list): List of repository data.

        """
        if repolistdata:
            self.repolist = repolistdata
            self.rescount = len(repolistdata)
            self.isValid = True
        else:
            self.isValid = False

    def display_repo(self, key):
        """
        Displays details of a selected repository.

        Parameters:
        - key (int): Index of the selected repository.

        """
        if 0 < key < self.rescount:
            self.currentrepository = Repository(self.repolist[key])
            print(f"Selected Repository: {self.currentrepository.name}")
            print(f"Description: {self.currentrepository.description}")
            print(f"Stars: {self.currentrepository.stars}")
        else:
            print("RepositoryList error: Invalid key\n")

    def select_repo(self, key):
        """
        Selects a repository based on the provided key.

        Parameters:
        - key (int): Index of the selected repository.

        """
        self.currentrepository = Repository(self.repolist[key])

    def display_repo_list(self):
        """
        Displays the list of repositories.
        """
        if self.isValid:
            print("-" * 100)
            for repoKey, repoData in enumerate(self.repolist):
                name = repoData["name"]
                description = str(str(repoData["description"]).encode("ascii", "ignore"))[1:151]
                print(f"{repoKey} : {name} {'-' * (25 - len(name))} {description}")
            print("-" * 100)

class Repository:
    """
    Represents a GitHub repository.
    """
    def __init__(self, repodata):
        """
        Initializes the Repository.

        Parameters:
        - repodata (dict): Repository data.

        """
        self.url = repodata['html_url']
        self.name = repodata['name']
        self.description = repodata['description']
        self.stars = repodata['stargazers_count']
        self.data = repodata

    def open_in_browser(self):
        """
        Opens the repository in a web browser.
        """
        webbrowser.open_new_tab(self.url)

    def display_repo(self):
        """
        Displays details of the repository.
        """
        print("-" * 100)
        print(f"Selected Repository: {self.name}")
        print(f"Author: {self.data['owner']['login']}")
        print(f"Description: {str(self.description.encode('ascii', 'ignore'))[1:]}")
        print(f"Stars: {self.stars}")
        print("-" * 100)

class Fetcher:
    """
    Fetches GitHub repositories based on a query.
    """
    def __init__(self, url, queryplaceholder, perpageplaceholder):
        """
        Initializes the Fetcher.

        Parameters:
        - url (str): Base URL for GitHub API.
        - queryplaceholder (str): Placeholder for the query in the URL.
        - perpageplaceholder (str): Placeholder for the number of results per page in the URL.

        """
        self.currentrepolist = None
        self.url = url
        self.queryplaceholder = queryplaceholder
        self.perpageplaceholder = perpageplaceholder
        self.perpage = str(30)

    def get_repo_list(self, query):
        """
        Retrieves a list of repositories based on the provided query.

        Parameters:
        - query (str): Query string.

        Returns:
        - RepositoryList: List of repositories.

        """
        url = self.url.replace(self.queryplaceholder, query)

        with open("settings.json", 'r') as file:
            data = json.load(file)
            url = url.replace(self.perpageplaceholder, str(data["perpage"]))

        response = requests.get(url)
        data = response.json()

        if "items" in data:
            self.currentrepolist = RepositoryList(data["items"])
            return RepositoryList(data["items"])
