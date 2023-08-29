from django.contrib import admin
from.models import port

admin.site.register(port)

# class port(admin.ModelAdmin):
#     list_display = ('id', 'name',)

# Register your models here.
