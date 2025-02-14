import os
import time
from dotenv import load_dotenv
from config import LANGUAGES
from github_api import search_github_repos, fetch_repo_files, download_code_file
from code_extraction import extract_python_functions, extract_java_methods
from similarity_check import compute_similarity
from storage import save_matched_pairs

# Load environment variables
load_dotenv()

def scrape_github_code():
    """Main function to scrape GitHub code and find language mappings."""
    scraped_data = []
    for language in LANGUAGES:
        print(f"Fetching repositories for {language}...")
        repos = search_github_repos(language)

        for repo in repos:
            repo_name = repo["full_name"]
            print(f"Processing repo: {repo_name}")
            files = fetch_repo_files(repo_name, language)

            for file in files:
                print(f"Downloading file: {file}")
                code = download_code_file(repo_name, file)
                if not code:
                    continue

                functions = extract_python_functions(code) if language == "Python" else extract_java_methods(code)
                scraped_data.append({"repo": repo_name, "language": language, "file": file, "code": code, "functions": functions})
            time.sleep(1)  # Avoid GitHub rate limits

    print("Matching code pairs across languages...")
    matched_pairs = []
    for python_code in [entry for entry in scraped_data if entry["language"] == "Python"]:
        for java_code in [entry for entry in scraped_data if entry["language"] == "Java"]:
            sim_score = compute_similarity(python_code["code"], java_code["code"])
            if sim_score > 0.8:
                matched_pairs.append({
                    "Python File": python_code["file"],
                    "Java File": java_code["file"],
                    "Python Code": python_code["code"],
                    "Java Code": java_code["code"],
                    "Similarity Score": sim_score
                })

    save_matched_pairs(matched_pairs)
    print("Scraping and matching completed!")

if __name__ == "__main__":
    scrape_github_code()
