from flask import Flask, render_template, request, redirect, url_for
from book import Book

app = Flask(__name__)

all_books = []


@app.route('/')
def home():
    return render_template("index.html")


@app.route("/add", methods=["GET", "POST"])
def add():
    print(request.method)
    data = request.form
    Book(data["book_name"], data["book_author"], data["rating"])
    return render_template("add.html")


if __name__ == "__main__":
    app.run(debug=True)

