from django.shortcuts import render
from django.http import JsonResponse
from .models import Matches, Deliveries
from django.db.models import Count, Sum

from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import MatchesSerializer, DeliveriesSerializer
from .models import Matches, Deliveries

# def matches_per_year_view(request):
#     matches_per_year = Matches.objects.values('season').annotate(matches=Count('season')).order_by('season')

#     chart_data = [['Season', 'Matches']]
#     for match in matches_per_year:
#         chart_data.append([match['season'], match['matches']])
#     return JsonResponse(chart_data, safe=False)

# def landing_view(request):
#     return render(request, 'landing.html')

# class MatchesPerYearView(APIView):
#     # def get(self, request, format=None):
#     #     matches_per_year = Matches.objects.values('season').annotate(matches=Count('season')).order_by('season')
#     #     serializer = MatchesSerializer(matches_per_year, many=True)
#     #     return Response(serializer.data)
#     def matches_per_year_view(request):
#         if request.method == 'GET':
#             matches_per_year = Matches.objects.values('season').annotate(matches=Count('season')).order_by('season')

#             chart_data = [['Season', 'Matches']]
#             for match in matches_per_year:
#                 chart_data.append([match['season'], match['matches']])
        
#             return JsonResponse(chart_data, safe=False)


def matches_per_year(request):
    data = Matches.objects.values('season').annotate(matches=Count('season')).order_by('season')
    return JsonResponse(list(data), safe=False)

def matches_won_by_teams(request):
    # Retrieve all matches from the database
    matches = Matches.objects.all()
    
    # Create a dictionary to store the number of matches won by each team
    teams_won = {}
    
    # Iterate over each match and count the number of wins for each team
    for match in matches:
        winner = match.winner
        if winner in teams_won:
            teams_won[winner] += 1
        else:
            teams_won[winner] = 1
    
    # Prepare the data in the desired format
    data = [{'team': team, 'matches_won': count} for team, count in teams_won.items()]
    
    # Return the data as a JSON response
    return JsonResponse(data, safe=False)

def extra_runs_conceded(request):
    if request.method == 'POST':
        year = request.POST.get('year')
        # extra_runs = Deliveries.objects.filter(season=year).values('bowling_team').annotate(total_extra_runs=Sum('extra_runs')).order_by('-total_extra_runs')
        extra_runs = Deliveries.objects.filter(_id_id__season=year).values('bowling_team').annotate(total_extra_runs=Sum('extra_runs')).order_by('-total_extra_runs')
        return render(request, 'extra_runs.html', {'extra_runs': extra_runs, 'year': year})
    return render(request, 'form.html')

def top_economical_bowlers(request):
    if request.method == 'POST':
        year = request.POST.get('year')
        economical_bowlers = Deliveries.objects.filter(season=year).values('bowler').annotate(economy_rate=Sum('total_runs') / Sum('overs')).order_by('economy_rate')[:10]
        return render(request, 'economical_bowlers.html', {'economical_bowlers': economical_bowlers, 'year': year})
    return render(request, 'form.html')

def matches_played_vs_won(request):
    if request.method == 'POST':
        year = request.POST.get('year')
        matches_played = Matches.objects.filter(season=year).values('team1').annotate(total_matches=Sum(1))
        matches_won = Matches.objects.filter(season=year).values('winner').annotate(total_wins=Sum(1))
        return render(request, 'matches_played_vs_won.html', {'matches_played': matches_played, 'matches_won': matches_won, 'year': year})
    return render(request, 'form.html')