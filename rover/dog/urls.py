from django.conf.urls import patterns, url

from dog.models import Dog, Breed, Owner
from dog.views import DogListView, DogCreate, DogSearch

urlpatterns = patterns('',
    url(r'^search/$',
        DogSearch.as_view(
            queryset=Dog.objects.prefetch_related('owner'),
            context_object_name="dog_list",
            template_name="dog/dog_list.html"
        ), name='dog-list'
    ),
    url(r'^add/$',
        DogCreate.as_view(
        ), name='dog-add'
    ),
    url(r'^$',
        DogListView.as_view(
            queryset=Dog.objects.prefetch_related('owner'),
            context_object_name="dog_list",
            template_name="dog/dog_list.html"
        ), name='dog-list'
    ),
)
