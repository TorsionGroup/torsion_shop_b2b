from django.views.generic import ListView, DetailView
from .models import *


class ContactsView(ListView):
    model = Contact
    queryset = Contact.objects.all()
    context_object_name = 'contacts_list'
    template_name = 'oscar/contacts/contacts.html'