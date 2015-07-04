from django.forms import ModelForm
from .models import UserSchedule

class UserScheduleForm(ModelForm):
    class Meta:
        model = UserSchedule
        exclude = ['week', 'user']
    