from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, UpdateView, ListView, DetailView, DeleteView
from .models import Event, Registration
from .forms import RegistrationForm
from django.urls import reverse_lazy


# Create your views here.

class homePage(TemplateView):
    template_name = 'eventpr/index.html'

def event(request):
    event_dict = Event.objects.all()
    context = {'events':
               event_dict}
    return render(request, 'eventpr/event.html', context)

class EventListView(ListView):
    model = Registration

    def get_queryset(self):
        queryset = Registration.objects.filter(cus_name = self.request.user) 
        return queryset  


def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            event = form.cleaned_data.get('name')

            if request.user.is_authenticated:
                if Registration.objects.filter(cus_name=request.user, name=event).exists():
                    form.add_error(None, "You are already registered for this event.")
                    return render(request, 'eventpr/registration_form.html', {'form': form})

            registration = form.save(commit=False)
            if request.user.is_authenticated:
                registration.cus_name = request.user.username
                registration.user = request.user  
            registration.save()

            return redirect('registered-events')  

    form = RegistrationForm()
    return render(request, 'eventpr/registration_form.html', {'form': form})


class EventDetailView(DetailView):
    model = Registration

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)
    
class RegistrationUpdateView(UpdateView):
    model = Registration
    success_url = reverse_lazy('registered-events')
    fields = ['cus_contact','name']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)    
    
class RegistrationDeleteView(DeleteView):
    model = Registration
    success_url = reverse_lazy('registered-events')

