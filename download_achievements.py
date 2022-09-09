from src.achievements import download_achievements
from src.sandboxes import load_sandbox_ids_dict


def main():
    sandbox_ids_dict = load_sandbox_ids_dict()
    sandbox_ids = set(sandbox_ids_dict.values())

    achievements = download_achievements(sandbox_ids, verbose=True)

    return


if __name__ == "__main__":
    main()
