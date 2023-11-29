import json
import typing
import requests
from sandbox import *
import pickle
import time

MATH_PREFIX = "0366"
CS_PREFIX = "0368"

NAMING_FIELDS = ["course_code", "most_common_names"]
GUESS_LEN = 4


# four digits prefix
def get_matches(prefix: str):
    
    matches = request(prefix)
    if "results" not in matches.keys():
        raise Exception("fuck.")
    
    print(matches)
    
    results = matches["results"]
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

def get_all():
    res = []
    for num in range(10**GUESS_LEN):
        code = int_to_code(num)
        print(code)
        res += (get_matches(code))
        time.sleep(0.001)
    return res

def main():
    get_matches("1")
    # # print(int_to_code(43))
    # # print(get_matches(HEDVA_CODE[:4]))
    # res = get_all()
    # with open("catalogue.txt", "wb") as f:
    #     print(res)
    #     pickle.dump(res, f)  
    
if __name__ == "__main__":
    main()
    