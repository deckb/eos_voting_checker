from voting_checker import bpjson
import eospy
import requests

ce = eospy.cleos.Cleos(url="https://eos.greymass.com")

reader = ce.get_producers(limit=30)["rows"]

# print(reader)

for bp in reader:

    output = f"{bp['owner']}"
    url = bp["url"]
    try:
        json_url = url + "/bp.json"
        r = requests.get(json_url)
        bp = bpjson.BpJson(r.json())
        github_users = bp.check_github()
        if github_users != "":
            if type(github_users) != str:
                print(",".join(github_users))
            else:    
                print(github_users)
    except Exception as ex:
        output += f"unreachable bp.json"
# bp = bpjson.BpJson(bp_json="/Users/buddy.deck/Documents/b1/dev/bp.json")

# bp.check_apis(version="v2.0")
# bp.check_peers()