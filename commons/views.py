from django.shortcuts import render
from django.views import generic as views

from MadeWithLove.accounts.models import MadeWithLoveUser
from MadeWithLove.ads.models import AdsModel
from MadeWithLove.commons.forms import SearchForm


def searchbar_view(request):
    search_form = SearchForm()
    context = {
        'search_form': search_form
    }
    return render(request, 'base.html', context)


class HomePage(views.ListView):
    model = AdsModel
    template_name = 'home_page.html'
    paginate_by = 10


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        search_form = SearchForm()
        context['search_form'] = search_form
        context['user'] = user
        return context
