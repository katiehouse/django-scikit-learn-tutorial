from django.contrib import admin
from .models import Predictions


@admin.register(Predictions)
class PredictionsAdmin(admin.ModelAdmin):
    pass
