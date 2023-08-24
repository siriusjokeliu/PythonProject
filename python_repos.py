import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS
"""执行API调用并储存响应"""

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code:", r.status_code)

"""将API响应储存在一个变量中"""
response_dict = r.json()
print("Total repositories:", response_dict['total_count'])

"""处理结果"""
repo_dicts = response_dict['items']
names,stars = [],[]
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

mystyle = LS('#333366',base_style=LCS)
chart =pygal.Bar(style = mystyle, x_label_rotation = 45, show_legend = True)
chart.title = 'Most-starred Python Projects on Github'
chart.x_labels = names
chart.add('',stars)
chart.render_to_file('python_repos.svg')