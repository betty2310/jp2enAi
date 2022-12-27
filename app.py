import os
from parse import parse
import openai
from flask import Flask, redirect, render_template, request, url_for


app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        keyword = request.form["keyword"]
        response_definition = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_definition(keyword),
            temperature=0.7,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        response_sentence = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_sentence(keyword),
            temperature=0.7,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        return redirect(url_for("index", result_def=response_definition.choices[0].text, result_sen=response_sentence.choices[0].text))

    result_def = request.args.get("result_def")
    result_def_jp = ""
    result_def_en = ""
    if result_def is not None:
        result_def_jp, result_def_en = parse(result_def)
    result_sen = request.args.get("result_sen")
    return render_template("index.html", result_def_jp=result_def_jp, result_def_en=result_def_en, result_sen=result_sen)


def generate_sentence(keyword):
    return "write some sentences to show how to use " + keyword + " in Japanese"


def generate_definition(keyword):
    return keyword + " とは何ですか?日本語と英語で説明をお願いします。"
