import json
import typing
import requests

TAU_FACTOR_SERVER_URL = "https://www.tau-factor.com/api/v1/courses/"
REQUEST_BY_CODE_PARAM = "?course_code="

DEFAULT_FIELDS = ["year", "semester", "statistics"]

HEDVA_CODE = "0366-1101"
def request(course_code: str) ->dict:
    request_url = TAU_FACTOR_SERVER_URL + REQUEST_BY_CODE_PARAM + course_code
    print(f"requesting from {request_url}:")
    response = requests.get(request_url)
    return response.json()
    
def request_and_save(code: str) -> None:    
    with open(f"{code}.json", "w") as dump_me:
        json.dump(request(code), dump_me, indent=4)

def save_json(file_name, the_json):
    with open(file_name, "w") as dump_me:
        json.dump(the_json, dump_me, indent=4)

def main():
    hedva = request(HEDVA_CODE)
    hedva_simp = simplify(hedva)
    with open(f"hedva_simp.json", "w") as dump_me:
        json.dump(hedva_simp, dump_me, indent=4)
    
    
    
def simplify(course_details: dict, fields=DEFAULT_FIELDS):
    results = course_details["results"][0]
    instances = results["instances"]
    res = []
    for inst in instances:
        simplified = {k:v for k,v in inst.items() if k in fields}
        res.append(simplified)
    return res
    

if __name__ == "__main__":
    main()
    
