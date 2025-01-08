from django import forms
from hands.models import Hand


class PracticeForm(forms.ModelForm):
    user_name = forms.CharField(max_length=100, required=True)  # Custom field for the username

    class Meta:
        model = Hand
        fields = []


class DoneForm(forms.ModelForm):
    user_name = forms.CharField(max_length=100, required=True)  # Custom field for the username

    class Meta:
        model = Hand
        fields = []