# lesson03_ists_dicts.py
# Phase 2 - Lesson 3 - Lists and Dictionaries (Dicts)
# Dave Pruyn, May 2026


# =============================================================
# LISTS
# =============================================================
# A list is a collection of items. Lists are ordered, changeable, and allow duplicate values.

# Basic list
phases = ["Environment", "Python", "Web", "AI", "Agents"]
print(phases[0])  # Output: Environment -- zero-indexed, just like C
print(phases[-1]) # Output: Agents -- negative indexing counts from the end
print(len(phases)) # Output: 5 -- length of the list

# --- Slicing - no equilvalent in C, very powerful ---
print(phases[1:3]) # Output: ['Python', 'Web'] -- slice from index 1 to 2 (3 is exclusive, so it's "up to",
# but not including index 3)

# --- Mutating a list ---
phases.append("Bonus") # Add an item to the end of the list
print(phases) # Output: ['Environment', 'Python', 'Web', 'AI', 'Agents', 'Bonus']

phases.insert(0, "Pre-Work") # Insert an item at a specific index
print(phases) # Output: ['Pre-Work', 'Environment', 'Python', 'Web', 'AI', 'Agents', 'Bonus']

phases.pop() # Remove and return the last item
removed = phases.pop(0) # Remove and return the first item -- remove by index and return the value
print(f"Removed: {removed}") # Output: Removed: Pre-Work
print(phases) # Output: ['Environment', 'Python', 'Web', 'AI', 'Agents', 'Bonus']

# --- Checking membership ---
print("Python" in phases) # Output: True - much cleaner than looping through an array in C to check for membership
print("COBOL" in phases) # Output: False

# --- Iterating ---
for phase in phases:
    print(f". Phase: {phase}")  # Output: Phase: Environment
# Output:
#   0: Environment
#   1: Python
#   2: Web
#   3: AI
#   4: Agents

# Enumerate - gives us both the index and the value in the loop
for i, phase in enumerate(phases):
    print(f"  {i}: {phase}")
# Output:
#   0: Environment
#   1: Python
#   2: Web
#   3: AI
#   4: Agents

# =============================================================
# LIST COMPREHENSIONS- read this carefully, it's a powerful and common Python idiom
# =============================================================
# A list comprehension is a concise way to create lists. It consists of brackets containing an expression followed by a 
# for clause, and optionally, one or more if clauses.

# Old way (C-style thinking):
lengths = []
for phase in phases:
    lengths.append(len(phase))
print(f"OLD WAY: {lengths}")

# Python way - list comprehension:
lengths = [len(phase) for phase in phases]
print(f"PYTHON WAY: {lengths}")

# With a filter:
long_phases = [p for p in phases if len(p) >= 6]
print(f"LONG PHASES: {long_phases}") # Output: ['Environment', 'Python', 'Agents'] - only phases with more than 6 characters

# Pattern: [expression for item in iterable if condition]
# Read is left to right: "give me len(phase) for each phase in phases


# =============================================================
# DICTIONARIES (DICTs)
# =============================================================
# A dictionary is a collection of key-value pairs. Dictionaries are unordered, changeable, and do not allow duplicate keys.

# --- Basic dict ---
prospect = {
    "company": "Acme Corp",
    "revenue": 500,
    "employees": 1200,
    "active": True 
}

print(prospect["company"]) # Output: Acme Corp
print(prospect.get("region")) # Output: None - get returns None if the key doesn't exist, instead of raising an error like prospect["region"] would
print(prospect.get("region", "Unknown")) # Output: Unknown - get allows us to specify a default value if the key doesn't exist

# --- Adding and updating ---
prospect["region"] = "Northeast" # Add a new key-value pair
prospect["revenue"] = 550 # Update an existing key-value pair
print(prospect) # Output: {'company': 'Acme Corp', 'revenue': 550, 'employees': 1200, 'active': True, 'region': 'Northeast'}

# --- Checking key membership ---
print("revenue" in prospect) # Output: True
print("headcount" in prospect) # Output: False

# --- Iterating over a dict ---
for key, value in prospect.items():
    print(f"  {key}: {value}")
# Output:
# company: Acme Corp
# revenue: 550
# employees: 1200
# active: True
# region: Northeast

# --- Keys and values separately:
print(f"Keys and values separately:")
print(list(prospect.keys())) # Output: ['company', 'revenue', 'employees', 'active', 'region']
print(list(prospect.values())) # Output: ['Acme Corp', 550, 1200, True, 'Northeast']

# --- Dict comprehension ---
# Build a dict of phase name -> character count
print(f"Building a dict of phase name -> character count")
phase_lengths = {phase: len(phase) for phase in phases}
print(phase_lengths) # Output: {'Environment': 11, 'Python': 6, 'Web': 3, 'AI': 2, 'Agents': 6}


# COMBINING LISTS AND DICTS
# a common pattern is to have a list of dicts, where each dict represents an object with multiple attributes.
# For example, we could have a list of prospects, where each prospect is represented as a dict:

pipeline = [
    {"company": "Acme",    "revenue": 500, "stage": "Proposal"},
    {"company": "Globex",  "revenue": 200, "stage": "Discovery"},
    {"company": "Initech", "revenue": 800, "stage": "Closed Won"},
]

# Filter to deals over $300M
big_deals = [deal for deal in pipeline if deal["revenue"] > 300]
print(f"Big deals: {[d['company'] for d in big_deals]}") # Output: Big deals: ['Acme', 'Initech'] - only the companies with revenue over 300

# Total pipeline value
total = sum(deal["revenue"] for deal in pipeline)
print(f"Total pipeline: ${total}M") # Output: Total pipeline: $1500M - sum up the revenue from all deals in the pipeline

