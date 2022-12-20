from django import forms


class CommentForm(forms.Form):
    comment = forms.CharField(widget=forms.Textarea)
    name = forms.CharField()
    email = forms.EmailField()
    website = forms.URLField()
