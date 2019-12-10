from django.contrib import admin
from .models import Language, Resource, Timezone, Skill, Manager, ResourceSkill, Project, ProjectTeam 

# Register your models here.

admin.site.register(Timezone)
admin.site.register(Language)
admin.site.register(Resource)
admin.site.register(Skill)
admin.site.register(Manager)
admin.site.register(ResourceSkill)
admin.site.register(Project)
admin.site.register(ProjectTeam)