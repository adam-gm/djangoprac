from django.urls import path
from . import views

# When reaching this url through the web browser, the HttpResponse from views.index will be sent to the web page.
# "" in path indicates that the url stops at 127.0.0.1:8000/polls/
urlpatterns = [
    # ex: /polls/
    path("", views.index, name="index"),
    # ex: /polls/5/
    path("<int:question_id>/", views.detail, name="detail"),
    # ex: /polls/5/results/
    path("<int:question_id>/results/", views.results, name="results"),
    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
]