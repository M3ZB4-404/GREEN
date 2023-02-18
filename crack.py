import os, sys
try:
    __import__("MEZBA").v()
except Exception as e:
    exit(str(e))
