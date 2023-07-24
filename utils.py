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
    return "<pre>" + result_str + "</pre>"


def build_preformatted_list(candidates):
    """"""
    result_str = ''
    for people in candidates:
        result_str += people["name"] + "\n"
        result_str += people["position"] + "\n"
        result_str += people["skills"] + "\n" + "\n"
    return "<pre>" + result_str + "</pre>"


def get_candidate_by_id(candidate):
    result_str = f'<img src ="{candidate["picture"]}">\n'
    result_str += "<pre>"
    result_str += candidate["name"] + "\n"
    result_str += candidate["position"] + "\n"
    result_str += candidate["skills"] + "\n" + "\n"
    return result_str + "</pre>"
