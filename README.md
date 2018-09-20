# lihao_test

#### 数据集
使用了Kaggle中的Fifa ranking数据集

https://www.kaggle.com/tadhgfitzgerald/fifa-international-soccer-mens-ranking-1993now
#### 数据库
使用MySQL数据库
#### 请求
访问方式 GET /search/?key=关键字1%20关键字2

支持多个关键字搜索，多个关键字之间用空格分隔。
#### 响应
返回包含所有搜索结果的json字符串。每个关键字对应一个搜索结果列表。如果没有搜索结果，则该列表为空。每一条搜索结果以字典类型展现。