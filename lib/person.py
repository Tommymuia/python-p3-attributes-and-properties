#!/usr/bin/env python3

class Person:
    approved_jobs = [
        "Sales", "ITC", "Marketing", "HR", "Engineering", "Finance"
    ]

    def __init__(self, name="John Doe", job="Sales"):
        # Name validation
        if not isinstance(name, str) or not (1 <= len(name) <= 25):
            print("Name must be string between 1 and 25 characters.")
            self.name = None
        else:
            # Save name in title case
            self.name = name.title()

        # Job validation
        if job not in self.approved_jobs:
            print("Job must be in list of approved jobs.")
            self.job = None
        else:
            self.job = job
