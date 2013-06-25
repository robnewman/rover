# Create your views here.
# Lets use CBVs
from django.http import Http404, HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.base import TemplateResponseMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from dog.models import Dog, Owner

class BreadcrumbTemplateMixin(TemplateResponseMixin):
    """
    Generalized breadcrumb generator

    Assumes django-breadcrumbs
    """
    def render_to_response(self, context, **response_kwargs):
        allowed_ordered_breadcrumbs = ['slug']
        app_path = '/' # Start at root
        breadcrumb_list = [
            ('Dogs', '/')
        ]

        if 'search' in self.request.path:
            breadcrumb_list.append(('Search Results','/search'))
        elif 'add' in self.request.path:
            breadcrumb_list.append(('Add New Dog','/add'))
        else:
            for aob in allowed_ordered_breadcrumbs:
                if aob in self.kwargs and self.kwargs[aob]:
                    app_path += '%s/' % self.kwargs[aob]
                    title = '%s' % self.kwargs[aob].title()
                    breadcrumb_list.append((title, app_path))

        if len(breadcrumb_list) > 0:
            self.request.breadcrumbs(breadcrumb_list)

        return self.response_class(
            request = self.request,
            template = self.get_template_names(),
            context = context,
            **response_kwargs
        )

class DogSearch(BreadcrumbTemplateMixin, ListView):
    """
    Add in custom mixin and override queryset
    """
    def get_queryset(self):
        q_type = self.request.GET.get('type')
        q_name = self.request.GET.get('name')
        if 'owner' in q_type:
            q_matches = self.queryset.filter(
                owner__full_name__iexact=q_name
            )
        elif 'dog' in q_type:
            q_matches = self.queryset.filter(
                name__iexact=q_name
            )
        return q_matches

    def get_context_data(self, **kwargs):
        context = super(DogSearch, self).get_context_data(**kwargs)
        context['searchtype'] = self.request.GET.get('type')
        context['searchname'] = self.request.GET.get('name')
        self.queryset = self.get_queryset()
        return context

class DogListView(BreadcrumbTemplateMixin, ListView):
    """
    Add in custom mixin
    """
    pass

"""
Use CBV ModelForm

Notes: Currently does not work
"""
class DogCreate(BreadcrumbTemplateMixin, CreateView):
    model = Dog
    exclude = ('dogphoto', 'slug',)
    success_url = reverse_lazy('dog-list')

class DogUpdate(UpdateView):
    model = Dog

class DogDelete(DeleteView):
    model = Dog
    success_url = reverse_lazy('dog-list')
