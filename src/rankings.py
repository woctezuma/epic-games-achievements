from src.disk_utils import get_ranking_fname


def aggregate_ranking(sandbox_ids_dict, achievements):
    ranking = list()

    for slug, sandbox_id in sandbox_ids_dict.items():
        try:
            achievement = achievements[sandbox_id]["achievementSets"][0]
        except KeyError:
            continue

        ranking.append(
            {
                "slug": slug,
                "id": sandbox_id,
                "num_progressed": achievement["numProgressed"],
                "num_completed": achievement["numCompleted"],
                "num_achievements": achievement["totalAchievements"],
            }
        )

    return ranking


def sort_ranking(ranking):
    return sorted(ranking, key=lambda x: x["num_progressed"], reverse=True)


def export_ranking_to_csv(ranking):
    with open(get_ranking_fname(), "w", encoding="utf8") as f:
        f.write(
            "Game slug, Number of achievers,Number of completionists, Number of achievements\n"
        )
        for entry in sort_ranking(ranking):
            f.write(
                f"{entry['slug']},{entry['num_progressed']},{entry['num_completed']},{entry['num_achievements']}\n"
            )

    return