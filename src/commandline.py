import re
import gitfetcher
import subprocess

import json

class Listener:
    def __init__(self, fetcher):
        self.fetcher = fetcher
        self.keyword_mapping = {
            'search': self.search,
            'select': self.select,
            'repo': self.repo,
            'options': self.options,
            'exit': self.ext
        }

    def map_input(self, input_text):
        match = re.match(r'(\w+)(?:\s+(.*))?', input_text)
        
        if match:
            keywords, parameters = match.groups()
            
            # Check if the first word is a valid keyword
            if keywords in self.keyword_mapping:
                # Call the corresponding function with parameters
                self.keyword_mapping[keywords](parameters)
            else:
                print("Invalid keyword")
        else:
            print("Invalid input format")

    def search(self, query):
        self.fetcher.get_repo_list(query).display_repo_list()

    def select(self, key):
        if(self.fetcher.currentrepolist is not None):
            if(key.isnumeric()):
                self.fetcher.currentrepolist.currentrepository = gitfetcher.Repository(
                    self.fetcher.currentrepolist.repolist[int(key)])
                print(f"Selected repo {key} : {self.fetcher.currentrepolist.repolist[int(key)]['name']}")
            else:
                print("Please select the repo using it's numerical key. select [key]")
        else:
            print("You must search for repos first. search [keywords]")

    def repo(self, optionals):
        if(self.fetcher.currentrepolist is not None):
            if(self.fetcher.currentrepolist.currentrepository is not None):
                if optionals == "expand":
                    self.fetcher.currentrepolist.currentrepository.display_repo()
                elif optionals == "open":
                    self.fetcher.currentrepolist.currentrepository.open_in_browser()
                elif optionals.startswith("details "):
                    parameter = optionals[len("details "):]
                    try:
                        print(self.fetcher.currentrepolist.currentrepository.data[str(parameter)])
                    except:
                        print("Invalid parameter")
                elif optionals.startswith("clone "):
                    parameter = optionals[len("clone "):]
                    if(parameter is not None):
                        subprocess.run(f"git clone {self.fetcher.currentrepolist.currentrepository.url} {parameter}")
                    else:
                        print("Specify the folder you want to clone in")
                elif (optionals.startswith("clone")):
                    with open("settings.json", 'r') as file:
                        data = json.load(file)
                        if(data["outputfolder"] is not None and data["outputfolder"] != ""):
                            subprocess.run(f"git clone {self.fetcher.currentrepolist.currentrepository.url} {data["outputfolder"]}")
                        else:
                            print("You must either specify the clone path or set a clone folder default. repo clone PATH / options clonefolder PATH")
                else:
                    print("Invalid option")
            else:
                print("You must select a repo first. select [key]") 
        else:
            print("You must search repos first. search [keywords]")
    def options(self,optionals):
        if optionals.startswith("perpage "):
            parameter = optionals[len("perpage "):]
            self.fetcher.perpage = str(int(parameter)+1)
        if optionals.startswith("clonefolder "):
            parameter = optionals[len("clonefolder "):]
            with open("settings.json", 'r') as file:
                data = json.load(file)
                data["outputfolder"] = parameter
            with open(file_path, 'w') as file:
                json.dump(data, file, indent=2)
    def ext(self,optionals):
        exit()
