from src.achievements import is_a_valid_achievement
from src.disk_utils import save_json, get_trimmed_achievements_fname


def trim_achievements(achievements, export_to_json=False):
    trimmed_dict = dict()

    for id, achievement in achievements.items():
        if is_a_valid_achievement(achievement):
            trimmed_dict[id] = achievement

    if export_to_json:
        save_json(trimmed_dict, get_trimmed_achievements_fname())

    return trimmed_dict
