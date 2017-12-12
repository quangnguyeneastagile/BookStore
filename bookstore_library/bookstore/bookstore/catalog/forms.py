from django import forms
from .models import Category

class CategoryForm(forms.Form):
    category_list = Category.objects.all()
    options = [('','All categories'),]
    for category in category_list:
        options.append((category, category))
    category_name = forms.CharField(label = 'Category', widget=forms.Select(choices=options))

    def clean_category_name(self):
        data = self.cleaned_data['category_name']
        return data

class AuthorForm(forms.Form):
    author_name = forms.CharField(widget=forms.TextInput(attrs={'class' : 'box_color'}))

    def clean_author_name(self):
        data = self.cleaned_data['author_name']
        return data
