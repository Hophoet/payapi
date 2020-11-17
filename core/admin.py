from django.contrib import admin
from .models import Client, Transfert, Method

# Register your models here.
admin.site.register(Client)
admin.site.register(Transfert)
admin.site.register(Method)
