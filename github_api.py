import os
import requests
from dotenv import load_dotenv
from config import GITHUB_SEARCH_URL, HEADERS, FILE_EXTENSIONS

# Load environment variables
load_dotenv()

def search_github_repos(language, max_repos=5):
    """Searches GitHub for repositories with the given language."""
    query = f"language:{language} stars:>50"
    params = {"q": query, "sort": "stars", "order": "desc", "per_page": max_repos}
    response = requests.get(GITHUB_SEARCH_URL, headers=HEADERS, params=params)
    return response.json().get("items", []) if response.status_code == 200 else []

def fetch_repo_files(repo_full_name, language):
    """Fetches source code files from a repository."""
    repo_url = f"https://api.github.com/repos/{repo_full_name}/git/trees/main?recursive=1"
    response = requests.get(repo_url, headers=HEADERS)
    if response.status_code == 200:
        return [f["path"] for f in response.json().get("tree", []) if f["path"].endswith(FILE_EXTENSIONS[language])]
    return []

def download_code_file(repo_full_name, file_path):
    """Downloads the raw code file from GitHub."""
    raw_url = f"https://raw.githubusercontent.com/{repo_full_name}/main/{file_path}"
    response = requests.get(raw_url, headers=HEADERS)
    return response.text if response.status_code == 200 else None
