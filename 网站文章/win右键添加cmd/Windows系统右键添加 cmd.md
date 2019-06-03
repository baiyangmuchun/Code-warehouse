## win右键添加cmd

win10 下`shift + 右键`不能打开cmd，只能打开powershell，而我希望能够打开`cmd`，所以自己折腾一下，最后通过修改注册表文件实现了。

## 注册表文件

notepad++新建文件并修改为`cmd.reg`

```C
Windows Registry Editor Version 5.00
 
[HKEY_LOCAL_MACHINE\SOFTWARE\Classes\Directory\background\shell\cmd_here]
@="在此处打开命令行"
"Icon"="cmd.exe"
 
[HKEY_LOCAL_MACHINE\SOFTWARE\Classes\Directory\background\shell\cmd_here\command]
@="\"C:\\Windows\\System32\\cmd.exe\""
 
[HKEY_LOCAL_MACHINE\SOFTWARE\Classes\Folder\shell\cmdPrompt]
@="在此处打开命令行"
 
[HKEY_LOCAL_MACHINE\SOFTWARE\Classes\Folder\shell\cmdPrompt\command]
@="\"C:\\Windows\\System32\\cmd.exe\" \"cd %1\""
 
[HKEY_LOCAL_MACHINE\SOFTWARE\Classes\Directory\shell\cmd_here]
@="在此处打开命令行"
"Icon"="cmd.exe"
 
[HKEY_LOCAL_MACHINE\SOFTWARE\Classes\Directory\shell\cmd_here\command]
@="\"C:\\Windows\\System32\\cmd.exe\""
```

PS：@="此处打开命令行"  该引号内文字可以随意修改成你想要显示的文字）

最后，双击注册，点击确定就可以了

## 效果预览

- shift + 右键

<img src="https://i.loli.net/2019/05/28/5cec897cd372563715.png" alt="shift右键cmd.png" title="shift右键cmd.png" height="30%" width="30%"/>

- 右键

<img src="https://i.loli.net/2019/05/28/5cec897cd35c184617.png" alt="右键cmd.png" title="右键cmd.png" height="30%" width="30%"/>



---

现在可以更愉快的使用 cmd 了

另一个快捷的启动cmd：win + R ,输入cmd（这个不可以直接定位到当前位置）



大家有其他问题在下方留言吧。