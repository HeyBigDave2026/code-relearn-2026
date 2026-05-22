# lesson05_classes.py
# Phase 2 - Lesson 5: Classes & Objects
# Dave Pruyn, May 2026

# Introduction to classes and objects in Python
# In this lesson, we'll explore the basics of classes and objects in Python. We'll cover how to define classes, create objects, and interact with them.
# We'll also look at how to define methods in classes and how to call them on objects.
# By the end of this lesson, you should have a good understanding of how classes and objects work in Python.
# Let's get started!


# ===============================================
# BASIC CLASS
# ===============================================

class Deal:
    """Represents a sales deal in the pipeline."""

    # Classes variable - shared across ALL instances of the class
    currency = "USD"

    def __init__(self, company, revenue, stage="Discovery"):
        """Constructor - runs when you instantiate the class."""
        # Instance variables - unique to each instance of the class
        self.company = company
        self.revenue = revenue
        self.stage = stage
        self.notes = []           # each deal gets its own empty list for notes

    def advance(self):
        """Move deal to next stage."""
        stages = ["Discovery", "Proposal", "Negotiation", "Closed Won"]
        if self.stage in stages:
            current = stages.index(self.stage)
            if current < len(stages) - 1:
                self.stage = stages[current + 1]
        return self

    def add_note(self, note):
        """Add a note to this deal."""
        self.notes.append(note)
        return self    # Return the deal object so that we can chain methods

    def summary(self):
        """Return a formatted summary string."""
        return f"{self.company} | ${self.revenue}M | {self.stage} | {len(self.notes)} notes"

    def __str__(self):
        """Called when you print() the object - like toString in Java."""
        return self.summary()

    def __repr__(self):
        """Called in the REPL or when object is in a list - developer-facing."""
        return f"Deal('{self.company}', {self.revenue}, '{self.stage}')"


# ===============================================
# INSTANTIATATION & USGE
# ===============================================


# Create instances - __init__ runs each time
acme = Deal("Acme", 500, "Proposal")
globex = Deal("Globex", 200)    # Uses the default stage of "Discovery"

print(acme)        # calls __str__
print(globex)

# Access and mutate instance variables directly
acme.revenue = 550
print(f"Updated revenue: {acme.revenue}")

# Call methods on the objects
print(f"Advanced stage: {acme.stage}")

# Method chaining - each method returns self
globex.add_note("Met with VP Sales").add_note("Strong budget confirmed")
print(f"Notes: {globex.notes}")

# Class variable - shared across ALL instances of the class
print(f"Currency: {acme.currency}")
print(f"Currency: {Deal.currency}")


# ===============================================
# INHERITANCE
# ===============================================

class EnterpriseDeal(Deal):
    """A Deal with enterprise-specific attributes.  Inherits from Deal."""
    
    def __init__(self, company, revenue, stage="Discovery", contract_years=3):
        super().__init__(company, revenue, stage)  # Call the parent class constructor
        self.contract_years = contract_years
        self.legal_review = False

    def summary(self):
        """Override parent summary with enterprise details>"""
        base = super().summary()    # get the parent's summary
        return f"{base} | {self.contract_years}yr contract"

# ===============================================
# PRIVATE BY CONVENTION
# ===============================================

class SalesRep:
    """Demonstrates Python's privacy conventions."""

    def __init__(self, name, quota):    # Private by convention
        self.name = name        # public - use freely
        self._quota = quota     # protected - internal use, don't touch from outside
        self.__ytd = 0          # private - name-mangled by Python

    def close_deal(self, amount):
        self.__ytd += amount

    def attainment(self):
        return f"{self.name}: {round(self.__ytd / self._quota * 100)}% of quota"


# ===============================================
# PUTTING IT TOGETHER
# ===============================================

pipeline = [
    Deal("Acme", 500, "Proposal"),
    Deal("Globex", 200, "Discovery"),
    EnterpriseDeal("Initech", 800, "Negotiation", contract_years=5),
]

for deal in pipeline:
    print(deal)

# List comprehension still works on objects
big_deals = [d for d in pipeline if d.revenue > 300]
print(f"\nBig deals: {[d.company for d in big_deals]}")

# SalesRep example
rep = SalesRep("Dave", 2000)
for deal in pipeline:
    if deal.stage in ("Closed Won", "Negotiation"):
        rep.close_deal(deal.revenue)
print(f"\n{rep.attainment()}")

