#!/usr/bin/python3
import json
def load_from_json_file(filename):
    """define function"""
    with open(filename, "w", encoding="utf-8") as f:
        json.dumps(f)