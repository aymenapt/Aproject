from django.contrib import admin
from.models import *


# Register your models here.

class ImagesAdmin(admin.StackedInline):
    model = Images
class TitelAdmin(admin.StackedInline):
    model = Titel

class ParagraphAdmin(admin.StackedInline):
    model = Paragraph    

class TaskAdmin(admin.ModelAdmin):
    inlines = [ImagesAdmin,TitelAdmin,ParagraphAdmin]

    class Meta:
        model = Task


admin.site.register(Task, TaskAdmin)

class ChallengeRulesAdmin(admin.StackedInline):
    model=ChallengeRules

class ChallengeAdmin(admin.ModelAdmin):
    inlines = [ChallengeRulesAdmin]

    class Meta :
        model =Challenges

    

admin.site.register(SposorAds)
admin.site.register(Challenges,ChallengeAdmin)