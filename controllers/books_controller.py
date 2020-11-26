from flask import Flask, render_template, Blueprint, redirect, request
from repositories import book_repository
from repositories import author_repository
import repositories.book_repository as book_repository
import repositories.author_repository as author_repository
from models.book import Book

books_blueprint = Blueprint("books", __name__)

@books_blueprint.route("/books")
def books():
    books = book_repository.select_all()
    return render_template("books/index.html", all_books = books)
# INDEX
# GET '/books'

@books_blueprint.route("/books/new", methods=["GET"])
def new_book():
    author = author_repository.select_all()
    return render_template("books/new.html", all_authors=author)

# NEW
# GET '/books/new'
@books_blueprint.route("/books/new", methods=["GET"])
def book():
    authors = author_repository.select_all()
    return render_template("books/new.html", all_authors=author)

# CREATE
# POST '/books'
# @books_blueprint.route("/books", methods=["POST"])
# def create_book():
#     # grab the form data for title, author, publisher and completed
#     title = request.form['title']
#     genre = request.form['genre']
#     publisher = request.form['publisher']
#     author = request.form['author']
#     author = author_repository.select(author_id)
#     # create a new book object
#     book = Book(title, genre, author, publisher)
#     # save that book object back to the database with the save method
#     book_repository.save(book)
#     return redirect('/books')
# # SHOW
#  def __init__(self, title, genre, publisher, author,  id = None, ):
# GET '/books/<id>'


# EDIT
# GET '/books/<id>/edit'


# UPDATE
# PUT '/books/<id>'



# DELETE
# DELETE '/books/<id>'

@books_blueprint.route("/books/<id>/delete", methods=['POST'])
def delete_book(id):
    book_repository.delete(id)
    return redirect('/books')
