# Django项目服务器部署

开始部署前，请确保你的项目已经基本开发完善，能在本地稳定运行。

我这里的本地开发环境是：Windows10，Python 3.6.0，Django2.2，MySQL5.7

这里选择的部署环境是：Unbatu16.04，Django2.2，Python3.5.2，MySQL5.7，nginx1.10.3，uwsgi-2.0.18

下面的教程仅供参考！



## 准备工作

- 由于需要远程操作服务器，请确保你拥有服务器的远程连接密码和服务器IP

- 远程连接工具：Xshell5（这里也可以选择其他的）
- 远程文件传输：fxtp软件（这里你也可以选择使用GitHub仓库），我这里选择MobaXterm个人版（免费）
- 文本编辑器：Notepad++（修改文件需要用到，使用这个是因为能够打开几乎所有格式的文件）

由于这里使用了fxtp软件，所有就算不熟悉Linux下的vim指令也无所谓，依然能够完美的完成整个服务器的操作。（本教程就是为了给小白看的）

- 服务器一台（国外免备案方便），域名

  对于服务器和域名的选择，大家自行Google吧，这个没啥困难的。



## 连接服务器

这个应该不需要怎么讲吧，大家如果实在不会的话，Google搜一下“Xshell连接服务器”吧，这里不详细讲了。

打开Xshell，然后点击 文件→主机（填写服务器IP）→端口号（国内服务器好像默认22，如果不是自己根据实际填写）→用户身份验证→方法→Password→用户名root→密码（填写自己服务器的密码）→确定，然后连接上去。

这里没有截图，可能大家不是很明白，相信大家都可以轻松解决这个问题



下面使用到的一些命令，如果大家不熟悉，没关系，大家后续学习一下Linux基本就懂了。

另外，如果光标变为方块，按键盘的`Insert`键即可恢复`|`

## 更新系统

```python
sudo apt-get update
sudo apt-get upgrade
```



## 安装MySQL

```python
#待会提示设置root密码,重复输入即可
sudo apt-get install mysql-server  

#安装这个是因为Django连接MySQL需要这个，mysqlclient这个库需要这个支持，否则会报错
sudo apt-get install libmysqlclient-dev  
```

### 修改数据库编码为 utf-8

因为我们网站的主要语言是中文，所有数据库编码要使用utf-8编码，否则会报错。

```python
#登录MySQL，然后输入密码（上面设置的root密码）
mysql -u root -p 

# 查看MySQL编码（不要漏掉英文输入法的分号，MySQL命令以英文分号结束）
show variables like 'char%'; 
```

<img src="https://i.loli.net/2019/05/18/5ce0020e3f6b642983.jpg" height="60%" width="60%" alt="MySQL编码.jpg" title="MySQL编码.jpg" />

现在的编码格式是`latin1`，下面我们要修改为`utf-8`

一般熟悉vim操作的话，我们可以直接使用vim在Xshell修改，为了照顾不熟悉Linux操作的朋友，下面使用fxtp软件操作。

打开`XobaXterm`,然后连接上数据库，具体操作这里不详细说了，比较简单，不会的朋友Google吧。

```python
# 进入这个目录，找到下面的 mysqld.cnf
/etc/mysql/mysql.conf.d

# 提前在本地新建一个 .conf文件，然后修改为默认notepad++打开
```

打开``mysqld.cnf ``文件，在`lc-messages-dir = /usr/share/mysql `语句后添加 `character-set-server=utf8 `语句

```python
lc-messages-dir	= /usr/share/mysql
character-set-server=utf8 # 添加这一行

# 然后保存
```

<img src="https://i.loli.net/2019/05/18/5ce0046c7026470639.png" height="60%" width="60%" alt="修改MySQL数据库编码.png" title="修改MySQL数据库编码.png" />



```python
# 按照上面一样的做法，打开下面目录下的 mysql.cnf 文件
/etc/mysql/conf.d/
```

```python
# 在 [mysql] 下面添加这行代码
default-character-set=utf8
```

### 重启数据库

在终端中输入 ` /etc/init.d/mysql restart `命令重启MySQL服务

```python
# 输入 /etc/init.d/mysql restart
root@localhost:~# /etc/init.d/mysql restart
[ ok ] Restarting mysql (via systemctl): mysql.service.

```

### 查看数据库编码修改成功

```python
# 登录MySQL
root@localhost:~# mysql -u root -p
# 查看数据库编码
show variables like 'char%'; 
```

<img src="https://i.loli.net/2019/05/18/5ce00687debd148734.jpg" height="60%" width="60%" alt="MySQL修改后编码.jpg" title="MySQL修改后编码.jpg" />

这个时候数据库编码已经修改为`utf-8`了

### 新建MySQL数据库

本地项目根目录下的配置文件：`settings.py`关于MySQL数据库的设置

将上面的安装MySQL的时候设置的密码，填写到自己需要部署的文件里面。

然后需要新建一个数据库。

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',      #主要是这里，将默认的sqlite3改为mysql
        'NAME': 'your_database_name',              #数据库的名字
        'USER':'root',                             #数据库用户名
        'PASSWORD':'your_password',                #数据库密码
        'HOST':'127.0.0.1',                        #数据库地址，默认本机地址
        'PORT':'3306',                             #数据库端口，默认3306

    }
}
```



### MySQL数据创建查看删除

登录MySQL之后：

```python
#新建数据库，注意别漏了“;”分号 (这里的my_database_name为你需要新建的数据库的名称)
create database my_database_name;

# 查看数据库
show databases;

# 删除名为mynewdatabase的数据库 
drop database mynewdatabase;

#退出数据库 exit 然后回车
exti # 回车
```



## 安装配置软件

下面进行一些必要的服务器软件安装：安装nginx，git，python3 ，python3-pip，virtualenv，uwsgi 

```python
sudo apt-get install nginx
sudo apt-get install git python3 python3-pip
sudo pip3 install virtualenv
pip3 install uwsgi 
```



## 新建用户

新建用户是为了避免使用 root 用户导致权限问题。

例如有时候会因为权限不足导致无法读取和上传文件到服务器。

```python
# 这里的 ShibaInu是我新建用户的用户名，大家替换为自己的即可 useradd -m -s /bin/bash ShibaInu
root@localhost:~# useradd -m -s /bin/bash ShibaInu

# 把新创建的用户加入超级权限组 usermod -a -G sudo ShibaInu
root@localhost:~# usermod -a -G sudo ShibaInu

# 为新用户设置密码，注意在输密码的时候不会有字符显示，不要以为键盘坏了，正常输入即可
# 命令：passwd ShibaInu
root@localhost:~# passwd ShibaInu
Enter new UNIX password:      #(这里填密码)
Retype new UNIX password:     #重复确认
passwd: password updated successfully

# 切换到创建的新用户 su - ShibaInu
root@localhost:~# su - ShibaInu

# 切换成功，@符号前面已经是新用户名而不是 root 了
ShibaInu@localhost:~$
```



## 上传软件到服务器

生成本地项目依赖包：进入本地项目虚拟环境，输入以下命令可以在项目根目录生成一个`requirements.txt`文件，里面包含了项目需要的一些依赖包

```python
pip freeze > requirements.txt
```



修改本地项目根目录下的`settings`配置文件

```python
# DEBUG = True
DEBUG = False

#这里修改为你的域名即可，没有域名的修改为服务器ip
ALLOWED_HOSTS = ['www.ipydev.com','ipydev.com',] 

# 静态文件设置
STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
```

关于上面的设置，我做一些解释说明：

- 首先`DEBUG`这样设置是为了项目出现问题的时候，可以方便的设置为`DEBUG = True`检查问题
- 关于域名的购买，大家自行Google，没有的可以设置为服务器IP，或者自行搭建一个服务器，这里的www前缀代表的是二级域名，ipydev.com是.com的顶级国际域名，关于域名的更多知识，大家可以Google了解。这样设置是为了访问`www.ipydev.com`也可以访问到我的网站。

- 关于静态文件的设置问题，第二行是正常的设置，第三行是为了下面迁移静态文件准备的，暂时还不需要，所有注释掉。不理解的没关系，下面会讲到这样做的原因。



上传项目文件到`/home/ShibaInu` (这里的ShibaInu是我上面新建的用户名，修改为自己的即可)

使用`MobaXterm`将项目文件（除了虚拟环境那个文件的整个文件）上传到新建用户目录下。

一般项目文件很小，大概是几个Mb，上传不需要很久。



另外关于CDN加速：下面是Bootstrap中文网 维护的 BootCDN 免费加速服务

我本地开发是使用压缩的本地文件，部署前，我使用了BootCDN文件进行了测试，发现jQuery会影响我的部分样式，所有我只使用了除 `jquery`外的CDN免费加速。（如果大家的项目是完全使用bootstrap开发的前端，自然是可以考虑使用这个免费的CDN加速服务的）

主要修改`base.html `和 `reply`

```html
<link rel="stylesheet" href="https://cdn.bootcss.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">

<script src="https://cdn.bootcss.com/jquery/3.2.1/jquery.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
<script src="https://cdn.bootcss.com/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
<script src="https://cdn.bootcss.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
```



## 配置域名解析

域名解析简单的理解就是，将服务器和域名联系到一起，访问者看到的不是127.0.0.1这个IP而是你的域名。

到域名购买商网站，选择DNS管理，然后按照下面这样设置：

（不同的域名商设置界面可能不太一样，但原理是一样的）

<img src="https://i.loli.net/2019/05/18/5ce010f2267c298719.jpg" height="60%" width="60%" alt="域名解析设置.jpg" title="域名解析设置.jpg" />

第一行是为了解析`ipydev.com`，第二行是解析`www.ipydev.com`



## 安装虚拟环境和环境包

进入到ShibaInu这个目录下：

```python
# 切换到创建的新用户 su - ShibaInu
root@localhost:~# su - ShibaInu

# 切换成功，@符号前面已经是新用户名而不是 root 了
ShibaInu@localhost:~$ 
```

安装虚拟环境和项目依赖的包（项目的整个文件夹已经上传到ShibaInu这个文件夹下了）

```python
# 安装虚拟环境
virtualenv --python=python3 env

# 进入虚拟环境 Linux需要使用 source这个命令
source env/bin/activate

# 进入项目文件夹 这里的mysite是我的项目名称
cd mysite

# 安装项目依赖的包
pip install -r requirements.txt
```



## 测试Django项目

注意这里必须使用管理员root 身份进行测试，普通用户可能会出现权限问题，例如无法post 数据到服务器

### 测试项目运行情况

#### 迁移静态文件

```python
python manage.py migrate
```

#### 创建超级用户

需要输入用户名，邮箱，密码，确认密码

```python
python manage.py createsuperuser
```

#### 测试运行

这里0.0.0.0指的是默认本地IP即服务器IP，8000是运行端口，你可以设置为其他的，insecure指的需要加载静态文件，否则静态文件不会加载

```python
python manage.py runserver 0.0.0.0:8000 --insecure
```

然后访问项目是否正常运行` http://your_server_ip:8000`



其实这个时候大部分都是正常的，部分功能会出现问题，例如我的网站的评论功能之类的，原因是静态文件还没有迁移。



### 静态文件迁移

下面进行静态文件的迁移。

在`MobaXterm`中打开项目配置文件`settings.py`修改静态文件配置

注释第二行，去掉第三行的注释

```python
STATIC_URL = '/static/'
# STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
```

以root用户进入虚拟环境

```python
root@localhost:~# cd /home/ShibaInu/
root@localhost:/home/ShibaInu# source env/bin/activate
(env) root@localhost:/home/ShibaInu# cd mysite
(env) root@localhost:/home/ShibaInu/mysite# 

# 转移静态文件,然后输入 yes 进行转移
python manage.py collectstatic
```

转移完静态文件后，需要修改静态文件目录的设置

```python
# 转移静态文件之后，修改回来
STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
```

其他问题：如果这个时候再按照上面的命令去测试运行情况，还是出现问题，就去修改`DEBUG=True`，根据命令行的输出去修复漏洞。

我这里还是会出现一个问题：富文本编辑器`ckeditor`的问题

- 1.无法加载评论框 → 还没有转移静态文件导致，转移静态文件即可

- 2.无法动态加载二级评论，即无法提交二级回复 → 本地虚拟环境下找到prism
  复制prims整个文件夹到静态文件夹下的富文本编辑器的下面这个目录，否则无法加载富文本编辑器
  本地：`\env\Lib\site-packages\ckeditor\static\ckeditor\ckeditor\plugins\prism`
  服务器：`\mysite\static\ckeditor\ckeditor\plugins`

在本地找到这个目录，使用`MobaXterm`上传到静态文件夹下的`ckeditor`的相应目录下即可。

出现这个问题的原因主要是服务器上安装的这个包确少这个目录。

大家也可能会出现其他问题，只需要根据错误信息找到相应的解决方法即可。

一切测试都已经通过的话，就可以修改`DEBUG=False`了



## 删除测试数据

删掉数据库，新建一个即可，重新迁移一下数据库就可以了

然后需要重新设置超级管理



## 配置 uWSGI

简单了解一下uwsig:

```powershell
wsgi：一种实现python解析的通用接口标准/协议，是一种通用的接口标准或者接口协议，实现了python web程序与服务器之间交互的通用性。 
利用它，web.py或bottle或者django等等的python web开发框架，就可以轻松地部署在不同的web server上了；

uwsgi:同WSGI一样是一种通信协议 
uwsgi协议是一个uWSGI服务器自有的协议，它用于定义传输信息的类型，它与WSGI相比是两样东西。

uWSGI :一种python web server或称为Server/Gateway 
uWSGI类似tornadoweb或者flup，是一种python web server，uWSGI是实现了uwsgi和WSGI两种协议的Web服务器，负责响应python 的web请求。 
因为apache、nginx等，它们自己都没有解析动态语言如php的功能，而是分派给其他模块来做，比如apache就可以说内置了php模块，让人感觉好像apache就支持php一样。 

uWSGI实现了wsgi协议、uwsgi协议、http等协议。 Nginx中HttpUwsgiModule的作用是与uWSGI服务器进行交换
```



虚拟环境安装uwsgi，测试uwsgi启动项目

- `http :8000`使用本地IP的8000端口运行

- `/home/ShibaInu/mysite/`是我的项目根目录
- `mysite.wsgi`我的项目名称是`mysite`
- `--static-map /static=/home/ShibaInu/mysite/static/`这个指的是运行加载静态文件并制定静态文件的目录
- 然后浏览器打开`http://your_server_ip:8000`查看运行情况,应该和上面使用`runserver`运行情况是一样的

```python
pip install uwsgi
uwsgi --http :8000 --chdir /home/ShibaInu/mysite/ --wsgi mysite.wsgi --static-map /static=/home/ShibaInu/mysite/static/
```



一切正常，开始使用配置文件运行测试：

uwsgi配置文件：mysite_uwsgi.ini

然后将这个配置文件上传到项目根目录下，即和静态文件`static`同一个目录

```ini
[uwsgi]
# 使用8080端口
http= :8080
#socket =  :8080
# 项目位置 mysite是我的项目名称
chdir           = /home/ShibaInu/mysite
# 修改为自己的项目名称即可
module          = mysite.wsgi
# 虚拟环境目录 env是我的服务器虚拟环境名称
home            = /home/ShibaInu/env/
master          = true
# 最大工作进程，一般根据核心数设置，也可以任意设置
processes       = 4
vacuum          = true
# 日志文件
daemonize = /home/ShibaInu/mysite/uwsgi.log
# 静态文件目录
static-map = /static=/root/mysite/static
```

重新打开一个Xshell窗口，然后运行下面的命令，使用配置文件运行项目

这里的` /home/ShibaInu/mysite/uwsgi.ini`指的是配置文件位置

```shell
# 开启 uwsgi配置文件启动
sudo uwsgi --ini /home/ShibaInu/mysite/uwsgi.ini
```

然后运行浏览器打开`http://your_server_ip:8080`查看运行情况,应该和上面使用`runserver`运行情况是一样的



运行测试没问题，开始配置nginx，并修改uwsgi配置文件

```ini
[uwsgi]
# 使用8080端口
#http= :8080
socket =  :8080
# 项目位置 mysite是我的项目名称
chdir           = /home/ShibaInu/mysite
# 修改为自己的项目名称即可
module          = mysite.wsgi
# 虚拟环境目录 env是我的服务器虚拟环境名称
home            = /home/ShibaInu/env/
master          = true
# 最大工作进程，一般根据核心数设置，也可以任意设置
processes       = 4
vacuum          = true
# 日志文件
daemonize = /home/ShibaInu/mysite/uwsgi.log
# 静态文件目录
#static-map = /static=/root/mysite/static
```

其实上面那一步配置文件测试不是必须的，但是你也可以测试一下，一般来说使用下面这个命令测试没问题都是没问题的了。

```shell
uwsgi --http :8000 --chdir /home/ShibaInu/mysite/ --wsgi mysite.wsgi --static-map /static=/home/ShibaInu/mysite/static/
```



## 配置nginx

nginx是常用高性能代理服务器，为什么要使用nginx呢，下面简单分析其工作原理。

```powershell
首先客户端请求服务资源，
nginx作为直接对外的服务接口,接收到客户端发送过来的http请求,会解包、分析，
如果是静态文件请求就根据nginx配置的静态文件目录，返回请求的资源，
如果是动态的请求,nginx就通过配置文件,将请求传递给uWSGI；uWSGI 将接收到的包进行处理，并转发给wsgi，
wsgi根据请求调用django工程的某个文件或函数，处理完后django将返回值交给wsgi，
wsgi将返回值进行打包，转发给uWSGI，
uWSGI接收后转发给nginx,nginx最终将返回值返回给客户端(如浏览器)。
*注:不同的组件之间传递信息涉及到数据格式和协议的转换
```

作用: 

- 第一级的nginx并不是必须的，uwsgi完全可以完成整个的和浏览器交互的流程； 

- 在nginx上加上安全性或其他的限制，可以达到保护程序的作用； 

- uWSGI本身是内网接口，开启多个work和processes可能也不够用，而nginx可以代理多台uWSGI完成uWSGI的负载均衡； 

- django在debug=False下对静态文件的处理能力不是很好，而用nginx来处理更加高效。



查看真实的Nginx配置文件位置

```python
nginx -t

root@localhost:~# nginx -t
nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
nginx: configuration file /etc/nginx/nginx.conf test is successful
```

<img src="https://i.loli.net/2019/05/18/5ce01e8c94f3024853.jpg" height="60%" width="60%" alt="nginx配置文件.jpg" title="nginx配置文件.jpg" />

将这个文件下载到本地，然后打开，修改

在http中的`include /etc/nginx/sites-enabled/*;`下面增加下面的`server{}`

```nginx
http{
    ...
	include /etc/nginx/conf.d/*.conf;
	include /etc/nginx/sites-enabled/*;
	
	server {
    listen      80;
    server_name    .ipydev.com; 
    ...
}
```

完整的`server{}`

```nginx
server {
    # http默认监听80端口
    listen      80;
    # 修改为自己的域名， .ipydev.com表示包含所有二级域名
    server_name    .ipydev.com; 
    charset     utf-8;
    client_max_body_size 75M;  
    
    # 修改为你的媒体文件目录
    location /media  {
        alias /home/ShibaInu/mysite/media;  # your Django project's media files - amend as required
    }
    
    # 修改为你的静态文件目录
    location /static {
        alias /home/ShibaInu/mysite/static; # your Django project's static files - amend as required
    }


    location / {
        # 这个是上面uwsgi.ini设置的8080端口，前后要一致，nginx就算靠这个和uwsgi通信的
        uwsgi_pass  127.0.0.1:8080;
        include     /etc/nginx/uwsgi_params; 
    }
}
```



然后将这个新的文件nginx.conf（修改后的）上传到项目根目录下(即和uwsgi.ini同级的目录下)

```python
# 停止nginx 
nginx -s stop 

# 启动nginx新配置 /home/ShibaInu/mysite/nginx.conf 为配置文件位置
nginx -c /home/ShibaInu/mysite/nginx.conf
```

这个时候就可以正常的访问 `http://ipydev.com`了

### Nginx常规操作

```nginx
启动服务：start nginx 
停止服务：nginx -s stop 
重新加载：nginx -s reload  (配置文件被修改后需要执行它)

# 查看真实的Nginx配置文件位置
nginx -t

# 提示80端口无法绑定，用命令 netstat -ntpl 查看端口占用情况
netstat -ntpl

# 列出占用端口的程序的pid号，并使用以下命令杀掉所有占用端口的程序
# pid_number为那个pid号
sudo kill -9 pid_number 
```



## SSL证书安装

[Let’s Encrypt](https://letsencrypt.org/) 是一个自动签发 https 证书的免费项目
[Certbot](https://certbot.eff.org/) 是 [Let’s Encrypt](https://letsencrypt.org/) 官方推荐的证书生成客户端工具

打开Xshell窗口

```python
# 输入以下命令
$ sudo apt-get update
$ sudo apt-get install software-properties-common
$ sudo add-apt-repository ppa:certbot/certbot
$ sudo apt-get update
$ sudo apt-get install certbot python-certbot-nginx 
$ certbot --version

检查端口占用
如果服务器上的 443 端口正在被占用，请先关闭对应的服务进程
否则可能个导致 certbot 运行出错

以命令交互方式开始制作证书（首次运行会让你输一次邮箱）
$ certbot certonly    --------> 开启命令

root@localhost:~# certbot certonly
Saving debug log to /var/log/letsencrypt/letsencrypt.log

How would you like to authenticate with the ACME CA?
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
1: Nginx Web Server plugin (nginx)
2: Spin up a temporary webserver (standalone)
3: Place files in webroot directory (webroot)
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Select the appropriate number [1-3] then [enter] (press 'c' to cancel): 1

这里选择1


Plugins selected: Authenticator nginx, Installer None
Starting new HTTPS connection (1): acme-v02.api.letsencrypt.org
Please enter in your domain name(s) (comma and/or space separated)  (Enter 'c'
to cancel): ipydev.com

这里输入域名


Obtaining a new certificate
Performing the following challenges:
http-01 challenge for ipydev.com
Waiting for verification...
Cleaning up challenges
Resetting dropped connection: acme-v02.api.letsencrypt.org

IMPORTANT NOTES:
 - Congratulations! Your certificate and chain have been saved at:
   /etc/letsencrypt/live/ipydev.com/fullchain.pem
   证书位置
   
   Your key file has been saved at:
   /etc/letsencrypt/live/ipydev.com/privkey.pem
   密钥位置
   
   Your cert will expire on 2019-08-15. To obtain a new or tweaked
   version of this certificate in the future, simply run certbot
   again. To non-interactively renew *all* of your certificates, run
   "certbot renew"
 - If you like Certbot, please consider supporting our work by:

   Donating to ISRG / Let's Encrypt:   https://letsencrypt.org/donate
   Donating to EFF:                    https://eff.org/donate-le

```

证书的有效期是3个月，到期可以续订，或者自动续订

自动续订：

```python
sudo certbot renew --dry-run
```

到期续订：

```python
certbot renew
```



修改nginx配置，使用证书生效

主要修改server{}

在原来的`server{}`前面增加一个`80端口重定向到443端口的server`

http协议监听80端口，https协议监听443端口

```nginx
# 增加这个
server {
    listen 80;
    server_name .ipydev.com;
    rewrite ^(.*)$ https://${server_name}$1 permanent; 
}

server {
    # listen      80;
    # 修改为 监听443
    listen 443 ;
    # 打开SSL
    ssl on;
    
    server_name    .ipydev.com; 
    
    # 修改为你的证书和密钥位置
    ssl_certificate /etc/letsencrypt/live/ipydev.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/ipydev.com/privkey.pem;
    
    charset     utf-8;
    
   ...
   
}
```



修改完配置文件，关闭nginx，重启配置文件使其生效

```python
nginx -s stop 
nginx -c /home/ShibaInu/mysite/nginx.conf
```



现在访问`ipydev.com`都是https加密的了



## 修改项目文件

好吧，到这里我们基本完成了全部工作，但是有一个问题，要是我们需要修改文件怎么办？？？

因为nginx的配置我们设置了`sendfile on;`可以快速生效修改配置，至于这个命令是什么作用，大家Google吧，这里不详细讨论。

```nginx
http {
    
    ...
    
	sendfile on;
	
	...
	}
```



使用ftp软件修改完项目文件，或者上传新的项目文件后，关闭`uwsgi.ini`并重启即可。

```python
# 查看uwsgi进程的pid
netstat -ntpl

# 杀死 uwsgi进程
sudo kill -9 uwsgi_pid)number

# 重启 uwsgi
sudo uwsgi --ini /home/ShibaInu/mysite/uwsgi.ini
```

上面这种方法是很粗鲁的，因为有可能造成程序错误，导致出现服务器`500`错误...

经过查看文档和网上的资料，得到了一种简单优雅的方法，就是下面的方法。



### 重新设置 uwsgi.ini

最好的设置：

`uwsgi.ini`放在 `/root` 目录下（`nginx.conf`最好也是，不过一般不需要修改这个配置文件）

```ini
[uwsgi]
#http= :8080
socket =  :8080
# Django-related settings
# the base directory (full path)
chdir           = /home/ShibaInu/mysite
# Django's wsgi file
module          = mysite.wsgi
# the virtualenv (full path)
home            = /home/ShibaInu/env/

# process-related settings
# master
master          = true
processes=4     #进程数量
threads=2      #线程数量
max-requests=1000
# the socket (use the full path to be safe）
#socket          = /root/mysite/mysite.sock
# ... with appropriate permissions - may be needed
#chmod-socket    = 664
# clear environment on exit
vacuum          = true
# 日志文件
daemonize = /root/uwsgi.log
# pid文件，用于脚本启动、停止该进程
pidfile = /root/uwsgi.pid    
# 静态文件目录
# static-map = /static=/home/ShibaInu/mysite/static
```



### 重启 启动 关闭 uwsgi.ini

修改项目文件后，重启`uwsgi.ini`

```bash
# 启动 uwsgi
sudo uwsgi --ini uwsgi.ini

# 关闭 uwsgi
sudo uwsgi --stop uwsgi.pid

# 重启 uwsgi 重启即可
sudo uwsgi --reload uwsgi.pid
```



这样子的话，我就可以每天实时修改一些自己想修改的内容了



---

到这里就结束了整个部署流程，还是比较顺利的。

如果大家有其他问题也可以留言，我有时间会回复大家的。

使用Ubantu18.04可能和16.04会不一样，另外我个人感觉Ubantu Server和CentOS 没太多区别，性能上感觉差别不大，当然大家选择自己喜欢就好了。

