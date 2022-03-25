from django.urls import path
from artyParty import views
from django.views.generic import TemplateView

app_name = 'arty'

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.user_login, name='login'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('about/', views.about, name='about'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('my_account/', views.my_account, name='my_account'),
    path('my_account/add_piece/', views.add_piece, name='add_piece'),
    path('my_account/add_gallery/', views.add_gallery, name='add_gallery'),
    path('my_account/manage_users/', views.manage_users, name='manage_users'),
    path('my_account/edit_details/', views.edit_details, name='edit_details'),
    path('my_account/posts/', views.posts, name='posts'),
    path('galleries/', views.galleries, name='galleries'),
    path('galleries/<slug:gallery_name_slug>/', views.show_gallery, name='show_gallery'),
    path('galleries/<slug:gallery_name_slug>/<slug:piece_name_slug>/', views.piece, name='piece'),
    path('galleries/<slug:gallery_name_slug>/<slug:piece_name_slug>/<slug:review_name_slug>/', views.show_review, name='show_review'),
]