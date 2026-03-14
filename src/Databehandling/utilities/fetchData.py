import json


def opneFile(path):
    """_summary_

    Args:
        path (str): Hvor json filen ligger

    Returns:
        dictionere: Ord bok av alt datan
    """

    with open(path , encoding="utf-8") as f:
        data = json.load(f)
        f.close
    return data

def returnData(path):
    """_summary_

    Args:
        path (str): Hvor json filen ligger

    Returns:
        _type_: _description_
    """
    ney = []
    data = opneFile(path)
    for y in range(data["size"][data["id"].index("AntRom")]): 
        data_i = 0
        info = []
        for x in range(data["size"][data["id"].index("Soner2")]):
            info.append([])
            for z in range(data["size"][data["id"].index("Tid")]):
                info[x].append(data["value"][data_i*5+y])
                data_i+=1
        ney.append(info)      

    # for i in ney:
    #     print("")
    #     print(i)
    return ney


def returnAar(path):
    """_summary_

    Args:
        path (str): Hvor json filen ligger

    Returns:
        _type_: _description_
    """

    data = opneFile(path)
    arr = []
    for key in data["dimension"]["Tid"]["category"]["index"]:
        arr.append(int(key))
    # print(arr)
    return arr
        
def returnAntRom(path):
    """_summary_

    Args:
        path (str): Hvor json filen ligger

    Returns:
        _type_: _description_
    """
    data = opneFile(path)
    arr = []
    for key in data["dimension"]["AntRom"]["category"]["index"]:
        arr.append(data["dimension"]["AntRom"]["category"]["label"][key])
    # print(arr)
    return arr

def returnSoner(path):
    """_summary_

    Args:
        path (str): Hvor json filen ligger

    Returns:
        _type_: _description_
    """
    data = opneFile(path)
    arr = []
    for i in range(data["size"][data["id"].index("Soner2")]):
        arr.append(0)

    for key in data["dimension"]["Soner2"]["category"]["index"]:
        arr[data["dimension"]["Soner2"]["category"]["index"][key]] = data["dimension"]["Soner2"]["category"]["label"][key]
    # print(arr)
    return arr
    
# returnSoner("data/leieMonde.json")



  
