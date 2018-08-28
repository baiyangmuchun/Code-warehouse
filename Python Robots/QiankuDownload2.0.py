message = ["http://588ku.com 千库网图片下载助手","下载说明：仅支持『背景图库』『商用插图』"," ","软件作者：BigCute"," "]
for i in range(0,len(message)):
    print(message[i])

def QiankuDownload():
    
    import urllib.request
    import urllib.error
    import re
    
    url = input('请输入图片网址：')

    headers = ("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36")
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]

    data = opener.open(url).read()
    data2 = data.decode("utf-8", "ignore")

    pat = 'img-l-box"><img src="(.*?)!|img id="qhimg" src="(.*?)!'
    imageURL = re.compile(pat).findall(data2)
    imageURL = max(imageURL)
    imageURL = "".join(imageURL)

    pat2 = '[(\d)]'
    i = re.compile(pat2).findall(url)
    i = "".join(i)
    
    try:
        print(" ")
        print("开始下载...")
        file ="D:/PictureMaterial/"+str(i)+".png"
        urllib.request.urlretrieve(imageURL,file)
        print(" ")
        print("Successful Download")
        print(" ")
        print("******************************************************")
        print("Continue to download")
        print(" ")
       
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)           
    QiankuDownload()

while True:
    QiankuDownload()
    if len(url) != 0:
        continue
        QiankuDownload()
