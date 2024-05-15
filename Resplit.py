"""
Title     : Re.split()
Subdomain : Regex and Parsing
Domain    : Python
Author    : Ahmedur Rahman Shovon
"""

import re

regex_pattern = r"[.,]+"

print("\n".join(re.split(regex_pattern, input())))
