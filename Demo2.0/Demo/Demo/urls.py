"""Demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from reviewsite.views import paper_list, allocate_list, review_list, allocate_detail, login_index, user_welcome, register_index, change_index, user_register, \
    paper_list, allocate_list, review_list, allocate_detail, \
    allocate_paper_jump, paper_review_list_jump, \
    paper_review_detail, review_jump_reviewer, review_list_editor,review_paper_jump_editor, review_jump_editor
from reviewsite import views


urlpatterns = [
    path('', login_index, name='login'),
    path('register/', register_index, name='register'),
    path('changePassword/', change_index, name='change'),
    path('registerResult/', user_register, name='registerResult'),
    path('welcome/', user_welcome, name='userindex'),
    path('list/', paper_list, name='list'),
    path('admin/', admin.site.urls),
    path('post/',views.post),
    path('postsubmit/',views.postsubmit),
    path('check_user/',views.check_user),
    path('check_admin/',views.check_admin),
    path('check_reviewer/',views.check_reviewer),
    path('download/',views.download),
    path('logout/',views.logout),
    path('allocate/', allocate_list, name='allocatelist'),
    path('allocatedetail/', allocate_paper_jump, name='allocatejump'),
    path('allocatecomplete/', allocate_detail, name='allocatedetail'),
    path('reviewlistexpert/', review_list, name='review'),
    path('reviewdetailexpert/', paper_review_detail, name='review'),
    path('paperlistexpert/', paper_review_list_jump, name='review'),
    path('reviewcomplete/', review_jump_reviewer, name='review'),
    path('reviewlisteditor/', review_list_editor, name='review_list_editor'),
    path('reviewdetaileditor/', review_paper_jump_editor, name='review_editor'),
    path('reviewaftereditor/', review_jump_editor, name='review_editor'),
]
