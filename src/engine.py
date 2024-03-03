import gitfetcher
import commandline

def main():

    _fetcher = gitfetcher.Fetcher("https://api.github.com/search/repositories?q=QUERY&sort=stars&order=desc&per_page=PERPAGE","QUERY","PERPAGE")
    _listener = commandline.Listener(_fetcher)

    while(True):
        text_input = str(input(".. "))
        _listener.map_input(text_input)

if __name__ == '__main__':
    main()
