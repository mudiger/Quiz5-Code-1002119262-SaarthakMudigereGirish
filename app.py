from flask import request
from flask import Flask
from flask import render_template
import os
import regex as re

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/page2/", methods=['GET', 'POST'])
def page2():
    count_list = []
    full_text = ''
    texts = ''
    if request.method == "POST":
        text = request.form['text']

        # initializing tag
        tag = ["b","i","h1","p"]
        texts=[]
        for i in tag:
            # regex to extract required strings
            reg_str = "<" + i + ">(.*?)</" + i + ">"
            texts.append(re.findall(reg_str, text))

        clean = re.compile('<.*?>')
        full_text = re.sub(clean, '', text)
        re.findall(r'<b>.*(\[|\]).*</b>', text)

    return render_template("2)Page.html", full_text=full_text, texts=texts)


if __name__ == "__main__":
    app.run(debug=True)

