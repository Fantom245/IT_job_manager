from django import forms


class TaskSearchForm(forms.Form):
    name = forms.CharField(max_length=255, required=False)
