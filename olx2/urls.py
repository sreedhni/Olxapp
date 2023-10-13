from django.urls import path
from olx2.views import SignUpView,SignInView,OlxCreateView,OlxListView,OlxUpdateView

urlpatterns=[path("signup/",SignUpView.as_view(),name="signup"),
             path("signin/",SignInView.as_view(),name="signin"),
             path("add/",OlxCreateView.as_view(),name="olx-add"),
             path("list/",OlxListView.as_view(),name="olx-list"),
             path("<int:pk>/change/",OlxUpdateView.as_view(),name="olx-change")

             ]