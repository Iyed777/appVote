from django.shortcuts import render
from django.views.generic import View
# Create your views here.
from .forms import subsForm
from .models import Member

from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
    )

User = get_user_model()

class FormView(View):
	def get(self, request):
		form = subsForm()
		return render(request, "subscribe.html", {"form":form})

	
	def post(self, request):
		form = subsForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data["username"]
			password = form.cleaned_data["password"]
			first_name = form.cleaned_data["first_name"]
			last_name = form.cleaned_data.get("last_name")
			email = form.cleaned_data["email"]
			birth_date = form.cleaned_data["birth_date"]

			new_user = User(username=username)
			new_user.set_password(password)
			new_user.save()
			nuser = authenticate(username=new_user.username, password=password)

			login(self.request, nuser)

			new_member = Member(username=username, first_name=first_name, last_name=last_name, email=email, birth_date=birth_date)
			new_member.save()

			context ={
				"lastName": last_name,
				"birth_date": birth_date,
			}

			return render(request, "welcome.html", context)

		