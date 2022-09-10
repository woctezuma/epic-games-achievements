from src.achievements import load_achievements
from src.rankings import aggregate_ranking, export_ranking_to_csv
from src.sandboxes import load_sandbox_ids_dict
from src.trim_utils import trim_achievements, trim_sandbox_ids_dict


def main():
    sandbox_ids_dict = load_sandbox_ids_dict()
    sandbox_ids_dict = trim_sandbox_ids_dict(sandbox_ids_dict)

    achievements = load_achievements()
    achievements = trim_achievements(achievements, export_to_json=False)

    ranking = aggregate_ranking(sandbox_ids_dict, achievements)
    export_ranking_to_csv(ranking)

    return


if __name__ == "__main__":
    main()
