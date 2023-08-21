"""
ProgrammingLanguage
Estimate: 40 minutes
Actual:   45 minutes
"""


class ProgrammingLanguage:
    def __init__(self, name, typing, reflection, year):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        reflection_str = "Reflection: true" if self.reflection else "Reflection: false"
        return f"{self.name}, Typing: {self.typing} , {reflection_str}, Year: {self.year}"

    def is_dynamic(self):
        return self.typing == "Dynamic"
