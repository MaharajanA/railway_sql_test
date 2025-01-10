from django.urls import path
from .views import login_view, signup_view, dashboard_view , index_view

urlpatterns = [
    path('', index_view , name='index'),
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('dashboard/', dashboard_view, name='dashboard'),
    # path('logout/', logout, {'next_page': '/login/'}, name='logout'),
]
