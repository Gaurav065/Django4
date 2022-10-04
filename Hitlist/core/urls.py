from django.urls import path,include
from .views import Hitlist,HitDetails, HitCreate, HitUpdate, HitTerminate, HitterLoginView
from django.contrib.auth.views import LogoutView 

urlpatterns = [

    path("hitter_divein/", HitterLoginView.as_view(), name='Hitter_DiveIn'),
    path("hitter_diveout/", LogoutView.as_view(next_page='Hitter_DiveIn'), name="Hitter_DiveOut"),
    path('', Hitlist.as_view(), name='Hitlist'),
    path('hit/<int:pk>/', HitDetails.as_view(),name='hit'),
    path('hit_init/', HitCreate.as_view(), name='Hit_init'),
    path("hit_update/<int:pk>/", HitUpdate.as_view(), name="Hit_update"),
    path("hit_terminate/<int:pk>/", HitTerminate.as_view(), name="Hit_terminate"),
    
]