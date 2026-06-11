import os
from datetime import datetime
from lib.generate_log import generate_log


def assert_true(cond, msg):
    if not cond:
        raise AssertionError(msg)


# Test data
log_data = ["Entry one", "Entry two", "Entry three"]

# Test 1: create file and return filename
filename = generate_log(log_data)
assert_true(os.path.exists(filename), f"{filename} not found.")

# Test 2: filename format
today = datetime.now().strftime("%Y%m%d")
assert_true(filename == f"log_{today}.txt", "Filename does not match expected format.")

# Test 3: content matches
with open(filename, "r", encoding="utf-8") as f:
    lines = [line.strip() for line in f.readlines()]
assert_true(lines == log_data, "Log file contents do not match input data.")

# Cleanup
os.remove(filename)

# Test 4: raises on invalid input
try:
    generate_log("not a list")
    raise AssertionError("Expected ValueError for invalid input")
except ValueError:
    pass

# Test 5: empty list creates empty file
filename = generate_log([])
with open(filename, "r", encoding="utf-8") as f:
    content = f.read()
assert_true(content == "", "Empty list should create empty file")
os.remove(filename)

print("All checks passed (no pytest).")
