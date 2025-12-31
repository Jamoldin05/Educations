from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView,DetailView,ListView
from .models import Subject,Course,Teacher
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm



def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            send_mail(
                subject=f"Yangi xabar: {name}",
                message=f"Email: {email}\n\nXabar:\n{message}",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[settings.EMAIL_HOST_USER],  
            )
            return redirect('success')
    else:
        form = ContactForm()

    return render(request, 'upskill/contact.html', {'form': form})



class BaseContextMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['courses'] = Course.objects.all()  
        context['teachers'] = Teacher.objects.filter(is_active=True)  
        context['subjects'] = Subject.objects.all()
        return context
    


class IndexView(BaseContextMixin, TemplateView):
    template_name = 'upskill/index.html'


class Aboutview(BaseContextMixin, TemplateView):
    template_name = 'upskill/about.html'


class Courseview(BaseContextMixin, TemplateView):
    template_name = 'upskill/course.html'


class TeamView(BaseContextMixin, TemplateView):
    template_name = 'upskill/team.html'


class TestView(BaseContextMixin, TemplateView):
    template_name = 'upskill/testimonial.html'


class ContactView(BaseContextMixin, TemplateView):  
    template_name = 'upskill/contact.html'


class FeatureView(BaseContextMixin, TemplateView):  
    template_name = 'upskill/feature.html'


class SubjectCourseListView(BaseContextMixin, ListView):
    model = Course
    template_name = 'upskill/subject.html'
    context_object_name = 'courses'

    def get_queryset(self):
        self.subject = get_object_or_404(Subject, slug=self.kwargs['slug'])
        return Course.objects.filter(subject=self.subject)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subject'] = self.subject
        return context


class CourseDetail(BaseContextMixin, DetailView):
    model = Course
    template_name = 'upskill/detail.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'



class CourseSearchView(ListView):
    model = Course
    template_name = 'upskill/search.html'
    context_object_name = 'courses'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Course.objects.filter(title__icontains=query)
        return Course.objects.none()
    



