from django.contrib import admin
from .models import Post
# Register your models here.

#Registra nuestro objeto post en el administrador
#de django para poder consultar o actualiza información
#del o de los post's.
admin.site.register(Post)