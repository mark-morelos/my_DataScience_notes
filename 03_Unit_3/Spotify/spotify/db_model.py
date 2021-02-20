from flask_sqalchemy import SQAlchemy

DB = SQAlchemy

# class SongTitle(DB.Model):
#     id = DB.Column(DB.String(30), primary_key=True)
#     name = DB.Column(DB.String(50), unique=True, nullable=False)

#     def __repr__(self):
#         return '<SongTitle %r>' % self.name

# class Tempo(DB.Model):
#     id = DB.Column(DB.String(30), primary_key=True)
#     tempo = DB.Column(DB.Float, nullable=False)
#     songtitle = DB.relationship('SongTitle', backref=DB.backref('tempo', lazy=True))

#     def __repr__(self):
#         return '<Tempo %r>' % self.tempo

class Song(DB.Model):
    acousticness = DB.Column(DB.Float)
    artists = DB.Column(DB.String(75))
    danceability = DB.Column(DB.Integer)
    duration_ms = DB.Column(DB.Float)
    energy = DB.Column(DB.Float)
    explicit = DB.Column(DB.Float)
    id = DB.Column(DB.String(100), primary_key=True)
    instrumentalness = db.Column(DB.Float)
    key = DB.Column(DB.Integer)
    liveness = DB.Column(DB.Float)
    loudness = DB.Column(DB.Float)
    mode = DB.Column(DB.Integer)
    name = DB.Column(DB.String(100))
    popularity = DB.Column(DB.Integer)
    release_date = DB.Column(DB.String(20))
    speechiness = DB.Column(DB.Float)
    tempo = DB.Column(DB.Float)
    valence = DB.Column(DB.Float)
    year = DB.Column(DB.Integer)

    def __repr__(self):
        return '''<Title %r - Artist %r -Duration(ms) %r 
        - Acousticness -%r - Danceability %r - Instrumentalness %r 
        - Loudness %r - Speechiness %r - Valence %r>''' %(
            self.name,
            self.artists,
            self.duration_ms,
            self.acousticness,
            self.danceability,
            self.instrumentalness,
            self.loudness,
            self.speechiness,
            self.valence)