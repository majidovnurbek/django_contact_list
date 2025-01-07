from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView, ListView
from django.shortcuts import render


from .models import Person, Job


def index(request):
    posts = Person.objects.all()
    return render(request,'contact.html', {'posts': posts})


class HomeDeleteView(DeleteView):
    model = Person
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('contact_list')

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)