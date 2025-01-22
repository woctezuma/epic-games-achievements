# Epic Games Achievements

[![Code Quality][codacy-image]][codacy]

This repository contains Python code to data-mine achievements on the Epic Games Store (EGS).

![Ranking of games sorted by number of achievers][img-cover]

## Disclaimer

> [!Note]
> As of January 22, 2025, the leak is plugged: `numProgressed` and `numCompleted` cannot be directly fetched from Epic Games anymore.

## Requirements

-   Install the latest version of [Python 3.X][python-download-url].
-   Install the required packages:

```bash
pip install -r requirements.txt
```

## Usage

First, download the `sandboxId` associated with every `pageSlug`, via [`epic-games-ratings`][epic-games-ratings].
```bash
python download_store_products.py
python download_sandbox_ids.py
```
The output is stored in:
```
data/sandbox_ids.json
```
NB: to distinguish base editions of games from DLC, it is recommended (but not mandatory) to keep a copy of:
```
data/store_data_0.json
data/store_data_1.json
```

Then, to retrieve the achievements associated with every `sandboxId`, run:
```bash
python download_achievements.py
```

Finally, to export trimmed results to JSON and CSV, run:
```bash
python export_results.py
```

Alternatively:

-   Run [`epic_games_achievements.ipynb`][colab-notebook]
[![Open In Colab][colab-badge]][colab-notebook]

## Results

A ranking of games sorted by number of players is available [here][ranking-url].

Here is a description of the headers:
- `Game slug` is the ID of the game which appears in the Epic Games store URL,
- `#players (EOS overlay)` is the number of players who have played with Epic Online Services in background,
- `#completionists` is the number of players who have acquired all the achievements for the game,
- `% of completionists` is the percentage of players who are completionists, described as "Platinum" on consoles,
- `#players (estimate)` is an estimate of the number of players based on stats about completionists,
- `#achievements` is the number of achievements of the game,
- `Max % for an achievement` is the highest unlock rate among all the achievements of the game,
- `Total XP` is the total number of experience points (XP) provided by game achievements ; [1000 XP are expected][num-xp-per-game].

### Discussion

1) some games did not have achievements on release day, or had issues with the EOS overlay,
so the number of players obtained via EOS should be considered as a lower-bound of the true number of players.

2) the percentage of completionists is rounded by Epic using one significant figure,
so our estimate of the number of players via Platinum stats should be used with caution.

3) there are bugs. For instance, Aeon Must Die has a negative number of completionists.

4) if the total XP is zero, then achievements are planned, being implemented, or the studio tried but gave up.

5) if the highest unlock rate is 0%, then achievements are most likely broken for this game.

6) the total XP is not equal to 1000 XP for [Alan Wake Remastered][alan-wake-achievements] due to exceptional DLC achievements,
for a total of 67 achievements (1500 XP) for the whole package, versus 50 achievements (1000 XP) for the base game.

7) the 100% unlock rate for an achievement (["Out of bed"][supraland-achievements]) of the game "Supraland" is not a bug: this achievement is obtained right at the start of the game.

## References

- [`MixV2/EpicResearch`][egs-api-unofficial-doc]
- [`ToutinRoger/EpicGraphQL`][egs-api-graphql]
- [`woctezuma/epic-games-ratings`][epic-games-ratings]
- [`woctezuma/epic-games-player-estimates`][epic-games-player-estimates]

<!-- Definitions -->

[img-cover]: <https://github.com/woctezuma/epic-games-achievements/wiki/img/cover.png>
[codacy]: <https://www.codacy.com/gh/woctezuma/epic-games-achievements>
[codacy-image]: <https://api.codacy.com/project/badge/Grade/e4e82c4abb6a41ef929600b668d0ebd6>
[python-download-url]: <https://www.python.org/downloads/>
[alan-wake-achievements]: <https://store.epicgames.com/achievements/alan-wake-remastered>
[num-xp-per-game]: <https://dev.epicgames.com/docs/epic-games-store/tech-features-config/epic-achievements/using-epic-achievements#xp-requirements-for-epic-games-store-achievements>
[supraland-achievements]: <https://store.steampowered.com/news/app/813630/view/3047216285009553891>
[egs-api-unofficial-doc]: <https://github.com/MixV2/EpicResearch>
[egs-api-graphql]: <https://github.com/ToutinRoger/EpicGraphQL>
[epic-games-ratings]: <https://github.com/woctezuma/epic-games-ratings>
[epic-games-player-estimates]: <https://github.com/woctezuma/epic-games-player-estimates>
[colab-notebook]: <https://colab.research.google.com/github/woctezuma/epic-games-achievements/blob/colab/epic_games_achievements.ipynb>
[colab-badge]: <https://colab.research.google.com/assets/colab-badge.svg>
[ranking-url]: <data/egs_achievements.csv>
