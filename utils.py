import json
from config import PATH


def load_json_data():
    """This function loads json data using config file"""
    with open(PATH, "r", encoding="utf-8") as fp:
        return json.load(fp)


def build_preformatted_list(candidates):
    """"""
    result_str = ''
    for people in candidates:
        result_str += people["name"] + "\n"
        result_str += people["position"] + "\n"
        result_str += people["skills"] + "\n" + "\n"
    return  "<pre>" + result_str +"</pre>"