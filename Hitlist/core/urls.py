from django.urls import path,include
from .views import Hitlist,HitDetails, HitCreate, HitUpdate, HitTerminate, HitterLoginView
from django.contrib.auth.views import LogoutView as HitterLogoutView

urlpatterns = [

    path("hitter_login/", HitterLoginView.as_view(), name='Hiiter_DiveIn'),
    path("hitter_logout/", HitterLogoutView.as_view(), name="Hitter_DiveOut"),
    path('', Hitlist.as_view(), name='Hitlist'),
    path('hit/<int:pk>/', HitDetails.as_view(),name='hit'),
    path('hit_init/', HitCreate.as_view(), name='Hit_init'),
    path("hit_update/<int:pk>/", HitUpdate.as_view(), name="Hit_update"),
    path("hit_terminate/<int:pk>/", HitTerminate.as_view(), name="Hit_terminate"),
    
]