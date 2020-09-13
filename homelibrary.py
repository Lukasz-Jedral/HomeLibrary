from app import app, db
from app.models import Books, Genres, Borrowed
import os
from flask import Flask, request, render_template, redirect, url_for
from app.forms import RadioForm, AddNewBookForm, BorrowFrom, UpdateBookForm
from datetime import datetime

@app.route("/home_library/main", methods=["GET", "POST"])
def load_main_view():
    form = RadioForm()
    if request.method == "POST":
        response = form.radio_field.data
        if response == 'browse':
            return redirect(url_for('display_full_list'))

        if response == 'add':
            return redirect(url_for('add_new_book'))

    return render_template('main.html', form = form)

@app.route("/home_library/add_new_book", methods=["GET", "POST"])
def add_new_book():
    form = AddNewBookForm()
    if request.method == "POST":
        if form.validate_on_submit():
            temp_dict = request.form.to_dict()
            book = Books(title = temp_dict['title'],
                         author = temp_dict['author'],
                         genre_id = temp_dict['genre'],
                         description = temp_dict['description'],
                         published = datetime(int(temp_dict['published']), 1, 1),
                         publisher = temp_dict['publisher'],
                         cover_url = temp_dict['cover']
                         )
            db.session.add(book)
            db.session.commit()
            return render_template('upload_succesful.html')

    return render_template('add_new_book.html', form = form)

@app.route("/home_library/full_list", methods=["GET", "POST"])
def display_full_list():
    books = Books.query.all()
    return render_template('full_list.html', books = books)

@app.route("/home_library/book/<int:book_id>", methods=["GET", "POST"])
def book_details(book_id):
    book = Books.query.get(book_id)
    for genre_id, in db.session.query(Books.genre_id):
        genre = Genres.query.get(genre_id)
    return render_template('book_details.html',
                           book = book,
                           book_id = book_id,
                           genre = genre)

@app.route("/home_library/book_update/<int:book_id>", methods=["GET", "POST"])
def book_update(book_id):
    if request.method == "GET":
        book = Books.query.get(book_id)
        form = UpdateBookForm(data = book)
        return render_template('book_update.html',
                               form=form)
    elif request.method == "POST":
        form = AddNewBookForm()
        if form.validate_on_submit():
            temp_dict = request.form.to_dict()
            book = Books(title=temp_dict['title'],
                         author=temp_dict['author'],
                         genre_id=temp_dict['genre'],
                         description=temp_dict['description'],
                         published=datetime(int(temp_dict['published']), 1, 1),
                         publisher=temp_dict['publisher'],
                         cover_url=temp_dict['cover']
                         )
            db.session.update(book)
            db.session.commit()
            return render_template('upload_succesful.html')


@app.route("/home_library/book_delete/<int:book_id>", methods=["GET", "POST"])
def book_delete(book_id):
    if request.method == "GET":
        book = Books.query.get(book_id)
        return render_template('delete_confirmation.html', book = book)

    elif request.method == "POST":
        book = Books.query.get(book_id)
        db.session.delete(book)
        db.session.commit()
        return render_template('upload_succesful.html')


@app.route("/home_library/borrow/<int:book_id>", methods=["GET","POST"])
def borrow_book(book_id):
    if request.method == "GET":
        book = Books.query.get(book_id)
        form = BorrowFrom()
        return render_template('book_borrow.html',
                               book = book,
                               form = form)
    elif request.method == "POST":
        form = BorrowFrom()
        if form.validate_on_submit():
            temp_dict = request.form.to_dict()
            #adding new row to borrowed table
            borrowed = Borrowed(id=book_id,
                                name=temp_dict['name'],
                                last_name=temp_dict['last_name'],
                                address=temp_dict['address'],
                                #created=datetime.utcnow()
                                )
            db.session.add(borrowed)

            #updating borrowed_id field for corresponding book
            book = Books.query.get(book_id)
            book.borrowed_id = book.id
            db.session.add(book)
            db.session.commit()
            return render_template('upload_succesful.html')



@app.route("/home_library/borrow_status/<int:book_id>", methods=["GET","POST"])
def book_borrow_status(book_id):
    if request.method == "GET":
        book = Books.query.get(book_id)
        borrowed = Borrowed.query.get(book_id)
        return render_template('borrowed_status.html',
                               book = book,
                               borrowed = borrowed)
    elif request.method == "POST":
        book = Books.query.get(book_id)
        borrowed = Borrowed.query.get(book_id)

        #setting borrowed_id to empty
        book.borrowed_id = None
        db.session.add(book)

        #removing corresponding row from borrowed
        db.session.delete(borrowed)
        db.session.commit()
        return render_template('upload_succesful.html')

if __name__ == '__main__':
    app.run(debug=True)
