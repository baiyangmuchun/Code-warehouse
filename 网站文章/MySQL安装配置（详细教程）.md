# MySQL安装和配置（详细教程）

## 安装

- Windows 版本：Windows 10 专业版 64bit
- MySQL 版本：MySQL 5.7.24

- **下载**：[MySQL Community Server](https://dev.mysql.com/downloads/mysql/)    

  现在的最新版本是 8.0.13 ，点击`Looking for the latest GA version?`,然后就看与看到以前的版本了

  这里选择的是免安装压缩包，**ZIP Archive** (mysql-5.7.24-winx64.zip)

- **安装（解压）**

   ZIP Archive版 是免安装的。只要解压就行了。和安装版的没什么不同，但就是不需要安装。找到下载好的`mysql-x.x.xx-winx64.zip`，然后解压到你想安装的地方，例如我这里解压到`D:\MySQL57`。解压完就ok了，但是现在还用不了，还需要配置系统变量，注册 MySQL 服务。

## 配置

- **配置系统环境变量**

   将安装路径的`bin` 目录加入系统环境变量,即在`Path`下新建一个环境变量，然后粘贴 bin 路径，保存然后全部确定。例如我的是`D:\MySQL57\bin `，复制路径然后在`Path`下新建一个文本框，粘贴进去，全部确定即可。

  - 没有配置环境变量的时候，在`cmd`下输入`mysql --version`回车，是这样的

  ```basic
  Microsoft Windows [版本 10.0.17134.345]
  (c) 2018 Microsoft Corporation。保留所有权利。
  
  C:\Users\pyCrawler>mysql --version
  'mysql' 不是内部或外部命令，也不是可运行的程序
  或批处理文件。
  ```

  - 配置好环境变量之后是这样的

  ```basic
  Microsoft Windows [版本 10.0.17134.345]
  (c) 2018 Microsoft Corporation。保留所有权利。
  
  C:\Users\pyCrawler>mysql --version
  mysql  Ver 14.14 Distrib 5.7.24, for Win64 (x86_64)
  ```

- **注册 MySQL 服务**

  - 以**管理员身份**打开命令提示符

    ```basic
    Microsoft Windows [版本 10.0.17134.345]
    (c) 2018 Microsoft Corporation。保留所有权利。
    
    C:\WINDOWS\system32>
    ```

  - 进入`MySQL安装目录下的 bin文件夹`，例如我的是`D:\MySQL57\bin`,具体操作如下：

    - 先进入相应的盘根目录，这里是`D盘`,输入`D:`（注意是在英文输入法下输入冒号）

      ```basic
      Microsoft Windows [版本 10.0.17134.345]
      (c) 2018 Microsoft Corporation。保留所有权利。
      
      C:\WINDOWS\system32>D:
      
      D:\>
      ```

    - 然后进入`bin文件夹`，输入`cd`+"空格"+"对应的文件路径"，例如我的是`cd D:\MySQL57\bin` 

      ```basic
      Microsoft Windows [版本 10.0.17134.345]
      (c) 2018 Microsoft Corporation。保留所有权利。
      
      C:\WINDOWS\system32>D:
      
      D:\>cd D:\MySQL57\bin
      
      D:\MySQL57\bin>
      ```

      <font color=red size=3 face="黑体">这一步非常重要，如果不在这个目录下，无法正确注册 MySQL 服务</font>  

  - 执行`mysqld -install`指令，注册 **MySQL 服务**。

    - 成功之后会显示`Service successfully installed.` 

    - <font color=red size=3 face="黑体">执行完毕后，请不要退出“命令提示符”</font>  

    ```
    Microsoft Windows [版本 10.0.17134.345]
    (c) 2018 Microsoft Corporation。保留所有权利。
    
    C:\WINDOWS\system32>D:
    
    D:\>cd D:\MySQL57\bin
    
    D:\MySQL57\bin>mysqld -install
    Service successfully installed.
    
    D:\MySQL57\bin>
    ```

  - **配置 MySQL Server** 

  进入 MySQL 所在的文件夹 ,我的是`D:\MySQL57` 

  编辑 `my-default.ini` ，如果没有这个文件，自己新建一个 `my.ini`

  <font color=red size=3 face="黑体">注：现在解压包多是没有这个配置文件的，这并不影响，直接新建一个即可。</font> 

  - - 在该文件中，`#`是注释标记。
    - 去掉 basedir 的注释符号，并在等号后边填写 MySQL 文件夹的完整地址。
    - 去掉 datadir 的注释符号，并在等号后边填写 MySQL  文件夹的完整地址外加`\data`。
    - <font color=red size=3 face="黑体">切记不要手动创建 data 文件夹！</font> 
    - port 不需要配置，不配置的状态下默认为 3306。（MySQL 默认使用的端口号）
    - 保存退出。退出后将`my-default.ini`重命名为`my.ini`
    - 在刚才的“命令提示符”中，执行`mysqld --initialize`（可能会假死，即看起来没什么反应，等一分钟手动关闭就好）。

  - 新建`my.ini` ，配置信息如下：
    - 如果没有，新建`my.ini` 文件之后，复制下面的代码，然后修改就可以了
    - 主要修改 `MySQL的安装目录`和`data数据储存位置` 
    - 保存退出，然后将`my-default.ini`重命名为`my.ini`
    - 在刚才的“命令提示符”中，执行`mysqld --initialize`（可能会假死，即看起来没什么反应，等一分钟手动关闭就好）。

  ```basic
  [mysql]
  # 设置mysql客户端默认字符集
  default-character-set=utf8 
  
  [mysqld]
  #设置3306端口
  port = 3306 
  
  # 设置mysql的安装目录
  basedir=D:\MySQL57
  
  # 设置mysql数据库的数据的存放目录
  datadir=D:\MySQL57\data
  
  # 允许最大连接数
  max_connections=200
  
  # 服务端使用的字符集默认为8比特编码的latin1字符集
  character-set-server=utf8
  
  # 创建新表时将使用的默认存储引擎
  default-storage-engine=INNODB
  ```



  - 上述操作完成后，即运行`mysqld --initialize`成功后，就看与在`MySQL`目录下载看到多了一个`data`文件夹

  <font color=blue size=3 face="黑体">注：以后需要修改数据存放目录,一样是修改配置文件，保存退出，然后管理员身份进入安装目录下的 bin 文件夹，最后运行`mysqld --initialize`，执行完之后，数据储存位置就更新了.</font> 



- **开启 MySQL Server**

  在“命令提示符”中执行`net start mysql`，开启 MySQL Server。

  - 出现这个错误：

```basic
Microsoft Windows [版本 10.0.17134.345]
(c) 2018 Microsoft Corporation。保留所有权利。

C:\Users\pyCrawler>net start mysql
发生系统错误 5。

拒绝访问。
```

- - 使用管理员身份运行命令提示符即可解决

  ```basic
  Microsoft Windows [版本 10.0.17134.345]
  (c) 2018 Microsoft Corporation。保留所有权利。
  
  C:\WINDOWS\system32>net start mysql
  请求的服务已经启动。
  
  请键入 NET HELPMSG 2182 以获得更多的帮助。
  ```



- **配置 MySQL root 账户** 

  - 管理员身份启动命令提示符，输入`net stop mysql`,停止`MySQL server`

  ```basic
  Microsoft Windows [版本 10.0.17134.345]
  (c) 2018 Microsoft Corporation。保留所有权利。
  
  C:\WINDOWS\system32>net stop mysql
  MySQL 服务正在停止.
  MySQL 服务已成功停止。
  ```

  - 再执行`mysqld --skip-grant-tables`开启无密码的 MySQL Server

    这里执行之后，可能会出现假死状态，即命令执行没有出现完成装填，也就是一直显示运行状态，没有跳转到下一个命令行，等一会关闭即可

  ```basic
  Microsoft Windows [版本 10.0.17134.345]
  (c) 2018 Microsoft Corporation。保留所有权利。
  
  C:\WINDOWS\system32>net stop mysql
  MySQL 服务正在停止.
  MySQL 服务已成功停止。
  
  
  C:\WINDOWS\system32>mysqld --skip-grant-tables
  
  ```

  - 打开一个新的“命令提示符”，执行`mysql -u root`登陆 MySQL Server。

  - 执行`flush privileges`刷新权限。

  - 执行`grant all privileges on *.* to 'root'@'localhost' identified by '你想设置的密码' with grant option;`。

  - 执行`flush privileges`刷新新的 root 用户密码。

  - 执行`exit`退出 MySQL。

    ```basic
    Microsoft Windows [版本 10.0.17134.345]
    (c) 2018 Microsoft Corporation。保留所有权利。
    
    C:\Users\pyCrawler>mysql -u root
    Welcome to the MySQL monitor.  Commands end with ; or \g.
    Your MySQL connection id is 6
    Server version: 5.7.24 MySQL Community Server (GPL)
    
    Copyright (c) 2000, 2018, Oracle and/or its affiliates. All rights reserved.
    
    Oracle is a registered trademark of Oracle Corporation and/or its
    affiliates. Other names may be trademarks of their respective
    owners.
    
    Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.
    
    mysql> flush privileges;
    Query OK, 0 rows affected (0.00 sec)
    
    mysql> grant all privileges on *.* to 'root'@'localhost' identified by 'The password you want' with grant option;
    Query OK, 0 rows affected, 1 warning (0.00 sec)
    
    mysql> flush privileges;
    Query OK, 0 rows affected (0.00 sec)
    
    mysql> exit
    Bye
    
    C:\Users\pyCrawler>
    ```

- 在任务管理器下手动结束`mysqld.exe`

`Ctr + Alt + Delete` 打开任务管理器

- 在“命令提示符”下执行`net start mysql `重新开启MySQL Server，再次使用`mysql -u root -p 你设置的密码`即可安全登陆 MySQL。
- 注意：上述操作如果出现**“拒绝访问”**的问题，切换管理员身份打开命令行即可



## 无法启动MySQL（解决）

- win + s :搜索`服务`，没有找到 `MySQL`

- cmd中输入net start mysql 提示：服务名无效

解决办法：

- 请进入MySQL的bin目录，并在bin目录打开命令行窗口，在命令行窗口输入：mysqld --install，回车，提示：Service successfully installed。表示安装MySQL服务成功，命令行窗口输入：net start mysql ，可以正常启动。

- 然后按照上述步骤重新设置密码即可



## MySQL 语句的规范

- 关键字与函数名称全部大写.

- 数据库名称, 表名称, 字段名称等全部小写.

- <font color=blue size=4 face="黑体">SQL 语句必须以分隔符 ; 结尾.</font> 

- SQL 语句支持折行操作, 只要不把单词, 标记或引号字符串分割为两部分, 可以在下一行继续写

- 数据库名称, 表名称, 字段名称等尽量不要使用MySQL的保留字, 如果需要使用的时候需使用反引号(``)将名称括起来.







