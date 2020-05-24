from django.contrib import admin
from p_library.models import Book, Author, Publisher

@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ['name', 'adress']
    fields = ['name', 'adress']

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    @staticmethod
    def author_full_name(obj):
        return obj.author.full_name
    @staticmethod
    def publisher_full_name(obj):
        return obj.publisher.name

    list_display = ['title', 'author_full_name', 'publisher_full_name']
    fields = ('ISBN', 'title', 'description', 'year_release', 'author', 'price', 'publisher')

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['full_name']


