from django import forms
from .models import *

class EmailForms(forms.Form):
    name=forms.CharField(max_length=255)
    email=forms.EmailField()
    # email1=forms.EmailField(widget=forms.EmailInput)
    comment=forms.CharField(widget=forms.Textarea)
    image=forms.ImageField()
    file=forms.FileField()
    # age = forms.IntegerField()
    # is_active = forms.BooleanField()
    # country = forms.ChoiceField(choices=[('USA', 'United States'), ('UK', 'United Kingdom')], widget=forms.Select)
    # gender = forms.ChoiceField(choices=[('M', 'Male'), ('F', 'Female')], widget=forms.RadioSelect)
    # hobbies = forms.MultipleChoiceField(choices=[('s', 'Skiing'), ('f', 'Fishing'), ('r', 'Running')], widget=forms.CheckboxSelectMultiple)
    
    # comment1=forms.CharField(widget=forms.TextInput)
    
    
    
    # name=forms.CharField(max_length=50)
    # email=forms.EmailField()
    # to=forms.EmailField()
    # comment=forms.CharField(required=False,widget=forms.Textarea)
    # comment1=forms.Textarea()
    
    
class IcecreamForms(forms.ModelForm):
    class Meta:
        model=Icecream
        fields=('name','description','photo','file')
        # fields=('name', 'description', 'photo', 'file', 'slug')

