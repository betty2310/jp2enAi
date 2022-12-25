import os

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
            prompt=generate_definition_jp(keyword),
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
        return redirect(url_for("index", result=response_definition.choices[0].text + "\n" + response_sentence.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_sentence(keyword):
    return "write some sentences to show how to use " + keyword + " in Japanese"


def generate_definition_en(keyword):
    return "explain for the word '" + keyword + "' in English"


def generate_definition_jp(keyword):
    return keyword + " とは何ですか 1. 日本語 2. English"
