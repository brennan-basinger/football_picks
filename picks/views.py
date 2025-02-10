# picks/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from .models import Game, Pick, User


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('picks:home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'picks/register.html', {'form': form})


@login_required
def home(request):
    # Retrieve all games ordered by team and week.
    games = Game.objects.all().order_by('team', 'week')

    # Build a schedule dictionary: {team: {week: game, ...}, ...}
    schedule = {}
    weeks = set()
    for game in games:
        weeks.add(game.week)
        schedule.setdefault(game.team, {})[game.week] = game
    weeks = sorted(list(weeks))

    weeks = sorted(list(weeks), key=lambda week: int(week.split()[1]))

    if request.method == 'POST':
        for team, games_by_week in schedule.items():
            for week, game in games_by_week.items():
                field_name = f"game_{game.id}"
                pick_value = request.POST.get(field_name)
                if pick_value in ['W', 'L']:
                    Pick.objects.update_or_create(
                        user=request.user, game=game,
                        defaults={'pick': pick_value}
                    )
        return redirect('picks:home')

    user_picks = {pick.game.id: pick.pick for pick in Pick.objects.filter(user=request.user)}
    return render(request, 'picks/home.html', {
        'schedule': schedule,
        'weeks': weeks,
        'user_picks': user_picks,
    })


@login_required
def leaderboard(request):
    users = User.objects.all()
    leaderboard_data = []
    for user in users:
        correct_picks_count = 0
        picks = Pick.objects.filter(user=user)
        for pick in picks:
            # Only count if the game result has been entered.
            if pick.game.result and pick.pick == pick.game.result:
                correct_picks_count += 1
        leaderboard_data.append({'user': user, 'correct': correct_picks_count})
    leaderboard_data.sort(key=lambda x: x['correct'], reverse=True)
    return render(request, 'picks/leaderboard.html', {'leaderboard': leaderboard_data})

@login_required
def view_picks(request, user_id):
    other_user = get_object_or_404(User, id=user_id)
    picks = Pick.objects.filter(user=other_user)
    return render(request, 'picks/view_picks.html', {'other_user': other_user, 'picks': picks})
