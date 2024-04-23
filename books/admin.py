from django.contrib import admin
from .models import Book, Review


class ReviewInLin(admin.TabularInline):
    model = Review


class BookAdmin(admin.ModelAdmin):
    inlines = [
        ReviewInLin,
    ]
    list_display = ['title', 'author', 'price']


admin.site.register(Book, BookAdmin)
