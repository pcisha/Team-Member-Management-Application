from django.http import Http404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import TeamMember
from .forms import TeamMemberForm
import logging

# Add views for listing, adding, editing and deleting team members.


logger = logging.getLogger('members')


# Endpoint URL: GET http://{domain}/members/
# Example: http://127.0.0.1:8000/members/
# List of all team members
class TeamMemberListView(ListView):
    model = TeamMember
    template_name = 'members/team_member_list.html'
    context_object_name = 'team_members'

    def dispatch(self, request, *args, **kwargs):
        count = TeamMember.objects.count()
        logger.info("\nDisplaying the list of all %d team members.", count)
        return super().dispatch(request, *args, **kwargs)



# Endpoint URL: POST http://{domain}/members/add/
# Add a new team member
class TeamMemberCreateView(CreateView):
    model = TeamMember
    form_class = TeamMemberForm
    template_name = 'members/team_member_add_form.html'
    success_url = reverse_lazy('team_member_list')

    def form_valid(self, form):
        http_response = super().form_valid(form)
        new_team_member = form.instance  # Access the newly created member object
        logger.info("\nSuccessfully created a new TeamMember with ID: %d and Name: %s %s",
            new_team_member.id, new_team_member.first_name, new_team_member.last_name)     # Log the ID and name of the new member
        return http_response

    def form_invalid(self, form):
        error_messages = ', '.join(f"{field}: {errors}" for field, errors in form.errors.items())
        logger.error("\nUnable to create a new TeamMember.", error_messages)     # Log the error when form is invalid
        return super().form_invalid(form)



# Endpoint URL: POST http://{domain}/members/{pk}/edit
# where, pk is an integer that uniquely identifies the team member
# Update the details of an existing team member
class TeamMemberEditView(UpdateView):
    model = TeamMember
    form_class = TeamMemberForm
    template_name = 'members/team_member_edit_form.html'
    success_url = reverse_lazy('team_member_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        edited_member = form.instance
        logger.info("\nSuccessfully edited the TeamMember with ID: %d and Name: %s %s",
                    edited_member.id, edited_member.first_name, edited_member.last_name)
        return response


# Endpoint URL: POdT http://{domain}/members/{pk}/delete
# where, pk is an integer that uniquely identifies the team member
# Delete an existing team member
class TeamMemberDeleteView(DeleteView):
    model = TeamMember
    template_name = 'members/team_member_delete.html'
    success_url = reverse_lazy('team_member_list')

    def delete(self, request, *args, **kwargs):
        team_member = self.get_object()
        logger.info("\nSuccessfully deleted the TeamMember with ID: %d and Name: %s %s",
                    team_member.id, team_member.first_name, team_member.last_name)
        http_response = super().delete(request, *args, **kwargs)
        return http_response



def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        try:
            member = get_object_or_404(TeamMember, pk=pk)
        except Http404:
            logger.error("\nTeamMember with ID=%d not found.", pk)
            raise  # 404 response should be returned
        return member