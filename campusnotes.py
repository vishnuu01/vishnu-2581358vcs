#!/usr/bin/env python3
"""Tiny CampusNotes demo with numbered note output."""
notes = [
    "Review remote repository workflow",
    "Practice feature branches and pull requests",
    "Study Git hooks and release tags",
]

if __name__ == "__main__":
    print("CampusNotes")
    for i, note in enumerate(notes, 1):
        print(f"{i}. {note}")
