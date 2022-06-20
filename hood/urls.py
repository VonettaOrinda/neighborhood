from . import views
from django.urls import re_path, path,include
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    # path('', views.home, name='home'),
    # path('account/', include('django.contrib.auth.urls')),
    re_path(r'', views.home_projects, name='homePage'),
    re_path(r'search/', views.search_businesses, name='search_businesses'),
    re_path(r'^join/(\d+)', views.join, name='join'),
    re_path(r'^exit/(\d+)', views.exit, name='exit'),
    re_path(r'^image(\d+)', views.project, name='project'),
    re_path(r'^business(\d+)', views.business, name='business'),
    re_path(r'^neighbourhood/(\d+)', views.neighbourhood, name='neighbourhood'),
    re_path(r'^users/', views.user_list, name='user_list'),
    re_path(r'^new/image$', views.new_image, name='new_image'),
    re_path(r'^new/business$', views.new_business, name='new_business'),
    re_path(r'^new/project$', views.new_project, name='new_project'),
    re_path(r'^new/neighbourhood$', views.new_neighbourhood, name='new_neighbourhood'),
    re_path(r'^edit/profile$', views.edit_profile, name='edit_profile'),
    re_path(r'^profile/(?P<username>[0-9]+)$',
        views.individual_profile_page, name='individual_profile_page'),
    re_path(r'^ajax/newsletter/$', views.newsletter, name='newsletter'),
    re_path(r'^$', views.review_list, name='review_list'),
    re_path(r'^review/(?P<review_id>[0-9]+)/$',
        views.review_detail, name='review_detail'),
    re_path(r'^project$', views.project_list, name='project_list'),
    
]

# if settings.DEBUG:
#     urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

