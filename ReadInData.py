import pandas as pd
import TeamStatistics as ts
from operator import itemgetter
from itertools import groupby as grpby
import numpy as np

game_stats = pd.read_csv('All_Data/09_14_game_stats.csv')
game_info = pd.read_csv('All_Data/09_14_game_info.csv')

all_stats = pd.merge(game_stats, game_info, left_on="game_id", right_on="Game_ID")

all_teams = all_stats.team.unique()

all_years = all_stats.year.unique()

all_teams = sorted(all_teams)
all_years = sorted(all_years)

print(all_teams)
print(all_years)

unc_2008 = all_stats.ix[(all_stats['team'] == 'North Carolina') & (all_stats['year'] == 2008)]

print(unc_2008)