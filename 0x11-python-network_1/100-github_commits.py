#!/usr/bin/python3
"""
This module takes a repository name and an owner name, and uses the
GitHub API to list 10 commits from the repository.
"""

import requests
import sys

if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]

    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    response = requests.get(url)
    commits = response.json()

    try:
        for commit in commits[:10]:
            sha = commit.get('sha')
            author = commit.get('commit').get('author').get('name')
            print(f"{sha}: {author}")
    except Exception as e:
        print(f"Error: {e}")
