"""It is util file"""
from flask import Flask

from utils import load_json_data, build_preformatted_list, get_candidate_by_id, get_candidate_by_skill


#
# # This is a sample Python script.
#
# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.

# # See PyCharm help at https://www.jetbrains.com/help/pycharm/

def run_app():
    """This function starts the flask app"""
    app = Flask(__name__)
    candidates = load_json_data()

    @app.route("/")
    def page_index():
        return build_preformatted_list(candidates)

    @app.route("/candidate/<int:uid>")
    def page_candidate_by_id(uid):
        """test"""
        for human in candidates:
            if human["id"] == uid:
                return get_candidate_by_id(human)

    def page_skill(uid):
        result_test = ''
        for human in candidates:
            if uid.lower() in human["skills"].lower():
                result_test += get_candidate_by_skill(human)
        return result_test

    app.add_url_rule("/skill/<uid>", view_func=page_skill)

    # app.run()
    app.run(host="127.0.0.4", port="5001")

print(__name__)
print(__doc__)

if __name__ == '__main__':
    run_app()
