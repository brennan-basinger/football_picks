# picks/management/commands/load_schedule_v2.py
from django.core.management.base import BaseCommand
from picks.models import Game

# Full schedule data as a list of dictionaries.
# Each dictionary contains: week, day, date, and game string.
# Note: For the row with "sss" in the original data, we convert it to week 13.
GAMES = [
    {"week": 1, "day": "Sat.", "date": "Aug 30", "game": "Alabama at Florida State"},
    {"week": 1, "day": "Sat.", "date": "Aug 30", "game": "Alabama A&M at Arkansas"},
    {"week": 1, "day": "Sat.", "date": "Aug 30", "game": "Auburn at Baylor"},
    {"week": 1, "day": "Sat.", "date": "Aug 30", "game": "Long Island at Florida"},
    {"week": 1, "day": "Sat.", "date": "Aug 30", "game": "Marshall at Georgia"},
    {"week": 1, "day": "Sat.", "date": "Aug 30", "game": "Toledo at Kentucky"},
    {"week": 1, "day": "Sat.", "date": "Aug 30", "game": "LSU at Clemson"},
    {"week": 1, "day": "Sat.", "date": "Aug 30", "game": "Georgia State at Ole Miss"},
    {"week": 1, "day": "Sat.", "date": "Aug 30", "game": "Mississippi State at Southern Miss"},
    {"week": 1, "day": "Sat.", "date": "Aug 30", "game": "Central Arkansas at Missouri"},
    {"week": 1, "day": "Sat.", "date": "Aug 30", "game": "Illinois State at Oklahoma"},
    {"week": 1, "day": "Sat.", "date": "Aug 30", "game": "Tennessee vs. Syracuse (Atlanta)"},
    {"week": 1, "day": "Sat.", "date": "Aug 30", "game": "Texas at Ohio State"},
    {"week": 1, "day": "Sat.", "date": "Aug 30", "game": "UTSA at Texas A&M"},
    {"week": 1, "day": "Sat.", "date": "Aug 30", "game": "Charleston Southern at Vanderbilt"},
    {"week": 1, "day": "Sun.", "date": "Aug 31", "game": "South Carolina vs. Virginia Tech (Atlanta)"},

    {"week": 2, "day": "Sat.", "date": "Sept. 6", "game": "UL-Monroe at Alabama"},
    {"week": 2, "day": "Sat.", "date": "Sept. 6", "game": "Arkansas State at Arkansas (Little Rock)"},
    {"week": 2, "day": "Sat.", "date": "Sept. 6", "game": "Ball State at Auburn"},
    {"week": 2, "day": "Sat.", "date": "Sept. 6", "game": "South Florida at Florida"},
    {"week": 2, "day": "Sat.", "date": "Sept. 6", "game": "Austin Peay at Georgia"},
    {"week": 2, "day": "Sat.", "date": "Sept. 6", "game": "Ole Miss at Kentucky"},
    {"week": 2, "day": "Sat.", "date": "Sept. 6", "game": "Louisiana Tech at LSU"},
    {"week": 2, "day": "Sat.", "date": "Sept. 6", "game": "Arizona State at Mississippi State"},
    {"week": 2, "day": "Sat.", "date": "Sept. 6", "game": "Kansas at Missouri"},
    {"week": 2, "day": "Sat.", "date": "Sept. 6", "game": "Michigan at Oklahoma"},
    {"week": 2, "day": "Sat.", "date": "Sept. 6", "game": "South Carolina State at South Carolina"},
    {"week": 2, "day": "Sat.", "date": "Sept. 6", "game": "East Tennessee State at Tennessee"},
    {"week": 2, "day": "Sat.", "date": "Sept. 6", "game": "San Jose State at Texas"},
    {"week": 2, "day": "Sat.", "date": "Sept. 6", "game": "Utah State at Texas A&M"},
    {"week": 2, "day": "Sat.", "date": "Sept. 6", "game": "Vanderbilt at Virginia Tech"},

    {"week": 3, "day": "Sat.", "date": "Sept. 13", "game": "Wisconsin at Alabama"},
    {"week": 3, "day": "Sat.", "date": "Sept. 13", "game": "South Alabama at Auburn"},
    {"week": 3, "day": "Sat.", "date": "Sept. 13", "game": "Eastern Michigan at Kentucky"},
    {"week": 3, "day": "Sat.", "date": "Sept. 13", "game": "Florida at LSU"},
    {"week": 3, "day": "Sat.", "date": "Sept. 13", "game": "Arkansas at Ole Miss"},
    {"week": 3, "day": "Sat.", "date": "Sept. 13", "game": "Alcorn State at Mississippi State"},
    {"week": 3, "day": "Sat.", "date": "Sept. 13", "game": "UL-Lafayette at Missouri"},
    {"week": 3, "day": "Sat.", "date": "Sept. 13", "game": "Oklahoma at Temple"},
    {"week": 3, "day": "Sat.", "date": "Sept. 13", "game": "Vanderbilt at South Carolina"},
    {"week": 3, "day": "Sat.", "date": "Sept. 13", "game": "Georgia at Tennessee"},
    {"week": 3, "day": "Sat.", "date": "Sept. 13", "game": "UTEP at Texas"},
    {"week": 3, "day": "Sat.", "date": "Sept. 13", "game": "Texas A&M at Notre Dame"},

    {"week": 4, "day": "Sat.", "date": "Sept. 20", "game": "Arkansas at Memphis"},
    {"week": 4, "day": "Sat.", "date": "Sept. 20", "game": "Florida at Miami"},
    {"week": 4, "day": "Sat.", "date": "Sept. 20", "game": "Southeastern Louisiana at LSU"},
    {"week": 4, "day": "Sat.", "date": "Sept. 20", "game": "Tulane at Ole Miss"},
    {"week": 4, "day": "Sat.", "date": "Sept. 20", "game": "Northern Illinois at Mississippi State"},
    {"week": 4, "day": "Sat.", "date": "Sept. 20", "game": "South Carolina at Missouri"},
    {"week": 4, "day": "Sat.", "date": "Sept. 20", "game": "Auburn at Oklahoma"},
    {"week": 4, "day": "Sat.", "date": "Sept. 20", "game": "UAB at Tennessee"},
    {"week": 4, "day": "Sat.", "date": "Sept. 20", "game": "Georgia State at Vanderbilt"},

    {"week": 5, "day": "Sat.", "date": "Sept. 27", "game": "Notre Dame at Arkansas"},
    {"week": 5, "day": "Sat.", "date": "Sept. 27", "game": "Alabama at Georgia"},
    {"week": 5, "day": "Sat.", "date": "Sept. 27", "game": "LSU at Ole Miss"},
    {"week": 5, "day": "Sat.", "date": "Sept. 27", "game": "Tennessee at Mississippi State"},
    {"week": 5, "day": "Sat.", "date": "Sept. 27", "game": "UMass at Missouri"},
    {"week": 5, "day": "Sat.", "date": "Sept. 27", "game": "Kentucky at South Carolina"},
    {"week": 5, "day": "Sat.", "date": "Sept. 27", "game": "Sam Houston at Texas"},
    {"week": 5, "day": "Sat.", "date": "Sept. 27", "game": "Auburn at Texas A&M"},
    {"week": 5, "day": "Sat.", "date": "Sept. 27", "game": "Utah State at Vanderbilt"},

    {"week": 6, "day": "Sat.", "date": "Oct. 4", "game": "Vanderbilt at Alabama"},
    {"week": 6, "day": "Sat.", "date": "Oct. 4", "game": "Texas at Florida"},
    {"week": 6, "day": "Sat.", "date": "Oct. 4", "game": "Kentucky at Georgia"},
    {"week": 6, "day": "Sat.", "date": "Oct. 4", "game": "Kent State at Oklahoma"},
    {"week": 6, "day": "Sat.", "date": "Oct. 4", "game": "Mississippi State at Texas A&M"},

    {"week": 7, "day": "Sat.", "date": "Oct. 11", "game": "Georgia at Auburn"},
    {"week": 7, "day": "Sat.", "date": "Oct. 11", "game": "South Carolina at LSU"},
    {"week": 7, "day": "Sat.", "date": "Oct. 11", "game": "Washington State at Ole Miss"},
    {"week": 7, "day": "Sat.", "date": "Oct. 11", "game": "Alabama at Missouri"},
    {"week": 7, "day": "Sat.", "date": "Oct. 11", "game": "Arkansas at Tennessee"},
    {"week": 7, "day": "Sat.", "date": "Oct. 11", "game": "Oklahoma vs. Texas (Dallas)"},
    {"week": 7, "day": "Sat.", "date": "Oct. 11", "game": "Florida at Texas A&M"},

    {"week": 8, "day": "Sat.", "date": "Oct. 18", "game": "Tennessee at Alabama"},
    {"week": 8, "day": "Sat.", "date": "Oct. 18", "game": "Texas A&M at Arkansas"},
    {"week": 8, "day": "Sat.", "date": "Oct. 18", "game": "Missouri at Auburn"},
    {"week": 8, "day": "Sat.", "date": "Oct. 18", "game": "Mississippi State at Florida"},
    {"week": 8, "day": "Sat.", "date": "Oct. 18", "game": "Ole Miss at Georgia"},
    {"week": 8, "day": "Sat.", "date": "Oct. 18", "game": "Texas at Kentucky"},
    {"week": 8, "day": "Sat.", "date": "Oct. 18", "game": "Oklahoma at South Carolina"},
    {"week": 8, "day": "Sat.", "date": "Oct. 18", "game": "LSU at Vanderbilt"},

    {"week": 9, "day": "Sat.", "date": "Oct. 25", "game": "Auburn at Arkansas"},
    {"week": 9, "day": "Sat.", "date": "Oct. 25", "game": "Tennessee at Kentucky"},
    {"week": 9, "day": "Sat.", "date": "Oct. 25", "game": "Texas A&M at LSU"},
    {"week": 9, "day": "Sat.", "date": "Oct. 25", "game": "Texas at Mississippi State"},
    {"week": 9, "day": "Sat.", "date": "Oct. 25", "game": "Ole Miss at Oklahoma"},
    {"week": 9, "day": "Sat.", "date": "Oct. 25", "game": "Alabama at South Carolina"},
    {"week": 9, "day": "Sat.", "date": "Oct. 25", "game": "Missouri at Vanderbilt"},

    {"week": 10, "day": "Sat.", "date": "Nov. 1", "game": "Mississippi State at Arkansas"},
    {"week": 10, "day": "Sat.", "date": "Nov. 1", "game": "Kentucky at Auburn"},
    {"week": 10, "day": "Sat.", "date": "Nov. 1", "game": "Georgia vs. Florida (Jacksonville)"},
    {"week": 10, "day": "Sat.", "date": "Nov. 1", "game": "South Carolina at Ole Miss"},
    {"week": 10, "day": "Sat.", "date": "Nov. 1", "game": "Oklahoma at Tennessee"},
    {"week": 10, "day": "Sat.", "date": "Nov. 1", "game": "Vanderbilt at Texas"},

    {"week": 11, "day": "Sat.", "date": "Nov. 8", "game": "LSU at Alabama"},
    {"week": 11, "day": "Sat.", "date": "Nov. 8", "game": "Florida at Kentucky"},
    {"week": 11, "day": "Sat.", "date": "Nov. 8", "game": "The Citadel at Ole Miss"},
    {"week": 11, "day": "Sat.", "date": "Nov. 8", "game": "Georgia at Mississippi State"},
    {"week": 11, "day": "Sat.", "date": "Nov. 8", "game": "Texas A&M at Missouri"},
    {"week": 11, "day": "Sat.", "date": "Nov. 8", "game": "Auburn at Vanderbilt"},

    {"week": 12, "day": "Sat.", "date": "Nov. 15", "game": "Oklahoma at Alabama"},
    {"week": 12, "day": "Sat.", "date": "Nov. 15", "game": "Texas at Georgia"},
    {"week": 12, "day": "Sat.", "date": "Nov. 15", "game": "Tennessee Tech at Kentucky"},
    {"week": 12, "day": "Sat.", "date": "Nov. 15", "game": "Arkansas at LSU"},
    {"week": 12, "day": "Sat.", "date": "Nov. 15", "game": "Florida at Ole Miss"},
    {"week": 12, "day": "Sat.", "date": "Nov. 15", "game": "Mississippi State at Missouri"},
    {"week": 12, "day": "Sat.", "date": "Nov. 15", "game": "New Mexico State at Tennessee"},
    {"week": 12, "day": "Sat.", "date": "Nov. 15", "game": "South Carolina at Texas A&M"},

    # The row with "sss" is converted to week 13
    {"week": 13, "day": "Sat.", "date": "Nov. 22", "game": "Eastern Illinois at Alabama"},
    {"week": 13, "day": "Sat.", "date": "Nov. 22", "game": "Mercer at Auburn"},
    {"week": 13, "day": "Sat.", "date": "Nov. 22", "game": "Tennessee at Florida"},
    {"week": 13, "day": "Sat.", "date": "Nov. 22", "game": "Charlotte at Georgia"},
    {"week": 13, "day": "Sat.", "date": "Nov. 22", "game": "Western Kentucky at LSU"},
    {"week": 13, "day": "Sat.", "date": "Nov. 22", "game": "Missouri at Oklahoma"},
    {"week": 13, "day": "Sat.", "date": "Nov. 22", "game": "Coastal Carolina at South Carolina"},
    {"week": 13, "day": "Sat.", "date": "Nov. 22", "game": "Arkansas at Texas"},
    {"week": 13, "day": "Sat.", "date": "Nov. 22", "game": "Samford at Texas A&M"},
    {"week": 13, "day": "Sat.", "date": "Nov. 22", "game": "Kentucky at Vanderbilt"},

    {"week": 14, "day": "Sat.", "date": "Nov. 29", "game": "Missouri at Arkansas"},
    {"week": 14, "day": "Sat.", "date": "Nov. 29", "game": "Alabama at Auburn"},
    {"week": 14, "day": "Sat.", "date": "Nov. 29", "game": "Florida State at Florida"},
    {"week": 14, "day": "Sat.", "date": "Nov. 29", "game": "Georgia vs. Georgia Tech (Atlanta)"},
    {"week": 14, "day": "Sat.", "date": "Nov. 29", "game": "Kentucky at Louisville"},
    {"week": 14, "day": "Sat.", "date": "Nov. 29", "game": "Ole Miss at Mississippi State"},
    {"week": 14, "day": "Sat.", "date": "Nov. 29", "game": "LSU at Oklahoma"},
    {"week": 14, "day": "Sat.", "date": "Nov. 29", "game": "Clemson at South Carolina"},
    {"week": 14, "day": "Sat.", "date": "Nov. 29", "game": "Vanderbilt at Tennessee"},
    {"week": 14, "day": "Sat.", "date": "Nov. 29", "game": "Texas A&M at Texas"},
]


class Command(BaseCommand):
    help = "Load the full football schedule with home/away info into the database."

    def handle(self, *args, **options):
        # Remove any existing schedule entries.
        Game.objects.all().delete()
        for entry in GAMES:
            game_str = entry["game"]
            date = entry["date"]
            # Determine home/away based on the game string.
            # We assume:
            #   " at " indicates an away game (the team is traveling),
            #   " vs. " indicates a home game.
            if " at " in game_str:
                team, opponent = game_str.split(" at ", 1)
                is_home = False
            elif " vs. " in game_str:
                team, opponent = game_str.split(" vs. ", 1)
                is_home = True
            else:
                # If the format is not recognized, skip this entry.
                continue

            Game.objects.create(
                team=team.strip(),
                date=date,
                opponent=opponent.strip(),
                is_home=is_home
            )
        self.stdout.write(self.style.SUCCESS("Schedule loaded successfully."))
