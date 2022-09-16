from src.achievements import is_a_valid_achievement
from src.disk_utils import save_json, get_trimmed_achievements_fname
from src.products import load_slugs_dict


def trim_achievements(achievements, export_to_json=False):
    trimmed_dict = dict()

    for id, achievement in achievements.items():
        if is_a_valid_achievement(achievement):
            trimmed_dict[id] = achievement

    if export_to_json:
        save_json(trimmed_dict, get_trimmed_achievements_fname())

    return trimmed_dict


def trim_sandbox_ids_dict(sandbox_ids_dict):
    # This variable is only correct if store data was constrained to the category "games/edition/base".
    slugs_for_base_games = load_slugs_dict()

    trimmed_dict = dict()

    # NB: the sort aims to **try** to make the base edition of the game appear first. This is useful, yet not foolproof!
    for slug, sandbox_id in sorted(sandbox_ids_dict.items(), key=lambda x: (len(x[0]), x[0])):
        # NB: the check for positive length is to tackle the edge case where store data is not on the disk.
        if slug not in slugs_for_base_games and len(slugs_for_base_games) > 0:
            continue
        if sandbox_id not in trimmed_dict.values():
            s = slug.strip()
            trimmed_dict[s] = sandbox_id
        else:
            print(f"Skipping {slug}, because dict already contains id = {sandbox_id}.")

    return trimmed_dict
