from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

# Write your classes below

class Artist(Base):
    __tablename__ = 'artists'

    id = Column(Integer, primary_key = True)
    name = Column(Text)

    songs = relationship('Song', back_populates = 'artists')
    genres = relationship('Genre', secondary='songs', back_populates='artists')

class Genre(Base):
    __tablename__ = 'genres'

    id = Column(Integer, primary_key = True)
    name = Column(Text)

    songs = relationship('Song', back_populates = 'genres')
    artists = relationship('Artist', secondary='songs', back_populates='genres')


class Song(Base):
    __tablename__ = 'songs'

    id = Column(Integer, primary_key = True)
    name = Column(Text)
    artist_id = Column(Integer, ForeignKey('artists.id'))
    genre_id = Column(Integer, ForeignKey('genres.id'))

    artists = relationship('Artist', back_populates = 'songs')
    genres = relationship('Genre', back_populates = 'songs')

engine = create_engine('sqlite:///songs.db')
Base.metadata.create_all(engine)
