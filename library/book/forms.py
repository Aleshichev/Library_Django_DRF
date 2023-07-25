from django import forms
from .models import Book
from authentication.models import CustomUser
from author.models import Author


class AddFormBook(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-input",
                    "placeholder": "Enter Name",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "cols": 30,
                    "rows": 2,
                    "placeholder": "Write a description",
                }
            ),
            "count": forms.NumberInput(attrs={"class": "form-control", "default": 10}),
            "authors": forms.SelectMultiple(attrs={"size": 3, "class": "form-control"}),
            "year_of_publication": forms.Select(
                choices=[(year, year) for year in range(1900, 2024)],
            ),
            "date_of_issue": forms.DateInput(
                attrs={"class": "form-control", "type": "date"}
            ),
        }


class FilterForm(forms.Form):
    parameter = forms.ChoiceField(
        choices=[
            ("None", "All books"),
            ("authors", "Authors ID"),
            ("title", "Title"),
            ("count", "Count"),
        ],
        widget=forms.Select(attrs={"class": "form-control"}),
        required=False,
    )
    value = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}), required=False
    )


class AddUserForm(forms.Form):
    user = forms.ModelChoiceField(
        queryset=CustomUser.objects.all().order_by("id"),
        widget=forms.Select(attrs={"class": "form-control"}),
        required=False,
        empty_label=None,
        to_field_name="id",
    )


class AddAuthorForm(forms.Form):
    author = forms.ModelChoiceField(
        queryset=Author.objects.all(), label="Choose an author"
    )
