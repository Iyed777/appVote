from django.shortcuts import render
from django.views.generic import View
# Create your views here.
from .forms import subsForm


class FormView(View):
	def get(self, request):
		form = subsForm()
		return render(request, "subscribe.html", {form:"form"})

	
		