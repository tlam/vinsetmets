from django import forms

from wines.models import Wine


class WineForm(forms.ModelForm):
    class Meta:
        model = Wine
        fields = [
            'style',
            'fruit',
            'sweetness',
            'tannin',
            'body',
            'acidity',
            'alcohol']

    def __init__(self, *args, **kwargs):
        super(WineForm, self).__init__(*args, **kwargs)
        for key in self.fields:
            self.fields[key].required = False
