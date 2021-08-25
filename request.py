#Function: this is a python script that checks to see if coverage reported from the Codecov API is accurate

import requests
import time
import os

payload = {'token': os.environ['API_KEY']}

link = 'https://codecov.io/api/gh/codecov/go-standard'

print("Waiting 60 seconds for report to upload before pinging API...")

# Sleep 60 seconds
time.sleep(60)

print("Pinging Codecov's API..")
# Get latest coverage data
all_data = requests.get(link, params=payload).json()
commit_data = all_data['commits'][0]
coverage_percentage = commit_data['totals']['c']

print("Ensuring coverage percentage is accurate...")
# Result should return 66.66667 as its coverage metric
expected_coverage = os.environ['EXPECTED_COVERAGE']

if(coverage_percentage == expected_coverage): 
    print("Success! Codecov's API returned the correct coverage percentage, "+ expected_coverage)
    exit(0)
else:
    print("Whoops, something is wrong D: Codecov did not return the correct coverage percentage. Coverage percentage should be "+expected_coverage+" but Codecov returned "+coverage_percentage)
    exit(1)
