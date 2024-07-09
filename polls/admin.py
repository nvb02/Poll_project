from django.contrib import admin
from .models import *

# Register your models here.

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class PollAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]

class VoteAdmin(admin.ModelAdmin):
    list_display = ('poll', 'choice')

admin.site.register(Poll, PollAdmin)
admin.site.register(Vote, VoteAdmin)
admin.site.register(Choice)
