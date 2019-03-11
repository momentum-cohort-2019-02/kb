from django import forms
from core.models import Dog


class DogSearchForm(forms.Form):
    age = forms.MultipleChoiceField(
        choices=Dog.AGE_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=False)
    size = forms.MultipleChoiceField(
        choices=Dog.SIZE_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=False)
    energy_level = forms.MultipleChoiceField(
        choices=Dog.ENERGY_LEVEL_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=False)

    def search(self):
        dogs = Dog.objects.all()

        if self.is_valid():
            age = self.cleaned_data['age']
            size = self.cleaned_data['size']
            energy_level = self.cleaned_data['energy_level']
            if age:
                dogs = dogs.filter(age__in=age)
            if size:
                dogs = dogs.filter(size__in=size)
            if energy_level:
                dogs = dogs.filter(energy_level__in=energy_level)

        return dogs
