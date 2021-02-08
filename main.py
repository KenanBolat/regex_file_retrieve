import re
import os
import datetime
import pprint
start = datetime.datetime.now()
process_path = "./files"
file_flags = ['N15', 'N18', 'N19', 'M01']
pattern = r"(^[x]{4}_OSV_("+"|".join(file_flags)+")_\d{8})|(^tle_\d{8}.txt)"
files = [row for row in os.listdir(process_path) if re.search(pattern, row)]
pprint.pprint(files)
end = datetime.datetime.now()
