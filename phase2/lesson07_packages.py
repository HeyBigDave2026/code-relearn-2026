# lesson07_packages.py
# Phase 2 - Lesson 7: pip & Packages
# Dave Pruyn, May 2026

import json
from rich.console import Console
from rich.table import Table
from rich import print as rprint


# ================================================================================
# RICH - better terminal output
# ================================================================================  

console = Console()

# Rich print - supports markup
rprint("[bold green]Packages are working![/bold green]")
rprint("[bold blue]Phase 2 - Lesson 7[/bold blue]")
# --- Rich Table ---
pipeline = [
    {"company": "Acme",     "revenue": 500, "stage": "Proposal"},
    {"company": "Globex",   "revenue": 200, "stage": "Discovery"},
    {"company": "Initech",  "revenue": 800, "stage": "Closed Won"},
    {"company": "Umbrella", "revenue": 150, "stage": "Closed Lost"},
]

table = Table(title="Sales Pipeline")
table.add_column("Company",  style="cyan",   no_wrap=True)
table.add_column("Revenue",  style="green",  justify="right")
table.add_column("Stage",    style="magenta")

for deal in pipeline:
    table.add_row(
        deal["company"],
        f"${deal['revenue']}M",
        deal['stage']
    )

console.print(table)

# --- Rich for status messages ---
console.print(f"\n[bold]Pipeline Summary[/bold]")
total = sum(d["revenue"] for d in pipeline)
active = [d for d in pipeline if d["stage"] not in ("Closed Won", "Closed Lost")]

console.print(f"  Total deals: [cyan]{len(pipeline)}[/cyan]")
console.print(f"  Active deals: [cyan]{len(active)}[/cyan]")
console.print(f"  Total value: [green]${total}M[/green]")
console.print(f"  Active value: [green]${sum(d['revenue'] for d in active)}M[/green]")
