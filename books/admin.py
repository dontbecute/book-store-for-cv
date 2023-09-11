from django.contrib import admin
from django.contrib.admin import TabularInline

# Register your models here.

from .models import Books , Review

class ReviewInLine(TabularInline):
    model = Review

class BookAdmin(admin.ModelAdmin):
    model = Books

    inlines = [
        ReviewInLine,
    ]
    list_display = (
        "title",
        "auth", 
        "price"
    )

admin.site.register(Books , BookAdmin)