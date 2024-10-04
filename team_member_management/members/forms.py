from django import forms
from .models import TeamMember

# Create form for TeamMember.

class TeamMemberForm(forms.ModelForm):
    class Meta:
        model = TeamMember
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'role']
