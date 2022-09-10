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

## Results

A ranking of games sorted by number of achievers is available [here][ranking-url].

<!-- Definitions -->

[img-cover]: <https://github.com/woctezuma/epic-games-achievements/wiki/img/cover.png>
[python-download-url]: <https://www.python.org/downloads/>
[epic-games-ratings]: <https://github.com/woctezuma/epic-games-ratings>
[colab-notebook]: <https://colab.research.google.com/github/woctezuma/epic-games-achievements/blob/colab/epic_games_achievements.ipynb>
[colab-badge]: <https://colab.research.google.com/assets/colab-badge.svg>
[ranking-url]: <data/egs_achievements.csv>
