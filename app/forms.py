from flask_wtf import FlaskForm
from wtforms import RadioField, SubmitField, StringField, IntegerField, HiddenField
from wtforms.validators import DataRequired
from wtforms_sqlalchemy.fields import QuerySelectField
from app.models import Genres
from app import db


def choice_query():
    """Funkcja potrzeban do zaludnienia dropdown listę w formularzu"""
    return Genres.query

class RadioForm(FlaskForm):
    radio_field = RadioField(label = "Co zamierzasz zrobić?:",choices=[('browse','Przeglądaj bibliotekę'),
                                        ('add','Dodaj pozycję do biblioteki')])
    submit_field = SubmitField("Wykonaj")

class AddNewBookForm(FlaskForm):
    title = StringField('Tytuł:', validators=[DataRequired()])
    author = StringField('Autor:', validators=[DataRequired()])
    description = StringField('Opis:', validators=[DataRequired()])
    published = IntegerField('Rok wydania:', validators=[DataRequired()])
    publisher = StringField('Wydawca:', validators=[DataRequired()])
    cover = StringField('URL Okładki:', validators=[DataRequired()])
    genre = QuerySelectField('Gatunek:', query_factory=choice_query, allow_blank=False, get_label='name')
    submit_field = SubmitField("Dodaj do biblioteki")

class BorrowFrom(FlaskForm):
    name = StringField('Imię:', validators=[DataRequired()])
    last_name = StringField('Nazwisko')
    address = StringField('Adres:')
    submit_field = SubmitField('OK')

class AddNewAuthorForm(FlaskForm):
    name = StringField('Imię:')
    last_name = StringField('Nazwisko:', validators=[DataRequired()])
    description = StringField('Opis:', validators=[DataRequired()])
    submit_field = SubmitField("Dodaj autora do biblioteki")

class AddNewPublisherForm(FlaskForm):
    name = StringField('Nazwa Wydwanictwa:', validators=[DataRequired()])
    address = StringField('Adres Wydawnictwa:')
    description = StringField('Opis:')
    submit_field = SubmitField("Dodaj wydawnictwo do biblioteki")

class UpdateBookForm(FlaskForm):
    id = HiddenField('Id', validators=[DataRequired()])
    title = StringField('Tytuł:', validators=[DataRequired()])
    author = StringField('Autor:', validators=[DataRequired()])
    description = StringField('Opis:', validators=[DataRequired()])
    published = IntegerField('Rok wydania:', validators=[DataRequired()])
    publisher = StringField('Wydawca:', validators=[DataRequired()])
    cover = StringField('URL Okładki:', validators=[DataRequired()])
    genre = QuerySelectField('Gatunek:', query_factory=choice_query, allow_blank=False, get_label='name')
    borrowed_id = HiddenField('Borrowed_id:')
    submit_field = SubmitField("Dodaj do biblioteki")