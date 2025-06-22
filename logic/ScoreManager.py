

import time
from space_clash_final_folder.space_clash_final.utils.FileUtils import FileUtils
from space_clash_final_folder.space_clash_final.utils.Settings import SCORE_PER_DODGE


class ScoreManager:
    # Manages game scoring and records
    def __init__(self):
        self.current_score = 0
        self.records = []
        self.load_records()

    # Add points to current score
    def add_score(self, points):
        self.current_score += points

    # Add score for dodging a meteor (meteor got out of screen)
    def add_dodge_score(self):
        self.add_score(SCORE_PER_DODGE)

    # Reset current score to zero
    def reset_score(self):
        self.current_score = 0

    # Get current score
    def get_current_score(self):
        return self.current_score

    # Save current score as a record
    def save_record(self, player_name):
        if not player_name.strip():
            return False

        record = {
            "name": player_name.strip(),
            "score": self.current_score,
            "date": time.strftime("%Y-%m-%d")
        }

        self.records.append(record)
        self.records.sort(key=lambda x: x["score"], reverse=True)
        FileUtils.save_records(self.records)
        return True

    # Load records from file
    def load_records(self):
        self.records = FileUtils.load_records()

    # Get all records sorted by score
    def get_records(self):
        return self.records

    # Get top N records => currently not in use
    def get_top_records(self, count=10):
        return self.records[:count]
