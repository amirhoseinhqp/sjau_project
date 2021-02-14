from django import forms
from .models import reservation
class reservationform(forms.ModelForm):
    class Meta:
        model = reservation
        fields = "__all__"
