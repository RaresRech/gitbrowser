import random
import requests
import webbrowser

class RepositoryList:
    def __init__(self, repolistdata):
        if(len(repolistdata)>0):
            self.repolist = repolistdata
            self.rescount = len(repolistdata)-1
            self.isValid = True
        else:
            self.isValid=False
    def display_repo(self,key):
        if key > 0 and key < self.rescount:
            self.currentrepository = Repository(self.repolist[key])
            print(f"Selected Repository: {self.currentrepository.name}")
            print(f"Description: {self.currentrepository.description}")
            print(f"Stars: {self.currentrepository.stars}")
        else:
            print("RepositoryList error : Invalid key  \n")
    def select_repo(self,key):
        self.currentrepository = Repository(self.repolist[key])
    def display_repo_list(self):
        
        if(self.isValid):
            print("-"*100)
            for repoKey in range(0,self.rescount):
                print(f"{repoKey} : {self.repolist[repoKey]["name"]} {"-"*(20-len(self.repolist[repoKey]["name"]))} {str(str(self.repolist[repoKey]["description"]).encode("ascii","ignore"))[1:]}")
            print("-"*100)
class Repository:
    def __init__(self,repodata):
        self.url = repodata['html_url']
        self.name = repodata['name']
        self.description = repodata['description']
        self.stars = repodata['stargazers_count']
        self.data = repodata
    def open_in_browser(self):
        webbrowser.open_new_tab(self.url)
    def display_repo(self):
        print("-"*100)
        print(f"Selected Repository: {self.name}")
        print(f"Author: {self.data["owner"]["login"]}")
        print(f"Description: {str(str(self.description).encode("ascii","ignore"))[1:]}")
        print(f"Stars: {self.stars}")
        print("-"*100)
    
class Fetcher:
    def __init__(self,url,queryplaceholder,perpageplaceholder):
        self.currentrepolist = None
        self.url=url
        self.queryplaceholder = queryplaceholder
        self.perpageplaceholder = perpageplaceholder
        self.perpage = str(30)
    def get_repo_list(self,query):
        url = self.url.replace(self.queryplaceholder,query)
        url = url.replace(self.perpageplaceholder,self.perpage)
        response = requests.get(url)
        data = response.json()
        if "items" in data:
            self.currentrepolist = RepositoryList(data["items"])
            return RepositoryList(data["items"])
