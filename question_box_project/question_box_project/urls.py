"""question_box_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
from rest_framework import routers
from question_box_app import views
from django.contrib.auth import views as auth_views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'questions', views.QuestionViewSet)
router.register(r'answers', views.AnswerViewSet)
router.register(r'question_comments', views.QuestionCommentViewSet)
router.register(r'answer_comments', views.AnswerCommentViewSet)
router.register(r'tags', views.TagViewSet)
router.register(r'question_votes', views.QuestionVoteViewSet)
router.register(r'answer_votes', views.AnswerVoteViewSet)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^index/', views.index),
    url(r'^profile/(?P<user_id>[0-9]+)', views.profile),
    url(r'^question_detail/(?P<question_id>[0-9]+)', views.question_detail),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'signup/$', views.signup, name='signup'),
    url(r'logout/$', auth_views.logout, name='logout'),
]
