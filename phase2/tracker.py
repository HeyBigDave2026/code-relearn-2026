# tracker.py
# Phase 2 - Milestone Project
# Dave Pruyn, May 2026

import json
import argparse
from datetime import date
from rich.console import Console
from rich.table import Table
from rich import print as rprint
# from rich.progress import Progress, BarColumn, TextColumn     # not used

console = Console()


# ================================================================================
# DATA STRUCTURES
# ================================================================================

course = {
    "title": "Dave's Coding Re-Learn Bootcamp",
    "description": "A comprehensive course to re-learn coding after long break.",
    "phases": {
        "phase1": {
            "name": "Environment & Mindset Reset",
            "description": "Your dev command center",
            "lessons": [
                {"title": "VS Code Setup", "completed": False, "completed_date": None},
                {"title": "Git Install", "completed": False, "completed_date": None},
                {"title": "GitHub Account", "completed": False, "completed_date": None},
                {"title": "Terminal Basics", "completed": False, "completed_date": None},
                {"title": "Python Install", "completed": False, "completed_date": None},
                {"title": "First Commit & Push", "completed": False, "completed_date": None},
                {"title": "Claude Project Setup", "completed": False, "completed_date": None}
            ],
            "milestone_project": "Your first repo on GitHub with a README. You understand the edit → stage → commit → push cycle cold."
        },
        "phase2": {
            "name": "Python Fundamentals — Your New C",
            "description": "Reactivating your CS brain",
            "lessons": [
                {"title": "Variables & Types", "completed": False, "completed_date": None},
                {"title": "Functions", "completed": False, "completed_date": None},
                {"title": "Lists & Dicts", "completed": False, "completed_date": None},
                {"title": "Loops & Conditionals", "completed": False, "completed_date": None},
                {"title": "Classes & Objects", "completed": False, "completed_date": None},
                {"title": "File I/O", "completed": False, "completed_date": None},
                {"title": "pip & packages", "completed": False, "completed_date": None},
                {"title": "Error Handling", "completed": False, "completed_date": None}
            ],
            "milestone_project": "A working CLI progress tracker for this learning journey — your first real utility, written by you."
        },
        "phase3": {
            "name": "The Web Layer — HTML, CSS & APIs",
            "description": "Making things people can see",
            "lessons": [
                {"title": "HTML Structure", "completed": False, "completed_date": None},
                {"title": "CSS Basics", "completed": False, "completed_date": None},
                {"title": "HTTP & Rest Concepts", "completed": False, "completed_date": None},
                {"title": "Python Requests Lib", "completed": False, "completed_date": None},
                {"title": "JSON Fluency", "completed": False, "completed_date": None},
                {"title": "Flask Mini-app", "completed": False, "completed_date": None},
                {"title": "Calling Public APIs", "completed": False, "completed_date": None}
            ],
            "milestone_project": "A simple web page that fetches and displays live data from a real API — deployed and shareable via URL."
        },
        "phase4": {
            "name": "AI Integration & the Claude API",
            "description": "Where sales experience becomes a superpower",
            "lessons": [
                {"title": "Anthropic Python SDK", "completed": False, "completed_date": None},
                {"title": "Prompt Engineering", "completed": False, "completed_date": None},
                {"title": "System Prompts", "completed": False, "completed_date": None},
                {"title": "Multi-turn Conversations", "completed": False, "completed_date": None},
                {"title": "Tool Use / Function Calling", "completed": False, "completed_date": None},
                {"title": "Streaming Responses", "completed": False, "completed_date": None}
            ],
            "milestone_project": "A custom AI-powered sales tool — prospect research assistant, call prep bot, or meeting summarizer."
        },
        "phase5": {
            "name": "Claude Code, Agents & the Full Stack",
            "description": "The sausage factory, fully visible",
            "lessons": [
                {"title": "Claude Code CLI", "completed": False, "completed_date": None},
                {"title": "Agent workflows", "completed": False, "completed_date": None},
                {"title": "MCP Servers", "completed": False, "completed_date": None},
                {"title": "Multi-agent Patterns", "completed": False, "completed_date": None},
                {"title": "Git Branching & PRs", "completed": False, "completed_date": None},
                {"title": "Deploy to Cloud", "completed": False, "completed_date": None}
            ],
            "milestone_project": "An agent that automates a real sales workflow end-to-end: research → draft outreach → log to CRM."
        }
    }
}


# ================================================================================
# FILE I/O FUNCTIONS
# ================================================================================

def load_data(filepath):
    """Loads tracker data from JSON file.  Returns default course structure if file does not exist."""

    import copy
    default_course = copy.deepcopy(course)

    try:
        with open(filepath, "r") as f:
            file_course_data = json.load(f)
    except FileNotFoundError:
        return default_course
    else:
        return file_course_data

def save_data(filepath, course_data):
    """Saves tracker data to JSON file."""

    try:
        with open(filepath, "w") as f:
            json.dump(course_data, f, indent=2)
    except IOError as e:
        print(f"Error saving data: {e}")


# ================================================================================
# TRACKER CLASS - Represents the tracker
# 3 methods: complete_lesson; uncomplete_lesson & get progress
# ================================================================================

class Course:
    """Represents a course"""

    def __init__(self, filepath):
        self.filepath = filepath
        self.data = load_data(filepath)      # this is the course dict

    def complete_lesson(self, target_title):
        """Mark a specific lesson COMPLETE"""

        today = date.today()
        for phase_key, phase_data in self.data["phases"].items():
            for lesson in phase_data["lessons"]:
                if lesson["title"].lower() == target_title.lower():
                    lesson["completed"] = True
                    lesson["completed_date"] = today.strftime("%m/%d/%Y")
                    save_data(self.filepath, self.data)
                    return True  # exits the entire method cleanly
        # if we get to here (did not return earlier above), lesson was not matched, so need to tell user)
        # print(f"Lesson not found: {target_title}")
        return False    # not found

    def uncomplete_lesson(self, target_title):
        """Mark a specific lesson UNCOMPLETE"""

        today = date.today()
        for phase_key, phase_data in self.data["phases"].items():
            for lesson in phase_data["lessons"]:
                if lesson["title"].lower() == target_title.lower():
                    lesson["completed"] = False
                    lesson["completed_date"] = None
                    save_data(self.filepath, self.data)
                    return True # exit method cleanly like complete_lesson() above
        # if we get to here (did not return earlier above), lesson was not matched, so need to tell user)
        # print(f"Lesson not found: {target_title}")
        return False    # not found
        
#    LEAVING IN FOR MY LEARNING PURPOSES + I was mistaken about this approach.  Claude "teacher st me straight
# 
# def get_progress(self):
#        """Provide summary of course progress"""
#
#       # get_progress() returns course_stats - a dict of total lessons and completed counts for each phase
#        course_stats = [
#            {"phase": "phase1", "total_lessons": 0, "lessons_completed": 0},
#            {"phase": "phase2", "total_lessons": 0, "lessons_completed": 0},
#            {"phase": "phase3", "total_lessons": 0, "lessons_completed": 0},
#            {"phase": "phase4", "total_lessons": 0, "lessons_completed": 0},
#            {"phase": "phase5", "total_lessons": 0, "lessons_completed": 0},   
#        ]
#
#        for phase_key, phase_data in self.data["phases"].items():
#            for lesson in phase_data["lessons"]:
#                course_stats.phase["phase_key"].total_lessons =+ 1
#                if lesson["completed"]:
#                    course_stats.phase["phase_key"].lessons_completed += 1
#                    break   # done - get out
#        return course_stats
#        save_data(self.filepath, self.data)     # would not execute since return exits first - duh!  :-)))).  Also, this method should not save since readonly data use

    def get_progress(self):
        """Provide summary of course progress -- Return progress stats per phase and overall."""

        # THIS is what I wanted to get to when I was working on this!!!!!

        stats = {}
        for phase_key, phase_data in self.data["phases"].items():
            total = len(phase_data["lessons"])
            completed = sum(1 for l in phase_data["lessons"] if l["completed"])
            stats[phase_key] = {
                "name": phase_data["name"],
                "total": total,
                "completed": completed
            }
        return stats


# ================================================================================
# DISPLAY FUNCTIONS - Provided by Claude "teacher"
# ================================================================================

def display_full(course):
    """Display all phases and lessons in a rich table."""

    stats = course.get_progress()
    # What will happen if file is not found - default course is returned

    for phase_key, phase_stat in stats.items():
        phase_data = course.data["phases"][phase_key]

        # Phase header table
        table = Table(
            title=f"{phase_stat['name']}  —  {phase_stat['completed']}/{phase_stat['total']} lessons",
            show_header=True,
            header_style="bold cyan"
        )
        table.add_column("Lesson", style="white", min_width=30)
        table.add_column("Status", justify="center", min_width=12)
        table.add_column("Completed", justify="center", min_width=14)

        for lesson in phase_data["lessons"]:
            if lesson["completed"]:
                status = "[green]✓ Done[/green]"
                date_str = lesson.get("completed_date") or "[dim]—[/dim]"
                title_str = f"[green]{lesson['title']}[/green]"
            else:
                status = "[dim]○ Pending[/dim]"
                date_str = "[dim]—[/dim]"
                title_str = f"[dim]{lesson['title']}[/dim]"

            table.add_row(title_str, status, date_str)

        console.print(table)
        console.print()

def display_phase(course, phase_num):
    """Display a single phase by number (1-5)."""

    phase_key = f"phase{phase_num}"
    if phase_key not in course.data["phases"]:
        console.print(f"[red]Phase {phase_num} not found. Use 1-5.[/red]")
        return

    # Reuse display_full logic for just this phase
    phase_data = course.data["phases"][phase_key]
    stats = course.get_progress()
    phase_stat = stats[phase_key]

    table = Table(
        title=f"{phase_stat['name']}  —  {phase_stat['completed']}/{phase_stat['total']} lessons",
        show_header=True,
        header_style="bold cyan"
    )
    table.add_column("Lesson", style="white", min_width=30)
    table.add_column("Status", justify="center", min_width=12)
    table.add_column("Completed", justify="center", min_width=14)

    for lesson in phase_data["lessons"]:
        if lesson["completed"]:
            status = "[green]✓ Done[/green]"
            date_str = lesson.get("completed_date") or "[dim]—[/dim]"
            title_str = f"[green]{lesson['title']}[/green]"
        else:
            status = "[dim]○ Pending[/dim]"
            date_str = "[dim]—[/dim]"
            title_str = f"[dim]{lesson['title']}[/dim]"

        table.add_row(title_str, status, date_str)

    console.print(table)
    # Milestone
    console.print(f"\n[bold cyan]Milestone:[/bold cyan] {phase_data['milestone_project']}\n")

def display_summary(course):
    """Display one-line progress bar per phase plus overall."""

    stats = course.get_progress()

    console.print("\n[bold white]── Course Progress ──[/bold white]\n")

    total_lessons = 0
    total_completed = 0

    for phase_key, stat in stats.items():
        total_lessons += stat["total"]
        total_completed += stat["completed"]

        pct = int((stat["completed"] / stat["total"]) * 100) if stat["total"] else 0
        bar_filled = int(pct / 5)        # 20 chars wide
        bar_empty = 20 - bar_filled
        bar = f"[green]{'█' * bar_filled}[/green][dim]{'░' * bar_empty}[/dim]"

        console.print(f"  [cyan]{phase_key}[/cyan]  {bar}  [white]{stat['completed']}/{stat['total']}[/white]  [dim]{pct}%[/dim]  [dim]{stat['name']}[/dim]")

    # Overall
    overall_pct = int((total_completed / total_lessons) * 100) if total_lessons else 0
    bar_filled = int(overall_pct / 5)
    bar_empty = 20 - bar_filled
    bar = f"[green]{'█' * bar_filled}[/green][dim]{'░' * bar_empty}[/dim]"

    console.print(f"\n  [bold]Overall[/bold]  {bar}  [white]{total_completed}/{total_lessons}[/white]  [bold green]{overall_pct}%[/bold green]\n")


# ================================================================================
# ARGPARSE WIRING - this parses arguments for CLI's - good example of the "how" to argparse
# ================================================================================

def build_parser():
    """Build and return the argument parser."""

    parser = argparse.ArgumentParser(
        prog="tracker",
        description="Dave's Coding Re-Learn Progress Tracker"
    )

    # Subcommands - each becomes a separate command (show, complete, etc.)
    subparsers = parser.add_subparsers(dest="command")

    # --- show ---
    show_parser = subparsers.add_parser("show", help="Display lessons and progress")
    show_parser.add_argument(
        "--phase",
        type=int,
        choices=[1, 2, 3, 4, 5],
        help="Show a specific phase only (1-5)"
    )

    # --- complete ---
    complete_parser = subparsers.add_parser("complete", help="Mark a lesson complete")
    complete_parser.add_argument(
        "title",
        type=str,
        help="Lesson title to mark incomplete"
    )

    # --- uncomplete ---
    uncomplete_parser = subparsers.add_parser("uncomplete", help="Mark a lesson incomplete")
    uncomplete_parser.add_argument(
        "title",
        type=str,
        help="Lesson title to mark incomplete"
    )

    # --- summary ---
    subparsers.add_parser("summary", help="Show phase-by-hase progress summary")

    return parser


# ================================================================================
# MAIN ENTRY POINT
# ================================================================================

DATA_FILE = "tracker_data.json"

def main():
    """Main entry point - parge args and displathc to the correct function."""

    parser = build_parser()
    args = parser.parse_args()

    # Load the crouse
    course = Course(DATA_FILE)

    # Dispatch based on command
    if args.command == "show":
        if args.phase:
            display_phase(course, args.phase)
        else:
            display_full(course)

    elif args.command == "complete":
        if course.complete_lesson(args.title):
            console.print(f"[green]✓ Marked complete: {args.title}[/green]")
        else:
            console.print(f"[red]Lesson not found: {args.title}[/red]")
        
    elif args.command == "uncomplete":
        if course.uncomplete_lesson(args.title):
            console.print(f"[yellow]○ Marked incomplete: {args.title}[/yellow]")
        else:
            console.print(f"[red]Lesson not found: {args.title}[/red]")

    elif args.command == "summary":
        display_summary(course)
        console.print("[dim]Run 'python3 tracker.py --help' for available commands.[/dim]")

if __name__ == "__main__":
    main()
