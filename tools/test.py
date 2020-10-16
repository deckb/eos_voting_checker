from voting_checker import bpjson
import json

with open("/Users/buddy.deck/Documents/b1/dev/bp.json") as bp_file:
    bp_json = json.load(bp_file)
    bp = bpjson.BpJson(bp_json)

    bp.check_github()
    #bp.check_apis(version="v2.0")
    #bp.check_peers()