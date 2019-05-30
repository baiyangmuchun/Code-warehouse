##  修改cmd命令行中的用户名

由于我现在换了一个喜欢的用户名，所以我想修改`cmd`命令行显示的用户名，即`c盘用户文件夹下的文件名`，但是一般用户文件夹下的名字是无法直接修改的，这里提供一个有效的修改方法。

例如我现在的用户名是`ShibaInu`，但是我想修改为`ipydev.com`

<img src="https://i.loli.net/2019/05/20/5ce23ca9f3d7d72969.png" alt="原用户名.png" title="原用户名.png" height="50%" width="50%" />





## 重新设置电脑账户

由于最近电脑重装系统，用的是Windows10，一开始就要设置用户名，但是后来我还是决定使用系统默认的用户名，，所以导致除了管理员账户，还有一个自己装系统的时候设置的用户，但是我觉得保留一个管理员账户即可，因为权限高。修改用户名的方法如下：删掉原来的账户，只保留管理员账户即可。

<img src="https://i.loli.net/2019/05/20/5ce23caa3249426921.png" alt="用户设置.png" title="用户设置.png" height="50%" width="50%" />

## 原用户名

这个时候我们打开`C:\Users`即`C:\用户`文件夹，可以看到此时的用户名，我这里是三个文件夹，其中一个是`ShibaInu`



##  修改用户名

1.`win + R`打开运行输入`regedit `回车，打开`注册表编辑器`

定位到下面这个文件夹下：然后找到下面文件名最长的那个，点击进去，找到右侧名为`ProfileImagePath`的文件，双击打开，修改自己喜欢的用户名，点击确定

```powershell
计算机\HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\ProfileList\
```

<img src="https://i.loli.net/2019/05/20/5ce240cebeef723095.png" alt="修改注册表.png" title="修改注册表.png" height="50%" width="50%" />



然后`注销`，登录临时管理员用户，进行用户名的修改。

<img src="https://i.loli.net/2019/05/20/5ce2427a70ce023282.png" alt="注销用户.png" title="注销用户.png" height="30%" width="30%"/>



注销之后，需要重新输入登录密码登录（如果设置了开机密码的话）

系统自动建立临时管理员账号`TempUser`登录

然后登陆之后，会有一个弹窗，说无法登陆当前账户，因为你修改了账户内容，但是还没有生效，点击`关闭`。

<img src="https://i.loli.net/2019/05/20/5ce23caa1aafa61398.png" alt="注销登录提示.png" title="注销登录提示.png" height="50%" width="50%"/>



这个时候我们是以临时管理员账户登录的，所以Windows桌面是默认的样式，也没什么内容。

我们打开下方的桌面文件夹图标，然后找到`C盘`，进入用户文件夹，这个时候会多出一个临时管理员用户文件夹，但是我们需要修改的是原来用户的那个文件夹.找到`ShibaInu`这个文件夹，然后修改为刚才在注册表那里修改的那个用户名，即`ipydev.com`，这个时候是可以修改的了，修改完之后，注销或者重启电脑。

<img src="https://i.loli.net/2019/05/20/5ce23ca9d5f2615920.png" alt="临时用户.png" title="临时用户.png" height="50%" width="50%"/>



<img src="https://i.loli.net/2019/05/20/5ce23ca9ea33284514.png" alt="临时用户修改用户名.png" title="临时用户修改用户名.png" height="50%" width="50%"/>



## 新用户

完成上述操作之后，重启或者注销，然后登录，可以看到还是原来的界面，这个时候我们打开`cmd`和查看c盘下的用户文件夹，查看是否修改成功

<img src="https://i.loli.net/2019/05/20/5ce23ca9e931b57189.png" alt="修改后用户名.png" title="修改后用户名.png" height="50%" width="50%" />



<img src="https://i.loli.net/2019/05/20/5ce23ca9ea15878202.png" alt="用户名.png" title="用户名.png" height="50%" width="50%" />

这里显示都是修改成功的了。这样大家就可以随时修改用户名了。

但是登录的时候，登录界面显示的还是管理员名称



---

为了让大家理解整个操作过程，这里我给了详细的截。

如果大家有其他问题可以在下方评论。











