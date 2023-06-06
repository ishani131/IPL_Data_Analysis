"""
URL configuration for IPL_Data_Analysis project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import include,path
from IPL_API import views
from IPL_API.views import matches_per_year, matches_won_by_teams, extra_runs_conceded, top_economical_bowlers, matches_played_vs_won

urlpatterns = [
    # path('api/', matches_per_year),
    # path('admin/', admin.site.urls),
    # path('', landing_view, name='landing-page'),
    # path('api/matches/', matches_per_year_view, name='match-list'),
    path('matches/', matches_per_year, name='matches-per-year'),
    path('matches/won/', matches_won_by_teams, name='matches-won-by-teams'),
    path('extra_runs/', extra_runs_conceded, name='extra_runs'),
    path('economical_bowlers/', top_economical_bowlers, name='economical_bowlers'),
    path('matches_played_vs_won/', matches_played_vs_won, name='matches_played_vs_won'),
]
