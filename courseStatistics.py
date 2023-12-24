import requests
TAU_FACTOR_SERVER_URL = "https://www.tau-factor.com/api/v1/courses/"
REQUEST_BY_CODE_PARAM = "?course_code="

DEFAULT_FIELDS = ["year", "semester", "statistics"]

CS_PREFIX = "0368"
MATH_PREFIX = "0366"

MIN_QUERY_LEN = 3
MAX_QUERY_LEN = 8


#TODO empty results
#TODO many results

def simplify(course_details: dict, fields=DEFAULT_FIELDS): 
    results = course_details["results"][0]
    instances = results["instances"]
    res = []
    for inst in instances:
        simplified = {k:v for k,v in inst.items() if k in fields}
        res.append(simplified)
    return res

def complete_to_min_query(prefix: str):
    pass

class CourseStatistics:
    def __init__(self, average, histogram):
        pass

def get_course_statistics(prefix="") -> list[CourseStatistics]:
    if len(prefix) < MIN_QUERY_LEN:
        pass
    elif MIN_QUERY_LEN <= len(prefix) < MAX_QUERY_LEN:
        pass
    else:
        raise Exception(f"get_course_statistics() recieved a too long prefix query: {prefix}")

def request(course_code: str) ->dict:
    request_url = TAU_FACTOR_SERVER_URL + REQUEST_BY_CODE_PARAM + course_code
    print(f"requesting from {request_url}:")
    response = requests.get(request_url)
    return response.json()