import requests
TAU_FACTOR_SERVER_URL = "https://www.tau-factor.com/api/v1/courses/"
REQUEST_BY_CODE_PARAM = "?course_code="

DEFAULT_FIELDS = ["year", "semester", "statistics"]

CS_PREFIX = "0368"
MATH_PREFIX = "0366"

DASH_INDEX_COURSE_CODE_FORMAT = 4

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

def format_query(code: str) -> str:
    if not code.isdecimal():                      #code is invalid
        raise Exception(f"The code {code} was given to format_query, but it's bad. Expected decimal code (or at least already-formated code)")
    elif len(code) <= DASH_INDEX_COURSE_CODE_FORMAT:  #code is too short
        return code
    elif code[DASH_INDEX_COURSE_CODE_FORMAT] == '-':#code is already formated
        return code
    else:
        prefix = code[:DASH_INDEX_COURSE_CODE_FORMAT]
        suffix = code[DASH_INDEX_COURSE_CODE_FORMAT:]
        return prefix + "-" + suffix
    
#bases is a list!!!
def append_all_digits_rec(digits: list[str], bases: list[str], times: int) -> list[str]:
    if times < 0:
        raise Exception(f"Bad value of 'times' in add_all_digits_rec: {times}")
    elif times == 0:
        return bases
    else:
        variations = [base + digit for digit in digits for base in bases]
        return append_all_digits_rec(digits, variations, times - 1)  

def complete_to_min_query(prefix: str) -> list[str]:
    DIGITS = ['0','1','2','3','4','5','6','7','8','9']
    
    if not prefix.isdecimal():
        raise Exception(f"The prefix {prefix} was given to complete_to_min_query, but it's bad. Expected decimal prefix (or at least already-formated code)")
    elif len(prefix) > MAX_QUERY_LEN:
        return []
    elif len(prefix) >= MIN_QUERY_LEN:
        return [prefix]
    else:
        missing_digits = MIN_QUERY_LEN - len(prefix)
        return append_all_digits_rec(DIGITS, [prefix], missing_digits)

class SemesterStatistics:
    def __init__(self, year: int, semester: str, mean, median, standard_deviation):
        self.year = year
        self.semester = semester
        self.mean = mean
        self.median = median
        self.standard_deviation = standard_deviation

class CourseStatistics:
    def __init__(self, code: str, name: str, semesters: list[SemesterStatistics]):
        self.code = code
        self.name = name
        self.semesters = semesters
    
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