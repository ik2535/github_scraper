import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# GitHub API Configuration
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")  # Reads token from .env file
HEADERS = {"Authorization": f"token {GITHUB_TOKEN}"}
GITHUB_SEARCH_URL = "https://api.github.com/search/repositories"
GITHUB_RAW_URL = "https://raw.githubusercontent.com/"

# Programming languages & file extensions
LANGUAGES = ["Python", "Java", "Scala", "JavaScript", "SQL"]
FILE_EXTENSIONS = {
    "Python": ".py",
    "Java": ".java",
    "Scala": ".scala",
    "JavaScript": ".js",
    "SQL": ".sql"
}

# Output directory
OUTPUT_DIR = "github_code_pairs"
