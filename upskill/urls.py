from django.urls import path
from .views import (
    IndexView,
    Aboutview,
    Courseview,
    CourseDetail,
    ContactView,
    FeatureView,
    TeamView,
    TestView,
    SubjectCourseListView,
    CourseSearchView,
    contact_view,
)


app_name = 'upskill'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('subject/<slug:slug>/', SubjectCourseListView.as_view(), name='subject_courses'),   
    path('about/', Aboutview.as_view(), name='about'),
    path('courses/', Courseview.as_view(), name='courses'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('feature/', FeatureView.as_view(), name='feature'),
    path('teachers/', TeamView.as_view(), name='teachers'),
    path('test/', TestView.as_view(), name='test'),
    path('search/', CourseSearchView.as_view(), name='search'),
    path('course/<slug:slug>/', CourseDetail.as_view(), name='detail'),
    path('contact/', contact_view, name='contact'),
]
