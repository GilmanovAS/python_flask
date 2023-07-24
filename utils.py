"""It is util file"""
import json

from config import PATH


def load_json_data():
    """This function loads json data using config file"""
    with open(PATH, "r", encoding="utf-8") as fp:
        return json.load(fp)


def html_format(candidate):
    str = ''
    str += "<pre>"
    str += candidate["name"] + "\n"
    str += candidate["position"] + "\n"
    str += candidate["skills"] + "\n" + "</pre>" + "\n"
    return str


def build_preformatted_list(candidates):
    """ """
    result_str = ""
    for people in candidates:
        result_str += html_format(people)
    return result_str


def get_candidate_by_id(candidate):
    result_str = f'<img src ="{candidate["picture"]}">\n'
    result_str += html_format(candidate)
    return result_str


def get_candidate_by_skill(candidate):
    return html_format(candidate)

print(__name__)
print(__doc__)