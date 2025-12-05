#!/usr/bin/env python3

class Dog:
    approved_breeds = [
        "Labrador", "Pug", "Dalmatian", "Beagle", "Bulldog",
        "Boxer", "Husky", "Golden Retriever"
    ]

    def __init__(self, name="Fido", breed="Mutt"):
        # Name validation
        if not isinstance(name, str) or not (1 <= len(name) <= 25):
            print("Name must be string between 1 and 25 characters.")
            self.name = None
        else:
            self.name = name

        # Breed validation
        if breed != "Mutt" and breed not in self.approved_breeds:
            print("Breed must be in list of approved breeds.")
            self.breed = None
        else:
            self.breed = breed
