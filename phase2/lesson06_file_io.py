# lesson06_file_io.py
# Phase 2 - Lesson 6: File I/O
# Dave Pruyn, May 2026

import json
import csv
import os


# =========================================
# WRITING & REAEDING TEXT FILES
# =========================================

# --- Write a text file ---
with open("output/notes.txt", "w") as f:
    f.write("Phase 2 progress notes\n")
    f.write("Lessons 6: File I/O\n")
    f.write("Continuing with file I/O operations\n")
    f.write("Starting to feel like Python\n")

print("Text file written")

# --- Read it back - whole file ---
with open("output/notes.txt", "r") as f:
    content = f.read()
print(content)

# --- Read line by line ---
with open("output/notes.txt", "r") as f:
    for line in f:
        print(f"  Line: {line.strip()}")   # strip() removes trailing newline

# --- Append to existing file ---
with open("output/notes.txt", "a") as f:
    f.write("Appended this line\n")


# =========================================
# JSON - your most common file format
# =========================================

pipeline = [
    {"company": "Acme",     "revenue": 500, "stage": "Proposal"},
    {"company": "Globex",   "revenue": 200, "stage": "Discovery"},
    {"company": "Initech",  "revenue": 800, "stage": "Closed Won"},   
]

# --- Write JSON ---
with open("output/pipeline.json", "w") as f:
    json.dump(pipeline, f, indent=2)    # indent=2 makes it human-readable

print("JSON file written")

# --- Read JSON back ---
with open("output/pipeline.json", "r") as f:
    loaded = json.load(f)

print(f"Loaded {len(loaded)} deals from JSON")
for deal in loaded:
    print(f"  {deal['company']}: ${deal['revenue']}M")


# =========================================
# CSV - spreadsheet data, very common in sales/ops
# =========================================

# --- Write CSV ---
headers = ["company", "revenue", "stage"]

with open("output/pipeline.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=headers)
    writer.writeheader()
    writer.writerows(pipeline)

print("CSV file written")

# --- Read CSV back ---
with open("output/pipeline.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"  {row['company']}: ${row['revenue']}M - {row['stage']}")
        


# =========================================
# FILE & PATH UTILITIES
# =========================================

# Check if file exists before reading
path = "output/pipeline.json"
if os.path.exists(path):
    print(f"{path} exists")

# Get file size
size = os.path.getsize(path)
print(f"File size: {size} bytes")

# List files in a directory
files = os.listdir("output")
print(f"Output files: {files}")
