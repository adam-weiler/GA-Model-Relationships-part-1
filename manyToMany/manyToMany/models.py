from django.conf import settings #Needed for foreignkey.
from django.contrib.auth.models import User
from django.db import models
# from django.forms import ModelForm
from django.utils import timezone # Needed for timezone.localtime()


# 1. Imagine an app that allows users to keep track of what films they've seen:
class Film(models.Model): #Film must be written first.
    title = models.CharField(max_length=255)
    director = models.CharField(max_length=255)
    year = models.IntegerField()

    def __str__(self):
        return f'title = {self.title}'

class Viewer(models.Model): #Viewer must be written first.
    user_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.IntegerField()

    def __str__(self):
        return f'user_name = {self.user_name}'

class Films_Watched(models.Model): #Has Many Through
    appointment_date = models.DateTimeField(default=timezone.localtime())
    film_id = models.ForeignKey(Film, on_delete=models.CASCADE, related_name='films')
    viewer_id = models.ForeignKey(Viewer, on_delete=models.CASCADE, related_name='viewers')
    
    def __str__(self):
        return f'film {self.film_id}, viewer {self.viewer_id}'



# 2. Imagine an app that allows users to keep track of the books they've read:
class Author(models.Model): #Author must be written first.
    name = models.CharField(max_length=255)
    biography = models.TextField(max_length=255)

    def __str__(self):
        return f'name = {self.name}'

class Book(models.Model): #Book must be written first.
    title = models.CharField(max_length=255)
    year = models.IntegerField()

    def __str__(self):
        return f'title = {self.title}'

class Reader(models.Model): #Reader must be written first.
    user_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.IntegerField()
    favourite_genre = models.CharField(max_length=255)

    def __str__(self):
        return f'user_name = {self.user_name}'

class Authorship(models.Model): #Has Many Through
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='authors')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='book_authors')

    def __str__(self):
        return f'author {self.author}, book {self.book}'

class Books_Read(models.Model): #Has Many Through
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='books')
    reader = models.ForeignKey(Reader, on_delete=models.CASCADE, related_name='readers')

    def __str__(self):
        return f'book {self.book}, reader {self.reader}'

class Chapter(models.Model):
    title = models.CharField(max_length=255)
    length = models.IntegerField()
    summary = models.CharField(max_length=255)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='book_chapters')

    def __str__(self):
        return f'title = {self.title}'



# 3. Comics:
class Artist(models.Model): #Artist must be written first.
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self):
        return f'first_name = {self.first_name}, last_name = {self.last_name}'

class Comic(models.Model): #Comic must be written first.
    series = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)

    def __str__(self):
        return f'series = {self.series}'

class Writer(models.Model): #Writer must be written first.
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self):
        return f'first_name = {self.first_name}, last_name = {self.last_name}'

class Comic_Artist(models.Model): #Has Many Through
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='artists_comic')
    comic = models.ForeignKey(Comic, on_delete=models.CASCADE, related_name='comics_artist')

    def __str__(self):
        return f'artist {self.artist}, comic {self.comic}'

class Comic_Writer(models.Model): #Has Many Through
    comic = models.ForeignKey(Comic, on_delete=models.CASCADE, related_name='comics_writer')
    writer = models.ForeignKey(Writer, on_delete=models.CASCADE, related_name='writers_comic')

    def __str__(self):
        return f'comic {self.comic}, writer {self.writer}'

class Issue(models.Model):
    title = models.CharField(max_length=255)
    year = models.IntegerField()
    comic_id = models.ForeignKey(Comic, on_delete=models.CASCADE, related_name='comics')

    def __str__(self):
        return f'title = {self.title}'