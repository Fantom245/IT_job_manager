from django import forms

from .models import Project


class TeamSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "class": "form-control rounded-start",
                "placeholder": "Search by team name",
                "style": "height: 38px;"
            }
        )
    )


class ProjectSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "class": "form-control rounded-start",
                "placeholder": "Search by project name",
                "style": "height: 38px;",
            }
        )
    )


class ProjectTeamForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['teams']
