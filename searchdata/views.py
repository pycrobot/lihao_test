from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from searchdata.models import FIFARanking

# Create your views here.


class SearchView(View):

    def get(self, request):
        # 获取关键字，关键字是查询字符串形式，关键字之间使用空格进行分隔
        key = request.GET.get('key')
        # 生成关键字列表
        if " " in key:
            keys = key.split(" ")
        else:
            keys = [key]

        # 最终返回字典形式数据，字典内包含多个关键字
        res = {}

        for key in keys:
            # 每个关键字的搜索结果放入列表中
            res[key] = []
            items = FIFARanking.objects.filter(country_full__exact=key)
            for item in items:
                # 每一条搜索结果
                dict = {
                    "rank": item.rank,
                    "country_full": item.country_full,
                    "country_abrv": item.country_abrv,
                    "total_points": item.total_points,
                    "previous_points": item.previous_points,
                    "rank_change": item.rank_change,
                    "cur_year_avg": item.cur_year_avg,
                    "cur_year_avg_weighted": item.cur_year_avg_weighted,
                    "last_year_avg": item.last_year_avg,
                    "last_year_avg_weighted": item.last_year_avg_weighted,
                    "two_year_ago_avg": item.two_year_ago_avg,
                    "two_year_ago_weighted": item.two_year_ago_weighted,
                    "three_year_ago_avg": item.three_year_ago_avg,
                    "three_year_ago_weighted": item.three_year_ago_weighted,
                    "confederation": item.confederation,
                    "rank_date": item.rank_date
                }
                res[key].append(dict)
        return JsonResponse(res)
