from src.disk_utils import save_json, get_achievements_fname, load_json
from src.query_achievement import to_achievement


def has_a_valid_field_value(dictionary, keyword):
    return bool(keyword in dictionary and dictionary[keyword] is not None)


def is_a_valid_achievement(achievement):
    is_valid = (
        bool(achievement is not None)
        and has_a_valid_field_value(achievement, "achievementSets")
        and len(achievement["achievementSets"]) > 0
    )

    return is_valid


def download_achievements(sandbox_ids, save_every=60, verbose=True):
    achievements = load_achievements()

    for iter, id in enumerate(sandbox_ids, start=1):
        if id in achievements and is_a_valid_achievement(achievements[id]):
            continue

        achievement = to_achievement(id, verbose=verbose)

        if verbose and achievement is not None:
            print(f"{id} -> {achievement}")

        achievements[id] = achievement

        if iter % save_every == 0:
            save_json(achievements, get_achievements_fname())
            if verbose:
                print(f"Saving {iter}/{len(sandbox_ids)}")

    save_json(achievements, get_achievements_fname())
    if verbose:
        print(f"Finally saving {iter}/{len(sandbox_ids)}")

    return achievements


def load_achievements():
    try:
        achievements = load_json(get_achievements_fname())
    except FileNotFoundError:
        achievements = dict()
    return achievements
