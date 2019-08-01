from django.contrib import admin
from manyToMany.models import Film, Viewer, Films_Watched
from manyToMany.models import Author, Book, Reader, Authorship, Books_Read, Chapter
from manyToMany.models import Artist, Comic, Writer, Comic_Artist, Comic_Writer, Issue

admin.site.register(Film) #Play must be called first.
admin.site.register(Viewer) #Play must be called first.
admin.site.register(Films_Watched) #Has Many Through

admin.site.register(Author) #Author must be called first.
admin.site.register(Book) #Book must be called first.
admin.site.register(Reader) #Book must be called first.
admin.site.register(Authorship) #Has Many Through
admin.site.register(Books_Read) #Has Many Through
admin.site.register(Chapter)

admin.site.register(Artist) #Artist must be called first.
admin.site.register(Comic) #Comic must be called first.
admin.site.register(Writer) #Writer must be called first.
admin.site.register(Comic_Artist) #Has Many Through
admin.site.register(Comic_Writer) #Has Many Through
admin.site.register(Issue)