##  Github仓库的基本操作

## 安装 Git工具

安装 Git GUI 和 Git Bash

下载：[git工具](https://git-scm.com/downloads) 选择需要的系统版本下载

<img src="https://upload-images.jianshu.io/upload_images/3067059-fa7d131432a1232e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/503/format/webp" height="50%" width="50%"/>



## 绑定用户

打开`git-bash.exe`（直接在桌面上点击右键，或者点击开始按钮找到Git Bash）

在打开的GIt Bash中输入以下命令（用户和邮箱为你github注册的账号和邮箱）

注：下面的用户名、邮箱替换为你自己的

```powershell
$ git config --global user.name "ShibaInu99"
$ git config --global user.email "ShibaInu@ipydev.com"
```



## 配置SSH key

git中sshkey有何作用？

> 众所周知ssh是加密传输。
>
> 加密传输的算法有好多，git可使用rsa，rsa要解决的一个核心问题是，如何使用一对特定的数字，使其中一个数字可以用来加密，而另外一个数字可以用来解密。这两个数字就是你在使用git和github的时候所遇到的public key也就是公钥以及private key私钥。
>
> 其中，公钥就是那个用来加密的数字，这也就是为什么你在本机生成了公钥之后，要上传到github的原因。从github发回来的，用那公钥加密过的数据，可以用你本地的私钥来还原。
>
> 如果你的key丢失了，不管是公钥还是私钥，丢失一个都不能用了，解决方法也很简单，重新再生成一次，然后在github.com里再设置一次就行

### 生成ssh key

首先检查是否已生成密钥`cd ~/.ssh`，如果返回的`ls`有3个文件,则密钥已经生成。

命令：

```powershell
$ cd ~/.ssh
$ ls
id_rsa  id_rsa.pub

```

如果没有密钥，则通过下面的命令生成，生成过程中一路按3次回车键就好了。（默认路径，默认没有密码登录）
生成成功后，去对应目录`C:\Users\pyCrawler\.ssh`里（pyCrawler为电脑用户名，每个人不同,这里的Users一般中文显示为用户）用记事本打开id_rsa.pub，得到ssh key公钥。

```powershell
$ ssh-keygen -t rsa -C "ShibaInu@ipydev.com"
```

<img src="https://i.loli.net/2019/05/19/5ce0f50519bf826119.png" alt="ssh密钥.png" title="ssh密钥.png" height="50%" width="50%" />

### 为github账号配置ssh key

切换到github，展开个人头像的小三角，点击settings，然后打开SSH keys菜单， 点击Add SSH key新增密钥，填上标题（最好跟本地仓库保持一致），接着将id_rsa.pub文件中key粘贴到此，最后Add key生成密钥。



## 上传文件到GitHub仓库 & 删除GitHub仓库文件

先将GitHub仓库pull下来

例如，我将git文件放到这里`D:\Git`，我在这里鼠标右键`Git Bash Here`

```powershell
$ git --help  # 帮助命令
$ git clone https://github.com/ShibaInu99/Code-warehouse.git  # pull拉GitHub仓库到本地

# 也可以使用下面的命令将远程仓库里面的项目拉下来（远程仓库默认tag name ：master or branch）
$ git pull origin master
```



### 上传文件

例如我们已经将远程仓库pull到本地了，然后我可以在仓库里面增加一些文件，然后上传到GitHub远程仓库，具体操作如下

```powershell
步骤：首先进入我们的本地仓库，右键进入Git Bash Here
git init                       # 初始化
git add  .                     # 添加跟踪
git commit  -m"描述文字"      # 提交本地版本库

# 建立远程连接 通常不需要
# git remote add orgin https://github.com/ShibaInu99/Code-warehouse.git 

# （远程仓库默认tag name ：master or branch）
git push origin master

```



### 删除文件

删除文件也很简单，和上传差不多。

首先将GitHub远程仓库pull到本地，然后将需要删除的文件删除，再同步到GitHub远程仓库

```powershell
$ dir # 列出远程仓库的文件
# 在本地仓库删除文件 myfile是需要删除的文件
$ git rm myfile
# 在本地仓库删除文件夹 myfolder是需要删除的文件夹
$ git rm -r myfolder
# 此处-r表示递归所有子目录，如果你要删除的，是空的文件夹，此处可以不用带上-r。

# 提交代码 将所有需要删除的文件删除后进行提交
$ git commit -m"我的修改"
# 推送到远程仓库（比如GitHub）
$ git push origin master
# 也可以使用 git push origin https://github.com/ShibaInu99/Code-warehouse.git
```



每次增加文件或删除文件，都要commit 然后直接 git push origin master，就可以同步到github上了



---

Github仓库基本操作并不难，相信这篇文章应该可以完美解决大家的问题了。

大家可以选择使用GitHub作为一个基本的图床使用，因为截图很小，所有一般是足够的，上传也很简单。



大家在操作过程遇到的任何问题也可以在下面评论，我有时间会回复的。



## Github做图床

在本地仓库新建一个`image`文件夹，直接将图片放到这个文件夹，然后将本地仓库同步上传到GitHub远程仓库。

```html
# 复制这张图片的网址如下
https://github.com/ShibaInu99/Code-warehouse/blob/master/image/skill.png

# markdown或html中显示：将blob修改为raw 否则无法显示，理由可以参考GitHub官方的解释
https://github.com/ShibaInu99/Code-warehouse/raw/master/image/skill.png
```









