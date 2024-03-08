from django.contrib import admin
from .models import Parfum, Order, OrderItem

# Inregistreaza modelele aici.

@admin.register(Parfum)
class ParfumAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


