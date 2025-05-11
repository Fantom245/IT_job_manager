from django import forms


class WorkerSearchForm(forms.Form):
    username = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "class": "form-control rounded-start",
                "placeholder": "Search by workers name",
                "style": "height: 38px;",
            }
        )
    )
