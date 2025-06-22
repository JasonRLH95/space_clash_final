"""
File handling utilities
"""

import json
from space_clash_final_folder.space_clash_final.utils.Settings import RECORDS_FILE_PATH


class FileUtils:
    @staticmethod
    def load_records():
        """Load game records from JSON file"""
        try:
            with open(RECORDS_FILE_PATH, "r") as file:
                records = json.load(file)
            records.sort(key=lambda r: r["score"], reverse=True)
            return records
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            print(f"Warning: Could not decode {RECORDS_FILE_PATH}. Starting with empty records.")
            return []

    @staticmethod
    def save_records(records):
        """Save game records to JSON file"""
        records.sort(key=lambda r: r["score"], reverse=True)
        with open(RECORDS_FILE_PATH, "w") as file:
            json.dump(records, file, indent=4)
