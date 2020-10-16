from voting_checker import bpjson
import csv
import requests

with open("/Users/buddy.deck/Documents/b1/dev/Voting List - Sheet1.csv") as csvfile:
    with open("/Users/buddy.deck/Documents/b1/dev/Voting List - Sheet1_results.csv", "w") as outfile:
        writer = csv.writer(outfile, delimiter=",")
        reader = csv.reader(csvfile, delimiter=",")
        for row in reader:
            if row[2] and 'http' in row[2]:
                print(row)
                try:
                    r = requests.get(row[2])
                    bp = bpjson.BpJson(r.json())
                    valid_apis = ""
                    valid_peers = ""
                    if bp.check_apis(version="v2.0"):
                        row[3] = "X"
                        row[4] = "X"
                    if bp.check_peers():
                        row[3] = "X"                
                except Exception as ex:
                    print(f'Unreachable bp json: {ex}')
                    row[6] = f'{ex}'
            writer.writerow(row)


# bp = bpjson.BpJson(bp_json="/Users/buddy.deck/Documents/b1/dev/bp.json")

# bp.check_apis(version="v2.0")
# bp.check_peers()