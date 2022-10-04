from dataclasses import field
from django import forms
from .models import Article

# field 설정으로 내가 원하는 input만 받을 수도 있음.
# model과 fields 설정


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = "__all__"
