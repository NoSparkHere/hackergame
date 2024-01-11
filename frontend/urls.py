from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.HubView.as_view(), name='hub'),
    path('announcements/', views.AnnouncementsView.as_view(),
         name='announcements'),
    path('board/', views.BoardView.as_view(), name='board'),
    path('first/', views.FirstView.as_view(), name='first'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('terms/', views.TermsView.as_view(), name='terms'),
    path('user/', views.UserView.as_view()),
    path('qa/', views.QaView.as_view(), name='qa'),
    path('credits/', views.CreditsView.as_view(), name='credits'),
    path('account/', views.AccountView.as_view(), name='account'),
    path('error/', views.ErrorView.as_view()),
    path('data/core.json', views.CoreDataView.as_view(), name='coredata'),
    path('challenge/<int:challenge_id>/', views.ChallengeURLView.as_view(), name='challenge_url'),
    path('score/', views.ScoreView.as_view(), name='score'),

    # path('profile/ustc/', views.UstcProfileView.as_view(), name='ustcprofile'),

    path('accounts/', include('frontend.auth_providers.debug')),
    path('accounts/', include('frontend.auth_providers.password')),

    path('admin/announcement/', views.AnnouncementAdminView.as_view()),
    path('admin/challenge/', views.ChallengeAdminView.as_view()),
    path('admin/submission/', views.SubmissionAdminView.as_view()),
    path('admin/terms/', views.TermsAdminView.as_view()),
    path('admin/trigger/', views.TriggerAdminView.as_view()),
    path('admin/user/', views.UserAdminView.as_view()),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
