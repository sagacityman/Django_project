from WebCase import models
from django import forms


class CaseModelFrom(forms.ModelForm):
    class Meta:
        models = models.Case
        fields = '__all__'
