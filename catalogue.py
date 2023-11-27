import json
import typing
import requests
from sandbox import *

NAMING_FIELDS = ["course_code", "most_common_names"]


# four digits prefix
def get_matches(prefix: str):
    results = request(prefix)["results"]
    res = []
    for result in results:
        required_data = {k:v for k,v in result.items() if k in NAMING_FIELDS}
        res.append(required_data)
    return res

def main():
    print(get_matches(HEDVA_CODE[:4]))
    
if __name__ == "__main__":
    main()
    