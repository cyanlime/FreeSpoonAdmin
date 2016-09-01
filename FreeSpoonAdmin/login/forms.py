from django import forms

class RegisterForm(forms.Form):
	username = forms.CharField(label='UserName', max_length=40)
	password = forms.CharField(label='PassWord', widget=forms.PasswordInput, max_length=40)
	password2 = forms.CharField(label='PassWord', widget=forms.PasswordInput, max_length=40)
	email = forms.EmailField(label='Email', max_length=40)
	mob = forms.CharField(label='MobNum', max_length=15)

class LoginForm(forms.Form):
	username = forms.CharField(label='UserName', max_length=40)
	password = forms.CharField(label='PassWord', widget=forms.PasswordInput, max_length=40)

class ChangePwd(forms.Form):
	password = forms.CharField(label='PassWord', widget=forms.PasswordInput, max_length=40)
	newpassword = forms.CharField(label='NewPassWord', widget=forms.PasswordInput, max_length=40)


