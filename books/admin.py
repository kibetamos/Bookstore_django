from django.contrib import admin

# Register your models here.
from .models import Book


admin.site.register(Book)


class BookAdmin(admin.ModelAdmin):
  
  list_display = ("title", "author", "price")
  
admin.site.register(Book, BookAdmin)


# books/admin.py
# from django.contrib import admin
# from .models import Book
# class BookAdmin(admin.ModelAdmin):
# list_display = ("title", "author", "price",)
# admin.site.register(Book, BookAdmin)