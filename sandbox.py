import json
import typing
import requests

TAU_FACTOR_SERVER_URL = "https://www.tau-factor.com/api/v1/courses/"
REQUEST_BY_CODE_PARAM = "?course_code="

HEDVA_CODE = "0366-1101"
    
    
def request(code: str):
    request_url = TAU_FACTOR_SERVER_URL + REQUEST_BY_CODE_PARAM + code
    print(f"requesting from {request_url}:")
    response = requests.get(request_url)
    
    with open(f"{code}.json", "w") as dump_me:
        response_json = response.json()
        json.dump(response_json, dump_me, indent=4)

def main():
    request(HEDVA_CODE)
    
    with open(f"{HEDVA_CODE}.json", encoding = "utf-8") as my_json:
        json_dict = json.load(my_json)
        data = json_dict["results"]    
    
if __name__ == "__main__":
    main()
    
