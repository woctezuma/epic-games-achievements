def estimate_num_players(num_completionists, platinum_rarity):
    if platinum_rarity == 0:
        num_players = 'N/A'
    else:
        platinum_completion_percentage = platinum_rarity / 100
        num_players = int(num_completionists / platinum_completion_percentage)
    return num_players
