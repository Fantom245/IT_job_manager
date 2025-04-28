from django import forms


class WorkerSearchForm(forms.Form):
    username = forms.CharField(max_length=255, required=False)
