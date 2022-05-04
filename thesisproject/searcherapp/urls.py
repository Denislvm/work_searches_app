from .views import *
from django.urls import path

urlpatterns = [
    path('', VacancyHome.as_view(), name='home'),
    path('about/', About.as_view(), name='about'),
    path('contact/', ContactFormView.as_view(), name='contact'),
    path('startup/', StartupHome.as_view(), name='startup'),
    path('startup_post/<slug:startup_slug>/', ShowStartup.as_view(), name='startup_post'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('addpage/', AddPage.as_view(), name='addpage'),
    path('add_startup/', AddStartup.as_view(), name='add_startup'),
    path('post/<slug:post_slug>', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', VacancyCategory.as_view(), name='category'),
    path('register/', RegisterUser.as_view(), name='register'),
]