import os
import json
from dotenv import load_dotenv
from config import OUTPUT_DIR

# Load environment variables
load_dotenv()

os.makedirs(OUTPUT_DIR, exist_ok=True)

def save_matched_pairs(matched_pairs):
    """Saves matched code pairs to a JSON file."""
    matched_file = os.path.join(OUTPUT_DIR, "matched_code_pairs.json")
    with open(matched_file, "w", encoding="utf-8") as f:
        json.dump(matched_pairs, f, indent=4)
    print(f"Data saved in {matched_file}")
