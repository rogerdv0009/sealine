
from django.views.generic import TemplateView

from apps.promotions.models import Promotion
from apps.services.models import Service
from apps.tours.models import Tour
from apps.news.models import New
from apps.testimonials.models import Testimonial
from apps.ticket.forms import Ticket_IndexForm
# Create your views here.

class MainView(TemplateView):
    template_name = "index.html"

    def getServices(self):
        cont = Service.objects.filter(state=True).count()
        services = None
        if cont:
            if cont > 0 and cont < 4:
                services = Service.objects.filter(state=True)
            else:
                services = Service.objects.filter(state=True)[:4]
        return services

    def getPromotions(self):
        cont = Promotion.objects.filter(state=True).count()
        promotions = None
        if cont:
            if cont > 0 and cont < 3:
                promotions = Promotion.objects.filter(state=True)
            else:
                promotions = Promotion.objects.filter(state=True)[:3]
        return promotions

    def getTours(self):
        cont = Tour.objects.filter(state=True).count()
        tours = None
        if cont:
            if cont > 0 and cont < 6:
                tours = Tour.objects.filter(state=True)
            else:
                tours = Tour.objects.filter(state=True)[:6]
        return tours

    def getNews(self):
        cont = New.objects.filter(state=True).count()
        news = None
        if cont:
            if cont > 0 and cont < 3:
                news = New.objects.filter(state=True)
            else:
                news = New.objects.filter(state=True)[:3]
        return news

    def getTestimonials(self):
        cont = Testimonial.objects.filter(state=True).count()
        testimonials = None
        if cont:
            if cont > 0 and cont < 3:
                testimonials = Testimonial.objects.filter(state=True)
            else:
                testimonials = Testimonial.objects.filter(state=True)[:3]
        return testimonials

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["promotions"] = self.getPromotions()
        context["tours"] = self.getTours()
        context["services"] = self.getServices()
        context["news"] = self.getNews()
        context["testimonials"] = self.getTestimonials()
        context["formulario"] = Ticket_IndexForm
        return context
