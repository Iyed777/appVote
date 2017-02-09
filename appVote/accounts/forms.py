from django import forms


class subsForm(forms.Form):
	username  = forms.CharField(label="username")
	password = forms.CharField(label="password", widget=forms.PasswordInput)
	firt_name = forms.CharField(label="first name")
	last_name = forms.CharField(label="last name")
	email = forms.EmailField(label="e-mail")
	birth_date = forms.DateField(label="birth date", widget=forms.SelectDateWidget(years=range(1970, 2017)))