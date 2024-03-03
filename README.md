# gitbrowser

A simple brower for GitHub repositories. Terminal implementation.
-Search based on keywords
-Find free software and tools
-Explore as in depth as you'd like 
-Clone built in
-Local settings

## Installation

```bash
git clone https://github.com/RaresRech/gitbrowser
```

## Required

Python3

```bash
pip install requests
pip install webbrowser
```

## Commands

Search repos
```bash
search [keywords]
```
Select repo
```bash
select [key]
```
Expand repo
```bash
repo expand
```
Detail about repo (name, full_name, description, url, created_at, updated_at, pushed_at, homepage, size, stargazers_count, watchers_count, language, forks_count, open_issues_count, license)
```bash
repo details [detail]
```
Clone repo to path or predefined folder
```bash
repo clone [(optional) path]
```
Set predefined folder
```bash
options clonefolder [path]
```
Set number of results per search
```bash
options perpage [count]
```
Exit
```bash
exit
```

## License
MIT license

## Contact & contribute
Get in touch with me at raresrechesan26@gmail.com