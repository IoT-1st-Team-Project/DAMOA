from django.contrib import admin
from .models import Club

# class BoardAdmin(admin.ModelAdmin):
#     search_fields = ['category']

admin.site.register(Club)




