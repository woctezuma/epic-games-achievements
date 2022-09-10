from src.achievement_utils import extract_stats_about_achievements
from src.disk_utils import get_ranking_fname
from src.player_utils import estimate_num_players


def aggregate_ranking(sandbox_ids_dict, achievements):
    ranking = list()

    for slug, sandbox_id in sandbox_ids_dict.items():
        try:
            achievement_data = achievements[sandbox_id]
        except KeyError:
            continue

        achievement = extract_stats_about_achievements(achievement_data)

        ranking.append(
            {
                "slug": slug,
                "id": sandbox_id,
                "num_progressed": achievement["numProgressed"],
                "num_completed": achievement["numCompleted"],
                "num_achievements": achievement["totalAchievements"],
                "total_xp": achievement["totalXP"],
                "rarity": achievement['rarity'],
                "platinum_rarity": achievement['platinumRarity'],
                "estimated_num_players": estimate_num_players(achievement["numCompleted"],
                                                              achievement['platinumRarity'])
            }
        )

    return ranking


def sort_ranking(ranking):
    return sorted(ranking, key=lambda x: x["num_progressed"], reverse=True)


def export_ranking_to_csv(ranking):
    with open(get_ranking_fname(), "w", encoding="utf8") as f:
        f.write(
            "Game slug, Number of achievers,Number of completionists, Number of achievements, Total XP, Max unlock percentage, Platinum completion percentage, Estimated number of players\n"
        )
        for entry in sort_ranking(ranking):
            f.write(
                f"{entry['slug']},{entry['num_progressed']},{entry['num_completed']},{entry['num_achievements']},{entry['total_xp']},{entry['rarity']},{entry['platinum_rarity']},{entry['estimated_num_players']}\n"
            )

    return
