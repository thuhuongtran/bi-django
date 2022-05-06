from django.contrib import admin

from mysite.polls.models import Question, Choice


class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question_text']


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
