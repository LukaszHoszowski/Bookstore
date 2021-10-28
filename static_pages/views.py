from django.views import generic


class LogoutView(generic.TemplateView):
    template_name = "static_pages/about.html"