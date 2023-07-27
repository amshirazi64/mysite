from django.contrib import admin
from .models import Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice

@admin.register(Question)
class QustionAdmin(admin.ModelAdmin):
    model = Question
    inlines = [ChoiceInline]