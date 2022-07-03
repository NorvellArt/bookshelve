from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'genre', 'description', 'is_complete']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'author': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'genre': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'description': forms.Textarea(attrs={'class': 'form-control mb-3', 'rows': 5}),
            'is_complete': forms.CheckboxInput(attrs={'class': 'mb-3'}),

        }
