from django import forms
from movie.models import Movie,User

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'
        widgets = {
            'image': forms.FileInput(attrs={'accept': 'image/*'})
        }


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'