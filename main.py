from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books-collection.db'
#Optional: But it will silence the deprecation warning in the console.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float(50), nullable=False)

# Create initial database
db.create_all()


@app.route('/')
def home():
    # Read all records
    all_books = db.session.query(Book).all()
    return render_template(
        "index.html",
        books=all_books
    )


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        # Add to database
        book = Book(
            title=request.form["book_name"],
            author=request.form["book_author"],
            rating=request.form["rating"]
        )
        db.session.add(book)
        db.session.commit()
        return redirect(url_for('home'))

    return render_template("add.html")


@app.route("/edit/<int:index>", methods=["GET","POST"])
def edit(index):
    if request.method == "POST":
        # Update database entry
        # book = Book(
        #     title=request.form["book_name"],
        #     author=request.form["book_author"],
        #     rating=request.form["rating"]
        # )
        return redirect(url_for('home'))

    book_to_update = Book.query.get(index)
    return render_template(
        "edit.html",
        book=book_to_update
    )


if __name__ == "__main__":
    app.run(debug=True)

