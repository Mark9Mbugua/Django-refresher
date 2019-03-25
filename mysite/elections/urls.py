from django.urls import path
from . import views

app_name = 'elections'
urlpatterns = [
    # /elections/
    path('', views.index, name='index'),
    # /elections/2/
    path('<int:question_id>/', views.detail, name='detail'),
    # /elections/2/results
    path('<int:question_id>/results/', views.results, name='results'),
    # /elections/2/vote
    path('<int:question_id>/vote/', views.vote, name='vote'),

]