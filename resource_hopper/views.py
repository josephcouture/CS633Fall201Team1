from django.shortcuts import render
from django.http import HttpResponse
from .models import ProjectTeam
from .models import Resource
from .models import ResourceSkill
from .models import Skill
from .forms import EnterResource, SelectSkill, BuildTeam, AddTeam, AddResourceTeam

def teams(request):
	context = {
		'projectteams': ProjectTeam.objects.order_by('project_id'),
		'resource': Resource.objects.all(),
		'skill': Skill.objects.all(),
		'resourceskill': ResourceSkill.objects.all(),
		'addteam': AddTeam(),

	}

	if request.method == 'POST':
		addteam_form = AddTeam(request.POST)
		if addteam_form.is_valid():
			addteam_form.save()
		
		context['newteam'] = addteam_form.cleaned_data['project_description']



	return render(request, 'resource_hopper/teams.html', context)

def resource(request):
	context = {
		'resourceform': EnterResource(),
		'skillform': SelectSkill()
	}

	if request.method == 'POST':
		resource_form = EnterResource(request.POST)
		skill_form = SelectSkill(request.POST)
		if resource_form.is_valid():
			#print("VALID RESOURCE")
			resource_form.save()
			resourcefullname = resource_form.cleaned_data['resource_fname'] + " " + resource_form.cleaned_data['resource_lname']
			context['resourcefullname'] = resourcefullname
		if skill_form.is_valid():
			#print("VALID SKILL")
			skill_form.save()
			context['resource_id'] = skill_form.cleaned_data['resource_id']
			#print(skill_form.cleaned_data)
			


#	resourceform = EnterResource()
	return render(request, 'resource_hopper/resource.html', context)


def buildteam(request):
	context = {
		'buildteam': BuildTeam(),
		'addresourceteam': AddResourceTeam(),
		#'selected_skills': selected_skills,
	}	

	if request.method == 'POST':
		form = BuildTeam(request.POST)
		addresourceteam = AddResourceTeam(request.POST)
		if form.is_valid():
			selected_skills = form.cleaned_data['skills']
			matched_skills = ResourceSkill.objects.none()
			for d in selected_skills:

				matched_skills = matched_skills | ResourceSkill.objects.filter(skill_id=d)
			context = {
				'buildteam': BuildTeam(),
				'matched_skills': matched_skills,
				'addresourceteam': AddResourceTeam(),
			}
		if addresourceteam.is_valid():
			affected_resource = (addresourceteam.cleaned_data['resource_id'])
			team = (addresourceteam.cleaned_data['project_id'])
			affected_resource.resource_onteam = True
			success = True
			affected_resource.save()
			#print(affected_resource.resource_onteam)
			addresourceteam.save()
			context = {
					'addresourceteam': AddResourceTeam(),
					'buildteam': BuildTeam(),
					'affectedresource': affected_resource,
					'team': team,
					'success': success,

			}


	return render(request, 'resource_hopper/buildteam.html', context)




def home(request):
	return HttpResponse('<h1>Home Page</h1>')


