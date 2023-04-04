from django import forms

class TranslatorForm(forms.Form):
    source_text = forms.CharField(label="Source Text", max_length=500)
