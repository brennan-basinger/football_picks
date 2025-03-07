# picks/templatetags/picks_extras.py
from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

@register.simple_tag
def game_marker(team, week):
    """
    Returns '@' if the game is away and 'vs' if the game is at home.
    Adjust the mapping below based on your known schedule.
    For example, here’s a sample mapping for Alabama.
    """

    # Georgia's schedule is wrong?

    # Double check load_schedule.py against actual schedule then continue
    # mapping vs and @ 

    mapping = {
        'Alabama': {
            'Week 1': '@',
            'Week 2': 'vs',
            'Week 3': 'vs',
            'Week 4': '',
            'Week 5': '@',
            'Week 6': 'vs',
            'Week 7': '@',
            'Week 8': 'vs',
            'Week 9': '@',
            'Week 10': '',
            'Week 11': 'vs',
            'Week 12': 'vs',
            'Week 13': 'vs',
            'Week 14': '@',
        },

        'Arkansas': {
            'Week 1': 'vs',
            'Week 2': 'vs',
            'Week 3': '@',
            'Week 4': '@',
            'Week 5': 'vs',
            'Week 6': '',
            'Week 7': '@',
            'Week 8': 'vs',
            'Week 9': 'vs',
            'Week 10': 'vs',
            'Week 11': '',
            'Week 12': '@',
            'Week 13': '@',
            'Week 14': 'vs',
        },

        'Auburn': {
            'Week 1': '@',
            'Week 2': 'vs',
            'Week 3': 'vs',
            'Week 4': '@',
            'Week 5': '@',
            'Week 6': '',
            'Week 7': 'vs',
            'Week 8': 'vs',
            'Week 9': '',
            'Week 10': 'vs',
            'Week 11': '@',
            'Week 12': '',
            'Week 13': 'vs',
            'Week 14': '',
        },

        'Florida': {
            'Week 1': 'vs',
            'Week 2': 'vs',
            'Week 3': '@',
            'Week 4': '@',
            'Week 5': '',
            'Week 6': 'vs',
            'Week 7': '@',
            'Week 8': 'vs',
            'Week 9': '',
            'Week 10': 'vs',
            'Week 11': '@',
            'Week 12': '@',
            'Week 13': 'vs',
            'Week 14': 'vs',
        },

        'Georgia': {
            'Week 1': 'vs',
            'Week 2': 'vs',
            'Week 3': '@',
            'Week 4': '',
            'Week 5': '',
            'Week 6': 'vs',
            'Week 7': '',
            'Week 8': 'vs',
            'Week 9': '',
            'Week 10': '',
            'Week 11': '@',
            'Week 12': 'vs',
            'Week 13': 'vs',
            'Week 14': '@',
        },

        'Kentucky': {
            'Week 1': 'vs',
            'Week 2': 'vs',
            'Week 3': 'vs',
            'Week 4': '',
            'Week 5': '@',
            'Week 6': '',
            'Week 7': '',
            'Week 8': 'vs',
            'Week 9': 'vs',
            'Week 10': '',
            'Week 11': '',
            'Week 12': 'vs',
            'Week 13': '@',
            'Week 14': '@',
        },

        'LSU': {
            'Week 1': '@',
            'Week 2': 'vs',
            'Week 3': '',
            'Week 4': 'vs',
            'Week 5': '@',
            'Week 6': '',
            'Week 7': 'vs',
            'Week 8': '@',
            'Week 9': 'vs',
            'Week 10': '',
            'Week 11': '',
            'Week 12': '',
            'Week 13': 'vs',
            'Week 14': '@',
        },

        'Mississippi State': {
            'Week 1': '@',
            'Week 2': 'vs',
            'Week 3': 'vs',
            'Week 4': 'vs',
            'Week 5': 'vs',
            'Week 6': '@',
            'Week 7': '',
            'Week 8': '',
            'Week 9': 'vs',
            'Week 10': '',
            'Week 11': '',
            'Week 12': '@',
            'Week 13': '',
            'Week 14': '',
        },

        'Missouri': {
            'Week 1': 'vs',
            'Week 2': 'vs',
            'Week 3': 'vs',
            'Week 4': 'vs',
            'Week 5': 'vs',
            'Week 6': '',
            'Week 7': '',
            'Week 8': '',
            'Week 9': '@',
            'Week 10': '',
            'Week 11': 'vs',
            'Week 12': '',
            'Week 13': '@',
            'Week 14': '',
        },

        'Oklahoma': {
            'Week 1': 'vs',
            'Week 2': 'vs',
            'Week 3': '@',
            'Week 4': '',
            'Week 5': '',
            'Week 6': 'vs',
            'Week 7': '@',
            'Week 8': '@',
            'Week 9': '',
            'Week 10': '@',
            'Week 11': '',
            'Week 12': '',
            'Week 13': '',
            'Week 14': '',
        },

        'Ole Miss': {
            'Week 1': 'vs',
            'Week 2': '',
            'Week 3': '',
            'Week 4': 'vs',
            'Week 5': '',
            'Week 6': '',
            'Week 7': 'vs',
            'Week 8': '',
            'Week 9': '@',
            'Week 10': 'vs',
            'Week 11': 'vs',
            'Week 12': '',
            'Week 13': '',
            'Week 14': '@',
        },

        'South Carolina': {
            'Week 1': '@',
            'Week 2': 'vs',
            'Week 3': 'vs',
            'Week 4': '',
            'Week 5': '',
            'Week 6': '',
            'Week 7': '',
            'Week 8': '',
            'Week 9': '',
            'Week 10': '',
            'Week 11': '',
            'Week 12': '@',
            'Week 13': 'vs',
            'Week 14': 'vs',
        },

        'Tennessee': {
            'Week 1': '@',
            'Week 2': 'vs',
            'Week 3': '',
            'Week 4': 'vs',
            'Week 5': '',
            'Week 6': '',
            'Week 7': '',
            'Week 8': '',
            'Week 9': '',
            'Week 10': '',
            'Week 11': '',
            'Week 12': 'vs',
            'Week 13': '',
            'Week 14': 'vs',
        },

        'Texas': {
            'Week 1': '@',
            'Week 2': 'vs',
            'Week 3': 'vs',
            'Week 4': '',
            'Week 5': 'vs',
            'Week 6': '',
            'Week 7': '',
            'Week 8': '',
            'Week 9': '',
            'Week 10': 'vs',
            'Week 11': '',
            'Week 12': '',
            'Week 13': '',
            'Week 14': 'vs',
        },

        'Texas A&M': {
            'Week 1': 'vs',
            'Week 2': 'vs',
            'Week 3': '@',
            'Week 4': '',
            'Week 5': '',
            'Week 6': '',
            'Week 7': '',
            'Week 8': '',
            'Week 9': '',
            'Week 10': '',
            'Week 11': '',
            'Week 12': '',
            'Week 13': 'vs',
            'Week 14': '',
        },

        'Vanderbilt': {
            'Week 1': 'vs',
            'Week 2': '@',
            'Week 3': '',
            'Week 4': 'vs',
            'Week 5': 'vs',
            'Week 6': '',
            'Week 7': '',
            'Week 8': '',
            'Week 9': '',
            'Week 10': '',
            'Week 11': '',
            'Week 12': '',
            'Week 13': '',
            'Week 14': '',
        },

    }


    # Default to "vs" if no mapping exists for the team and week.
    return mapping.get(team, {}).get(week, 'vs')