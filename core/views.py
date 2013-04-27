# core/views.py
from django.views.generic import FormView, TemplateView
from .forms import ContactForm

class AboutView(TemplateView):
    template_name = "core/about.html"


class ThanksView(TemplateView):
    template_name = "core/thanks.html"


class ContactView(FormView):
    template_name = "core/contact.html"
    form_class = ContactForm
    success_url = '/thanks/'

    def form_valid(self, form):
        # form.send_email()
        return super(ContactView, self).form_valid(form)
