from colorama import Fore, Back, Style
import colorama
import json
import random
import re 


colorama.init(autoreset=True)

class DebHel(object):
    debug = True

#Debug to successfully.
def debugMode(text):
    if DebHel.debug: print(f"{Fore.YELLOW}DEBUG HELPER | {Fore.MAGENTA}{text}")

#Debug to Error.
def debugModeErr(text):
    if DebHel.debug: print(f"{Fore.RED}DEBUG HELPER | {Fore.MAGENTA}{text}")

#Loading to json file.
def loadjson(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as jsonfile:
            debugMode(f"(loadjson): Loading to Json File '{filepath}")
            return json.load(jsonfile)
    except Exception as e: debugModeErr(f"(loadjson): Errored ' {e} '"); return None

#Write to json file.
def dumpjson(data, filepath):
    try: 
        datas = loadjson(filepath)
        pop = 0
        for result in datas:
            if result['id'] == data['id']:
                datas[pop] = data
            else: pop=pop+1
        with open(filepath, 'w', encoding='utf-8') as file:
            json.dump(datas, file, indent=4, ensure_ascii=False)
            debugMode(f"(dumpjson): Successfully dumping data '{datas}'")
    except Exception as e: debugModeErr(f"(dumpjson): Errored ' {e} '"); return None

#Adding a new dictionary to json.
def push(filepath, data):
    try:
        json_data = loadjson(filepath)
        json_data.append(data)
        with open(filepath, 'w', encoding='utf-8') as outfile:
            json.dump(json_data, outfile, indent=4, ensure_ascii=False)
            debugMode(f"(push): Successfully pushing in {filepath} by data '{json_data}'")
    except Exception as e: debugModeErr(f"(push): Errored ' {e} '"); return None

#Delete to json file.
def delete(filepath, id):
    try:
        data = loadjson(filepath)
        minimal = 0
        for person in data:
            if person["id"] == id:
                data.pop(minimal)
            else:
                minimal = minimal + 1
        with open(filepath, 'w', encoding='utf-8') as outfile:
            json.dump(data, outfile, ensure_ascii=False, indent=4)
            debugMode(f"(delete): Successfully deleted user with ID is {id}")
            return True
    except Exception as e: debugModeErr(f"(delete): Errored ' {e} '"); return None
        
#Beautiful numbers.
def task(intenger):
    try:
        debugMode("(task): Successfully tasked")
        return re.sub(r'(?<!^)(?=(\d{3})+$)', r'.', f"{intenger}")
    except Exception as e: debugModeErr(f"(task): Errored ' {e} '"); return None

#Maximum id.
def maxuId(filepath):
    try:
        data = loadjson(filepath)
        max_item = max(data, key = lambda item: int(item['uid']))
        debugMode("(maxuId): Successfully found the last number")
        return int(max_item['uid'])+1
    except Exception as e: debugModeErr(f"(maxuId): Errored ' {e} '"); return 0

#Random by chance.
def chance(chance, x=bool):
    status = random.choices([True, False], weights=[chance,100-chance], k=1)[0]
    if x is True:
        if status is True: x = [1, 2, 2.5, 5, 10]
        else: x = [0, 0.5, 0.25, 0.75]
        totalx = random.choice(x)
        debugMode(f"(chance): Total is {status}, ({totalx}x)")
        return {"status": status, "bet": totalx}
    return {"status": status}

#Replace string to intenger.
def replace(string):
    try:
        text = string.replace('к', '000')
        text = text.replace('k', '000')
        debugMode(f"(replace): Befor is {string}, After is {int(text)}")
        return int(text)
    except Exception as e: debugModeErr(f"(replace): Errored ' {e} '"); return 0

#Find to user by id.
def find(object, id, filepath):
    try: return list(filter(lambda x: x[object]==id, loadjson(filepath)))[0]
    except Exception as e: return None