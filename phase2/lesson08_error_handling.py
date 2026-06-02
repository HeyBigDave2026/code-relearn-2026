# lesson08_error_handling.py
# Phase 2 - Lesson 8: Error Handling
# Dave Pruyn, May 2026

import json
import os
from rich.console import Console

console = Console()


# ================================================================================
# Error handling with try/except blocks
# ================================================================================ 

# Without error handling - this crashes
# result = 10 / 0    # ZeroDivisionError

# With error handling
try:
    result = 10/0
except ZeroDivisionError:
    print("Can't divide by zero")

# --- Catching multiple exception types
def parse_revenue(value):
    """Convert a string to a revnue integer, safetly."""
    try:
        return int(value)
    except ValueError:
        print(f"  '{value}' is not a valid number")
        return 0
    except TypeError:
        print(f"  Got None instead of a string")
        return 0

print(parse_revenue("500"))   # works
print(parse_revenue("abc"))   # ValueError
print(parse_revenue(None))    # TypeError


# ================================================================================
# ELSE AND FINALLY
# ================================================================================

# else: runs if NO exception was raised
# finally: runs ALWAYS - cleanup code goes here

def load_json_file(path):
    """Load a JSON file safely."""
    try:
        with open(path, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        console.print(f"[red]File not found: {path}[/red]")
        return None
    except json.JSONDecodeError as e:
        console.print(f"[red]Invalid JSON in {path}: {e}[/red]")
        return None
    else:
        console.print(f"[green]Loaded {path} successfully[/green]")
        return data
    finally:
        console.print(f"[dim]Attempted to load: {path}[/dim]")
    
# Test it
data = load_json_file("output/pipeline.json")     # exists so should work
data = load_json_file("output/nonexistent.json")   # does not exist so "File not found"(in RED no less!)
    
# ================================================================================
# RAISING EXCEPTIONS
# ================================================================================

def create_deal(company, revenue):
    """Create a deal dict with validation"""
    if not company:
        raise ValueError("Company name cannot be empty")
    if revenue < 0:
        raise ValueError(f"Revenue cannot be negative: {revenue}")
    if not isinstance(revenue, (int, float)):
        raise TypeError(f"Revenue must be a number, got {type(revenue)}")
    return {"company": company, "revenue": revenue, "stage": "Discovery"}

# Test validation
try:
    deal = create_deal("", 500)
except ValueError as e:
    console.print(f"[red]Validation error: {e}[/red]")
    
try:
    deal = create_deal("Acme", -100)
except ValueError as e:
    console.print(f"[red]Validation error: {e}[/red]")
    
try:
    deal = create_deal("Acme", 500)
    console.print(f"[green]Create deal: {deal}[/green]")
except ValueError as e:
    console.print(f"[red]Validation error: {e}[/red]")
    

# ================================================================================ 
# CUSTOM EXCEPTIONS
# ===============================================================================

class PipelineError(Exception):
    """Base exception for pipeline operations."""
    pass

class DuplicateDealError(PipelineError):
    """Raised when a deal already exists in the pipeline."""
    def __init__(self, company):
        self.company = company
        super().__init__(f"Deal already existst for: {company}")

class InvalidStageError(PipelineError):
    """Raised when an invalid stage is specified for a deal."""
    pass


class Pipeline:
    """A sales pipline with validation."""
    
    VALID_STAGES = ["Discovery", "Proposal", "Negotiation", "Closed Won", "Closed Lost"]

    def __init__(self):
        self.deals = []

    def add_deal(self, company, revenue, stage="Discovery"):
        # Check for duplicate
        if any(d["company"] == company for d in self.deals):
            raise DuplicateDealError(company)
        # Validate the stage
        if stage not in self.VALID_STAGES:
            raise InvalidStageError(f"{stage} is not valid.  Use: {self.VALID_STAGES}")
        self.deals.append({"company": company, "revenue": revenue, "stage": stage})
        return self

    def total_value(self):
        return sum(d["revenue"] for d in self.deals)


# Test the pipeline
pipeline = Pipeline()

try:
    pipeline.add_deal("Acme", 500, "Proposal")
    pipeline.add_deal("Globex", 200)
    pipeline.add_deal("Acme", 300)   # Duplicate deal - should raise DuplicateDealError
except DuplicateDealError as e:
    console.print(f"[red]Duplicate: {e}[/red]")
except InvalidStageError as e:
    console.print(f"[red]Bad stage: {e}[/red]")

try:
    pipeline.add_deal("Initech", 800, "Verbal Commit")   # Invalid stage - should raise InvalidStageError
except DuplicateDealError as e:
    console.print(f"[red]Duplicate: {e}[/red]")
except InvalidStageError as e:
    console.print(f"[red]Bad stage: {e}[/red]")

console.print(f"\n[bold]Pipeline has {len(pipeline.deals)} deals worth ${pipeline.total_value()}M[/bold]")
