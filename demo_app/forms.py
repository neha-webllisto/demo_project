from django.forms import ModelForm
from .models import *
from django import forms


class Register_form(forms.ModelForm):
	# choices
	SUBJECT = (('Choose Subject','Choose Subject'), ('C','C'), ('C++','C++'), ('Java','Java'),
	 ('Php','Php'), ('Python','Python'))

	subject = forms.ChoiceField(choices=SUBJECT)

	class Meta:
		model = Register
		fields = '__all__'


class Login_form(ModelForm):
	class Meta:
		model = Login 
		fields = '__all__'