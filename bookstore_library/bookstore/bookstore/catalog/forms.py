from django import forms

class AuthorForm(forms.Form):
    author_name = forms.CharField(widget=forms.TextInput(attrs={'class' : 'box_color'}))

    def clean_author_name(self):
        data = self.cleaned_data['author_name']
        return data
