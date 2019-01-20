from django import forms


class StatusForm(forms.Form):
    Tweet = forms.CharField(required=True, max_length=100,
                            widget=forms.Textarea, initial='Enter your Tweet here')
