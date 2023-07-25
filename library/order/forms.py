from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    plated_end_at = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))

    class Meta:
        model = Order
        fields = ["book", "plated_end_at"]

    def clean(self):
        cleaned_data = super().clean()
        book = cleaned_data.get("book")
        if book and book.count < 1:
            raise forms.ValidationError("No book available, you can't order this book.")
        return cleaned_data

    def save_order(self, user):
        order = self.save(commit=False)
        order.user = user
        book = self.cleaned_data["book"]
        book.count -= 1
        book.save()
        order.save()
        return order
