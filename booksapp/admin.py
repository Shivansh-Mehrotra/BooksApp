from django.contrib import admin
from .models import Book,Author,Publisher

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('book_name', 'author', 'published_date', 'type')
    search_fields = ('title', 'author')


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name','birth_date')
    search_fields = ('first_name', 'last_name')


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name', 'website')
    search_fields = ('name',)