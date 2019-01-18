from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import *
from .models import *
# Create your views here.

def register(request):
	if request.method == 'POST':
		form = Register_form(request.POST)

		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/show/')
	else:
		form = Register_form()
	return render(request, 'register.html', {'form':form})


def show(request):
	data = Register.objects.all()
	return render(request, 'show.html', {'data':data})

def delete(request,id):
	dele = Register.objects.get(id=id).delete()
	return HttpResponseRedirect('/show/')

def edit(request,id):
	edit = Register.objects.get(id=id)
	form = Register_form(instance=edit)
	if request.method == 'POST':
		form = Register_form(request.POST,instance=edit)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/show/')
			
	return render(request, 'edit.html', {'form':form, 'id':id})


def login(request):
	if request.method == 'POST':
		form = Login_form(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('Saved Successfully')
	else:
		form = Login_form()
	return render(request, 'login.html', {'form':form})