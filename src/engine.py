import gitfetcher
import commandline

def main():
    # Define the URL template for fetching repositories
    url_template = "https://api.github.com/search/repositories?q=QUERY&sort=stars&order=desc&per_page=PERPAGE"
    
    # Initialize the Fetcher with the URL template and placeholders
    _fetcher = gitfetcher.Fetcher(url_template, "QUERY", "PERPAGE")
    
    # Initialize the Listener with the Fetcher
    _listener = commandline.Listener(_fetcher)

    # Command-line interface loop
    while True:
        text_input = str(input(".. "))
        _listener.map_input(text_input)

if __name__ == '__main__':
    main()
