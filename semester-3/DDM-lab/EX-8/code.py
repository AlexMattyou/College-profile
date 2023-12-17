from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, CheckConstraint
from sqlalchemy.orm import declarative_base, Session, relationship

engine = create_engine("sqlite:///:memory:")
Base = declarative_base()

class Author(Base):
    __tablename__ = "Authors"

    AuthorID = Column(Integer, primary_key=True)
    Name = Column(String(20), nullable=False)
    books = relationship("Book", back_populates="author")

class Publisher(Base):
    __tablename__ = "Publishers"
    PublisherID = Column(Integer, primary_key=True)
    Name = Column(String(10), nullable=False)
    books = relationship("Book", back_populates="publisher")

class Book(Base):
    __tablename__ = "Books"
    BookID = Column(Integer, primary_key=True)
    Title = Column(String(30), nullable=False)
    AuthorID = Column(Integer, ForeignKey("Authors.AuthorID"), nullable=False)
    PublisherID = Column(Integer, ForeignKey("Publishers.PublisherID"), nullable=False)
    PublicationYear = Column(Integer, CheckConstraint("PublicationYear > 1"))
    author = relationship("Author", back_populates="books")
    publisher = relationship("Publisher", back_populates="books")

Base.metadata.create_all(engine)

session = Session(engine)
authorsData = [
    {"AuthorID": 1, "Name": "Guru Rohith"},
    {"AuthorID": 2, "Name": "Roger Samuel"},
]
publishersData = [
    {"PublisherID": 1, "Name": "Alpha"},
    {"PublisherID": 2, "Name": "Beta"},
    {"PublisherID": 3, "Name": "Gamma"},
]
booksData = [
    {"BookID": 1, "Title": "Our Responsibility", "AuthorID": 1, "PublisherID": 1, "PublicationYear": 2017},
    {"BookID": 2, "Title": "School != Education", "AuthorID": 2, "PublisherID": 2, "PublicationYear": 2022},
    {"BookID": 3, "Title": "Think Savant", "AuthorID": 2, "PublisherID": 1, "PublicationYear": 2020},
    {"BookID": 4, "Title": "Chess of Life", "AuthorID": 1, "PublisherID": 3, "PublicationYear": 2019},
    {"BookID": 5, "Title": "Change Your Story", "AuthorID": 2, "PublisherID": 3, "PublicationYear": 2023},
]

for author_data in authorsData:
    session.add(Author(**author_data))
for publisher_data in publishersData:
    session.add(Publisher(**publisher_data))
for book_data in booksData:
    session.add(Book(**book_data))

session.commit()
authors_query = session.query(Author).all()
publishers_query = session.query(Publisher).all()
books_query = session.query(Book).all()

print("\nAuthors:")
for author in authors_query:
    print(f"AuthorID: {author.AuthorID}, Name: {author.Name}")
print("\nPublishers:")
for publisher in publishers_query:
    print(f"PublisherID: {publisher.PublisherID}, Name: {publisher.Name}")
print("\nBooks:")
for book in books_query:
    print(
        f"BookID: {book.BookID}, Title: {book.Title}, AuthorID: {book.AuthorID}, "
        f"PublisherID: {book.PublisherID}, PublicationYear: {book.PublicationYear}"
    )

session.close()
