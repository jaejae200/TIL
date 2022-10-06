from cProfile import label
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        labels = {
            'title' : ('제목'),
            'summary' : ('줄거리'),
            'running_time' : ('러닝 타임')
        }
        widgets = {
            'title' : forms.TextInput(attrs={
                'placeholder': '영화 제목을 입력해주세요.'
            }),
            'summary' : forms.Textarea(attrs={
                'placeholder': '줄거리를 입력해주세요.'
            }),
            'running_time' : forms.TextInput(attrs={
                'placeholder' : '영화 상영 시간 (분 단위)'
            })
        }
