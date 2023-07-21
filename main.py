from flask import Flask
from utils import load_json_data, build_preformatted_list


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
    print(candidates)
    str1 = build_preformatted_list(candidates)
    print(str1)

    @app.route("/")
    def page_index():
        # print(candidates)
        # str1 = build_preformatted_list(candidates)
        # print(str1)
        return str1

    @app.route("/catalog/<uid>")
    def page_catalog(uid):
        """test"""
        # return f"I'm catalog page {uid}"
        return page_catalog.__doc__

    def page_user(uid):
        return f"I am user page{uid}"

    app.add_url_rule("/user/<uid>", view_func=page_user)

    # app.run()
    app.run(host="127.0.0.5", port="5001")


if __name__ == '__main__':
    run_app()
