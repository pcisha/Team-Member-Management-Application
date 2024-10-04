from django.urls import reverse
from django.test import TestCase
from .models import TeamMember
from .forms import TeamMemberForm

# Tests for the TeamMember model. Happy path tests plus some edge cases.

class TeamMemberModelTest(TestCase):

    def setUp(self):
        TeamMember.objects.create(
            first_name='Angelina',
            last_name='Jolie',
            phone_number='9876543210',
            email='angelina.jolie@gmail.com',
            role='admin'
        )

    def test_team_member_creation(self):
        team_member = TeamMember.objects.get(email='angelina.jolie@gmail.com')
        self.assertEqual(team_member.first_name, 'Angelina')
        self.assertEqual(team_member.last_name, 'Jolie')
        self.assertEqual(team_member.phone_number, '9876543210')
        self.assertEqual(team_member.role, 'admin')

    def test_team_member_string_representation(self):
        team_member = TeamMember.objects.get(email='angelina.jolie@gmail.com')
        self.assertEqual(str(team_member), 'Angelina Jolie')


## Tests for the TeamMember views.

class TeamMemberViewTest(TestCase):

    def setUp(self):
            self.team_member = TeamMember.objects.create(
                first_name='Brad',
                last_name='Pitt',
                phone_number='9876543211',
                email='brad.pitt@gmail.com',
                role='user'
            )

    def test_team_member_list_view(self):
        response = self.client.get(reverse('team_member_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Brad Pitt')
        self.assertTemplateUsed(response, 'members/team_member_list.html')

    def test_team_member_add_view(self):
        response = self.client.get(reverse('team_member_add'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'members/team_member_add_form.html')

    def test_team_member_edit_view(self):
        response = self.client.get(reverse('team_member_edit', args=[self.team_member.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'members/team_member_edit_form.html')

    def test_team_member_delete_view(self):
        response = self.client.get(reverse('team_member_delete', args=[self.team_member.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'members/team_member_delete.html')


## Tests for the TeamMember forms.

class TeamMemberFormTest(TestCase):
    
    def test_valid_form(self):
        form_data = {
            'first_name': 'Cameron',
            'last_name': 'Diaz',
            'phone_number': '1237890456',
            'email': 'cameron.diaz@gmail.com',
            'role': 'user'
        }
        form = TeamMemberForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form_firstname(self):
        form_data = {
            'first_name': '',
            'last_name': 'Diaz',
            'phone_number': '1237890456',
            'email': 'cameron.diaz@gmail.com',
            'role': 'user'
        }
        form = TeamMemberForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 1)

    def test_invalid_form_lastname(self):
        form_data = {
            'first_name': 'Cameron',
            'last_name': '',
            'phone_number': '1237890456',
            'email': 'cameron.diaz@gmail.com',
            'role': 'user'
        }
        form = TeamMemberForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 1)

    def test_invalid_form_emailaddress(self):
        form_data = {
            'first_name': 'Cameron',
            'last_name': 'Diaz',
            'phone_number': '1237890456',
            'email': '',
            'role': 'user'
        }
        form = TeamMemberForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 1)

    def test_invalid_form_phonenumber(self):
        form_data = {
            'first_name': 'Cameron',
            'last_name': 'Diaz',
            'phone_number': '',
            'email': 'cameron.diaz@gmail.com',
            'role': 'user'
        }
        form = TeamMemberForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 1)

    def test_invalid_form_role(self):
        form_data = {
            'first_name': 'Cameron',
            'last_name': 'Diaz',
            'phone_number': '1237890456',
            'email': 'cameron.diaz@gmail.com',
            'role': ''
        }
        form = TeamMemberForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 1)
