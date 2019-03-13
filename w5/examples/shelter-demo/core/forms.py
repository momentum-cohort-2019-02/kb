from django import forms
from core.models import Dog, AdoptionApplication


class SearchForm(forms.Form):
    age = forms.ChoiceField(
        label="Age",
        widget=forms.widgets.RadioSelect,
        choices=((None, "Any age"),) + Dog.AGE_CHOICES,
        required=False)
    size = forms.MultipleChoiceField(
        widget=forms.widgets.CheckboxSelectMultiple,
        label="Size",
        choices=Dog.SIZE_CHOICES,
        required=False)
    good_with_kids = forms.BooleanField(
        label="Good with kids", required=False, label_suffix="")
    good_with_dogs = forms.BooleanField(
        label="Good with other dogs", required=False, label_suffix="")
    good_with_cats = forms.BooleanField(
        label="Good with cats", required=False, label_suffix="")

    def search(self):
        if not self.is_valid():
            return None

        data = self.cleaned_data
        dogs = Dog.objects.all()
        if data['age']:
            dogs = dogs.filter(age=data['age'])
        if data['size']:
            dogs = dogs.filter(size__in=data['size'])
        if data['good_with_kids']:
            dogs = dogs.filter(good_with_kids=True)
        if data['good_with_dogs']:
            dogs = dogs.filter(good_with_dogs=True)
        if data['good_with_cats']:
            dogs = dogs.filter(good_with_cats=True)
        return dogs


class AdoptionApplicationForm(forms.ModelForm):

    class Meta:
        model = AdoptionApplication
        exclude = ['applicant']
        widgets = {'dog': forms.HiddenInput()}
