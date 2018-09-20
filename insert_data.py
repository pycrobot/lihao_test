"""如果无法直接向数据库中导入csv，可以使用在manage.py shell执行以下代码，手动添加"""

import pandas as pd

from searchdata.models import FIFARanking

data = pd.read_csv('fifa_ranking.csv')

for i in range(data.shape[0]):
    item = FIFARanking(
        rank=data.iloc[i, 0],
        country_full=data.iloc[i, 1],
        country_abrv=data.iloc[i, 2],
        total_points=data.iloc[i, 3],
        previous_points=data.iloc[i, 4],
        rank_change=data.iloc[i, 5],
        cur_year_avg=data.iloc[i, 6],
        cur_year_avg_weighted=data.iloc[i, 7],
        last_year_avg=data.iloc[i, 8],
        last_year_avg_weighted=data.iloc[i, 9],
        two_year_ago_avg=data.iloc[i, 10],
        two_year_ago_weighted=data.iloc[i, 11],
        three_year_ago_avg=data.iloc[i, 12],
        three_year_ago_weighted=data.iloc[i, 13],
        confederation=data.iloc[i, 14],
        rank_date=data.iloc[i, 15],
    )
    item.save()
