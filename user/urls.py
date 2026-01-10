from django.urls import path
from .views import (
    Signup_view, 
    Login_view, 
    dashboard_redirect_view,
    student_dashboard, 
    teacher_dashboard,
    admin_dashboard,

)

urlpatterns = [
    path('signup', Signup_view, name='signup'),
    path('', Login_view, name='login'),
    path('dashboard/', dashboard_redirect_view, name='dashboard'),
    path('dashboard/student/', student_dashboard, name='student_dashboard'),
    path('dashboard/teacher/', teacher_dashboard, name='teacher_dashboard'),
    path('dashboard/admin/', admin_dashboard, name='admin_dashboard'),

]