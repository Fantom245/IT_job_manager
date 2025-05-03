from django import forms

from .models import Project


class TeamSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search by team name"}
        )
    )


class ProjectSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search by project name"}
        )
    )


class ProjectTeamForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['teams']
