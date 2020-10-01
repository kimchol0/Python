import requests
from bs4 import BeautifulSoup

"""
爬取小说，用两个函数实现。
输入一个小说的首页，爬取对应章节的链接与标题。
得到一个列表之后，遍历每个章节的链接，
并得到相对应的页面正文。
"""


# 获取章节
def get_novel_chapters():
    root_url = "https://www.89wxw.com/read/3414/"  # 小说首页的地址
    r = requests.get(root_url)  # 将root_url存入变量r中
    # r.encoding="gbk" # 编码方式为GBK
    soup = BeautifulSoup(r.text, "html.parser")

    data = []
    for dd in soup.find_all("dd"):  # 遍历网页中包含dd内容的标签
        link = dd.find("a")  # 查找章节标题
        if not link:  # 如果没有标题就跳过
            continue

        data.append(("https://www.89wxw.com%s" % link['href'], link.get_text()))  # 字符串拼接，为了将前缀添加上去
    return data


def get_chapter_content(url):
    r = requests.get(url)  # 将url存入变量r中
    # r.encoding='gbk' # 编码方式为GBK
    soup = BeautifulSoup(r.text, "html.parser")
    return soup.find("div", id='content').get_text()  # 返回网页content中的文本内容


novel_chapers = get_novel_chapters()  # 将章节信息存入novel_chapers变量中
total_cnt = len(novel_chapers)  # 计算总章节的个数并存入total_cnt变量中
idx = 0  # 设置初始值为0
"""
遍历章节信息，每遍历一章则自加一
打印输出当前爬取的章节和总章节数
保存为txt文件
"""
for chapter in novel_chapers:
    idx += 1
    print(idx, total_cnt)
    url, title = chapter
    with open("%s.txt" % title, "w") as fout:
        fout.write(get_chapter_content(url))
