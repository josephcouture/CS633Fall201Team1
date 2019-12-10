from django import forms
from .models import Resource, Skill, ResourceSkill, Project, ProjectTeam

class EnterResource(forms.ModelForm):
	class Meta:
		model = Resource
		fields = ('resource_fname', 'resource_lname', 'timezone_id', 'language_id')
		labels = {
			"resource_fname": "First Name",
			"resource_lname": "Last Name",
			"timezone_id": "Timezone",
			"language_id": "Language",
		}


class SelectSkill(forms.ModelForm):



	class Meta:
		model = ResourceSkill
		fields = ('resource_id', 'skill_id', 'resource_skill_level')
		labels = {
			"resource_id": "Resource",
			"skill_id" : "Skill",
			"resource_skill_level":" Resource Skill Level : To rate resource skills from 1-5 ",

		}
		SKILL_LEVEL = (
			('', 'Select a Value'),
			('1', '1'),
			('2', '2'),
			('3', '3'),
			('4', '4'),
			('5', '5'),
				)
		widgets = {
			'resource_skill_level': forms.Select(choices=SKILL_LEVEL,attrs={'class': 'form-control'}),
		}



class BuildTeam(forms.Form):
	SKILLS = (
		("1", "CS633 - Requirements"),
		("2", "CS633 - PM"),
		("3", "CS633 - Coding"),
		("4", "CS633 - Testing"),
		("5", "CS633 - UX"),
	)
	skills = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=SKILLS,label="<h4>Search for Skills</h4>")

class AddTeam(forms.ModelForm):

	class Meta:
		model = Project
		fields = ('project_description',)
		labels = {
			"project_description": "Team Name",
		}

class AddResourceTeam(forms.ModelForm):

	def __init__(self,*args,**kwargs):
		super (AddResourceTeam,self ).__init__(*args,**kwargs)
		self.fields['resource_id'].queryset = Resource.objects.filter(resource_onteam=False)

	class Meta:
		model = ProjectTeam
		fields = ('resource_id', 'project_id',)
		labels = {
			"resource_id": "Resource",
			"project_id": "Team",
		}

#	fname = forms.CharField()
#	lname = forms.CharField()
#	language = forms.ChoiceField(choices = [('english', 'English'), ('spanish', 'Spanish')])
#	timezone = forms.ChoiceField(choices = [('+11', '+11'), ('+12', '+12')])