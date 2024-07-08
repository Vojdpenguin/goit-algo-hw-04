import json

def get_cats_info(path):
    list = []
    try:
        with open(path, "r", encoding="UTF-8") as file:
            cats_info = [el.strip() for el in file.readlines()]

            cats_info_list = [elem.split(",") for elem in cats_info]

            for id, name, age in cats_info_list:
                cats_info_dict = {}
                cats_info_dict["id"] = id
                cats_info_dict["name"] = name
                cats_info_dict["age"] = age
                list.append(cats_info_dict)

    except FileNotFoundError:
        print("File not found or the file was corrupted")

    formated_list = json.dumps(list, indent=0)
    return formated_list

print(get_cats_info("cats_info.txt"))