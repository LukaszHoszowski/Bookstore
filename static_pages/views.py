from django.views import generic


class AboutView(generic.TemplateView):
    template_name = "static_pages/about.html"