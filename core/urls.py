from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'viewallusers/',views.ViewAllUsers.as_view()),
    url(r'get10usersfromapi/',views.Get10UsersFromAPI.as_view()),
    url(r'deleteallusers/',views.DeleteAllUsers.as_view()),
    url(r'deletegivenuser/(?P<id>\d+)/',views.DeleteGivenUser.as_view()),
    url(r'getgivenuser/(?P<user_id>\d+)/',views.GetGivenUser.as_view()),
    url(r'postuser/',views.PostUser.as_view()),
    url(r'',views.home),
    
]