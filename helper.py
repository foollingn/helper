import json
import random
import re 

#Json file upload.
def loadjson(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as jsonfile:
            return json.load(jsonfile)
    except Exception:
        return None

#Write to json file
def dumpjson(data, filepath):
    try: 
        with open(filepath, 'r', encoding='utf-8') as jsonfile:
            datas = json.load(jsonfile)
        pop = 0
        for result in datas:
            if result['id'] == data['id']:
                datas[pop] = data
            else: pop=pop+1
        with open(filepath, 'w', encoding='utf-8') as file:
            json.dump(datas, file, indent=4, ensure_ascii=False)
    except Exception:
        return None

#Adding a new dictionary to json.
def push(filepath, data):
    try:
        with open(filepath, encoding='utf-8') as json_file:
            data = json.load(json_file)
        data.append(data)
        with open(filepath, 'w', encoding='utf-8') as outfile:
            json.dump(data, outfile, indent=4, ensure_ascii=False)
    except Exception:
        return None

#Beautiful numbers.
def task(intenger):
    try:
        return re.sub(r'(?<!^)(?=(\d{3})+$)', r'.', f"{intenger}")
    except Exception:
        return None

#Maximum id.
def maxuId(filepath):
    try:
        with open(filepath, encoding='utf-8') as json_file:
            data = json.load(json_file)
            max_item = max(data, key = lambda item: int(item['uid']))
            return int(max_item['uid'])+1
    except Exception:
        return 0

#Random by chance.
def chance(chance, x=bool):
    status = random.choices([True, False], weights=[chance,100-chance], k=1)[0]
    if x is True:
        if status is True: x = [1, 2, 2.5, 5, 10]
        else: x = [0, 0.5, 0.25, 0.75]
        return {"status": status, "bet": random.choice(x)}
    return {"status": status}

#Replace string to intenger.
def replace(text):
    try:
        text = text.replace('к', '000')
        text = text.replace('k', '000')
        return int(text)
    except Exception:
        return 0

#Find to user by id.
def find(object, id, filepath):
    try:
        return list(filter(lambda x: x[object]==id, loadjson(filepath)))[0]
    except Exception:
        return None
