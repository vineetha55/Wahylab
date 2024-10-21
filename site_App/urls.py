from django.urls import path
from . import views
urlpatterns=[
    path("",views.index,name="index"),
    path("about-us/",views.about_us,name="about-us"),
    path("internships/",views.internships,name="internships"),
    path("services/",views.services,name="services"),
    path("portfolio/",views.portfolio,name="portfolio"),
    path("career/",views.career,name="career"),
    path("blog/",views.blog,name="blog"),
    path("contact/",views.contact,name="contact")
]