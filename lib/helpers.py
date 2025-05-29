from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Genre, Book, ReadingStatus

engine = create_engine('sqlite:///bookbuddy.db')
Session = sessionmaker(bind=engine)

def get_session():
    return Session()

def list_genres():
    session = get_session()
    genres = session.query(Genre).all()
    session.close()
    return genres

def list_books():
    session = get_session()
    books = session.query(Book).all()
    session.close()
    return books

def add_genre(name):
    session = get_session()
    genre = Genre(name=name)
    session.add(genre)
    session.commit()
    session.close()

def add_book(title, author, genre_name, status=ReadingStatus.to_read):
    session = get_session()
    genre = session.query(Genre).filter_by(name=genre_name).first()
    if not genre:
        genre = Genre(name=genre_name)
        session.add(genre)
        session.commit()
    book = Book(title=title, author=author, genre=genre, status=status)
    session.add(book)
    session.commit()
    session.close()
