from django.contrib import admin
from .models import Book,Character,Author

# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    #fields = ['title','description']
    list_display = ['title','price']
    list_filter = ['published']
    search_fields = ['title']

admin.site.register(Character)
admin.site.register(Author)
