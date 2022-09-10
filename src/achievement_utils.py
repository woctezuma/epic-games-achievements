def get_all_achievement_sets(achievement_data):
    return achievement_data["achievementSets"]


def get_base_achievement_sets(achievement_data):
    all_achievement_sets = get_all_achievement_sets(achievement_data)
    return [e for e in all_achievement_sets if e['isBase']]


def list_all_unlock_percentages(achievement_data):
    return [e['achievement']['rarity']['percent'] for e in achievement_data['achievements']]


def compute_max_unlock_percentage(achievement_data):
    rarity_list = list_all_unlock_percentages(achievement_data)

    if len(rarity_list) > 0:
        rarity = max(rarity_list)
    else:
        rarity = None

    return rarity


def extract_stats_about_achievements(achievement_data, verbose=True):
    base_achievement_sets = get_base_achievement_sets(achievement_data)
    if verbose and len(base_achievement_sets) > 1:
        print(f"Several BASE achievement sets are detected: {base_achievement_sets}")

    achievement = base_achievement_sets[0]
    achievement['rarity'] = compute_max_unlock_percentage(achievement_data)

    return achievement
