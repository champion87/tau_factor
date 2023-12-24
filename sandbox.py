import json
import typing
from courseStatistics import request, simplify

HEDVA_CODE = "0366-1101"
ANOTHER_HEDVA_CODE = "03661101"



    
def request_and_save(code: str) -> None:    
    with open(f"{code}.json", "w") as dump_me:
        json.dump(request(code), dump_me, indent=4)

def save_json(file_name, the_json):
    with open(file_name, "w") as dump_me:
        json.dump(the_json, dump_me, indent=4)

def main():
    hedva = request(HEDVA_CODE)
    # hedva_simp = simplify(hedva)
    
    another_hedva = request(ANOTHER_HEDVA_CODE)
    # another_hedva_simp = simplify(another_hedva)
    
    print(hedva)
    print("\n\n\n\n\n\n\n\n\n")
    print(another_hedva)
    
    
    

    

if __name__ == "__main__":
    main()
    
