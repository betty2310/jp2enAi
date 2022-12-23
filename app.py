import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        animal = request.form["animal"]
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_definition_en(
                animal) + generate_definition_jp(animal),
            temperature=0.7,
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_sentence(keyword):
    return "Suggest some sentences in Japanese with keyword '" + keyword + "'"


def generate_definition_en(keyword):
    return "explain for the word '" + keyword + "' in English"


def generate_definition_jp(keyword):
    return "explain for the word '" + keyword + "' in Japanese"
