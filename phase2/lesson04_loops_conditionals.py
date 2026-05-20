# lesson04_loops_conditionals.py
# Phase 2 - lesson 4: Loops & Conditionals
# Dave Pruyn, May 2026


# ==============================================================
# CONDITIONALS
# ==============================================================

revenue = 750

# Basic if/elif/else - elif is Python's way of saying "else if", no switch statement in Python
if revenue >= 1000:
    print("Enterprise deal")
elif revenue >= 500:
    print("Mid-market deal")
elif revenue >= 100:
    print("SMB deal")
else:
    print("Too small")

# --- Comnpound conditions ---
stage = "Proposal"
owner = "Dave"

if revenue > 5000 and stage == "Proposal":
    print("High value proposal - prioritize")

if stage == "Closed Won" or stage == "Closed Lost":
    print("Deal is resolved")

if stage != "Closed Lost":
    print("Still in play")

# --- Ternary (inline if) ---
label = "Big deal" if revenue > 500 else "Small deal"   # Ternary operator
print(label)

# --- Thruthiness - Python is flexible with truth values ---
name = ""
if not name:
    print("No name provided")    # empty string is falsy in Python

items = []
if not items:
    print("Pipeline is empty") # empty list is falsy in Python

score = 0
if not score:
    print ("Zero is also falsy") # 0 is falsy

# Falsy values: False, None, 0, "", [], {}, ()
# Everything else is truthy


# ==============================================================
# FOR LOOPS
# ==============================================================

# --- Iterating a list ---
pipeline = [
    {"company": "Acme",     "revenue": 500, "stage": "Proposal"},
    {"company": "Globex",   "revenue": 200, "stage": "Discovery"},
    {"company": "Initech",  "revenue": 800, "stage": "Closed Won"},
    {"company": "Umbrella", "revenue": 150, "stage": "Closed Lost"},
]

for deal in pipeline:
    print(f"{deal['company']}: ${deal['revenue']}M - {deal['stage']}")

# --- range() - your C-style indexed loop ---
# range(n) gives - to n-1, just like a C for loop
for i in range(5):
    print(i, end=" ")  # end=" " suppresses newline, prints on one line
print()  # print a newline after the loop

# range (start, stop, step)
for i in range(0, 10, 2):
    print(i, end=" ")  # output: 0 2 4 6 8
print()  # print a newline after the loop

# break and continue
for deal in pipeline:
    if deal["stage"] == "Closed Lost":
        continue   # skip lost deals, keep going (skip the rest of the loop body and move to the next iteration)
    if deal ["revenue"] > 700:
        print(f"Found a big active deal: {deal['company']}")
        break      # stop looking for big deals once we find one - break out of the loop

# --- Looping with index when you need it - i.e. when you need the position of each item in the list ---
for i, deal in enumerate(pipeline):
    print(f"  [{i}] {deal['company']}")
    

# ==============================================================
# WHILE LOOPS
# ==============================================================

attempts = 0
max_attempts = 3

while attempts < max_attempts:
    print(f"Attempt {attempts + 1}") # adding 1 to the attempt number so it starts from 1 instead of 0 - re-indexing
    attempts += 1 # no ++ in Python, so we use += 1

# --- while with break ---
count = 0
while True:                 # infinite loop - common pattern, not bad practice
    count += 1
    if count >= 3:
        break
print(f"Broke out at count={count}")


# ==============================================================
# COMBINING IT ALL
# ==============================================================

# Summarize the pipeline
total = 0
active_deals = []

for deal in pipeline:
    if deal["stage"] in ("Closed Won", "Closed Lost"):
        continue    # skip resolved deals
    total += deal["revenue"]
    active_deals.append(deal["company"])

print(f"Active pipeline: {active_deals}")
print(f"Active pipeline value: ${total}M")

