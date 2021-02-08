import re
import os
import datetime
import pprint

# Initiation Time
start = datetime.datetime.now()

# Define process path
process_path = "./files"

# Add/update file flags
# file_flags = ['N15', 'N18', 'N19', 'M01']

# Define pattern
# pattern = r"(^[x]{4}_OSV_(" + "|".join(file_flags) + ")_\d{8})|(^tle_\d{8}.txt)"
pattern = r"(^[x]{4}_OSV_(N15|N18|N19|M01)_\d{8})|(^tle_\d{8}.txt)"


# apply filtering
files = [row for row in os.listdir(process_path) if re.search(pattern, row)]

pprint.pprint(files)
# Script run time
end = datetime.datetime.now()
print("Initiation time:", str(start), " Duration:", str(end - start))
