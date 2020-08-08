from django import forms

from .models import models, User


class RegistForm(forms.Form):
    username=forms.CharField(max_length=100,error_messages={"min_length":'用户名设定不符合要求'})
    password=forms.CharField(max_length=100,error_messages={"min_length":'密码设定不符合要求'})

    def clean_username(self):
        username = self.cleaned_data.get('username')
        exists = User.objects.filter(username=username).exists()
        if exists:
            # 验证失败抛出的异常
            raise forms.ValidationError(message='用户名已被占用')
        return username
class LoginForm(forms.Form):
    username=forms.CharField(max_length=100,error_messages={"min_length":'用户名设定不符合要求'})
    password=forms.CharField(max_length=100,error_messages={"min_length":'密码设定不符合要求'})

class SelectForm(forms.Form):
    username= forms.CharField(max_length=100)