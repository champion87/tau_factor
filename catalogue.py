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

# 0 <= num < 10000
def int_to_code(num, len = 4):
    if not ( 0 < num or num <= 10**len ):
        raise Exception("Int out of range") 
    return str(num).zfill(len)
def main():
    print(get_matches(HEDVA_CODE[:4]))
    
if __name__ == "__main__":
    main()
    