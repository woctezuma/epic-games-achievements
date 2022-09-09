# Epic Games Achievements

This repository contains Python code to data-mine achievements on the Epic Games Store (EGS).

## Requirements

-   Install the latest version of [Python 3.X][python-download-url].
-   Install the required packages:

```bash
pip install -r requirements.txt
```

## Usage

First, download the `sandboxId` associated with every `pageSlug`, via [`epic-games-ratings`][epic-games-ratings].
```
data/sandbox_ids.json
```

Then, to retrieve the achievements associated with every `sandboxId`, run:
```bash
python download_achievements.py
```

<!-- Definitions -->

[img-cover]: <https://github.com/woctezuma/epic-games-achievements/wiki/img/cover.png>
[python-download-url]: <https://www.python.org/downloads/>
[epic-games-ratings]: <https://github.com/woctezuma/epic-games-ratings>
[colab-notebook]: <https://colab.research.google.com/github/woctezuma/epic-games-achievements/blob/colab/epic_games_achievements.ipynb>
[colab-badge]: <https://colab.research.google.com/assets/colab-badge.svg>
