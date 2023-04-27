from django.contrib import admin
from.models import Challenges , Images, Paragraph, Task, Titel 
from.serializers import ChallengesSreilalizer, ImagesSreilalizer, ParagraphSreilalizer ,TaskSreilalizer, TitelSreilalizer

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





admin.site.register(Challenges)