# 导入urllib和re库
import urllib.request
import re

# 设置爬取的页数，进行循环爬取
for i in range(1, 3):
    url = "http://www.shxz.gov.cn/sites/CSMHXZMH/ViewList2_pg.ashx?page=" + str(
        i) + "&ctgId=fe188544-e1fe-4230-b754-40e8d70ae432&leftBarId=08f6f7e1-badb-49fd-8da9-009f8dcc14a0"

    # 模拟浏览器爬取并安装为全局变量 ，爬取所有页面的信息
    headers = ("User-Agent",
               "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0")
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]
    data = opener.open(url).read()
    data2 = data.decode("utf-8", "ignore")

    # 设置新闻网址的正则表达式去掉重复链接并提取每个新闻页面的网址,最后提取有用的部分
    pat = '40e8d70ae432&(infId.*?)&leftBarId'

    allurl = re.compile(pat).findall(data2)
    # 设置循环，列表输出去重
    for j in range(0, len(allurl)):
        try:
            realurl = "http://www.shxz.gov.cn/sites/Iframe_ZZTY_cxs/dyn/Content.ashx?"+str(allurl[j])+"&ctgId=fe188544-e1fe-4230-b754-40e8d70ae432&leftBarId=08f6f7e1-badb-49fd-8da9-009f8dcc14a0"
            print("第" + str(i) + str(j) + "次爬取")
            #设置保存文件本地路径并命名爬取到的每个文件
            file = "D:/PyCharm/code/news_shxz_gov/" + str(i) + str(j) + ".html"
            #开始爬取下载
            urllib.request.urlretrieve(realurl, file)
            print("-------成功-------")
        #设置异常处理
        except urllib.error.URLError as e:
            if hasattr(e, "code"):
                print(e.code)
            if hasattr(e, "reason"):
                print(e.reason)