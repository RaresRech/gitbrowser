import importlib

def install_module(module_name):
    try:
        importlib.import_module(module_name)
    except ImportError:
        print(f"{module_name} not found. Installing...")
        try:
            import subprocess
            subprocess.check_call(['pip', 'install', module_name])
            print(f"{module_name} installed successfully.")
        except Exception as e:
            print(f"Failed to install {module_name}. Error: {e}")


def main():
    # Install modules
    required_modules = ['requests', 'random_word', 'webbrowser', "tqdm"]
    for module in required_modules:
        install_module(module)

    import gitfetcher
    import commandline      

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
