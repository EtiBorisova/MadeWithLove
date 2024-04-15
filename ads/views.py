from urllib import request

from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

from MadeWithLove.ads.forms import CreateAdForm
from MadeWithLove.ads.models import AdsModel



class CreateAdsView(views.CreateView):
    model = AdsModel
    form_class = CreateAdForm
    template_name = 'create_ad_page.html'
    success_url = reverse_lazy('home')


    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.seller = self.request.user
        obj.save()
        return super(CreateAdsView, self).form_valid(form)


class DetailsAdView(views.DetailView):
    model = AdsModel
    template_name = 'ad_details.html'