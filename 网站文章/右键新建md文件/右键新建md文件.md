## 右键新建md文件

在 **HKEY_CLASSES_ROOT** 下面添加一个`.md `的子项即可实现（需要导入注册表信息）

## 记事本打开

这是一个用 `记事本`打开md文件的注册表文件：

```c
Windows Registry Editor Version 5.00

[HKEY_CLASSES_ROOT\.md]
@="MarkdownFile"
"PerceivedType"="text"
"Content Type"="text/plain"

[HKEY_CLASSES_ROOT\.md\ShellNew]
"NullFile"=""

[HKEY_CLASSES_ROOT\MarkdownFile]
@="Markdown File"

[HKEY_CLASSES_ROOT\MarkdownFile\DefaultIcon]
@="%SystemRoot%\system32\imageres.dll,-102"

[HKEY_CLASSES_ROOT\MarkdownFile\shell]

[HKEY_CLASSES_ROOT\MarkdownFile\shell\open]

[HKEY_CLASSES_ROOT\MarkdownFile\shell\open\command]
@="%SystemRoot%\system32\NOTEPAD.EXE %1"
```


导入之后是这个效果：

<img src="https://i.loli.net/2019/05/27/5ceb5abdd352f76175.jpg" alt="记事本md.jpg" title="记事本md.jpg" height="50%" width="50%"/>

## Typora打开

如果装了其他的 markdown编辑器的话只要把 **.md** 这个项的值改成对应的类型就好了 比如我装的是 **Typora** 直接导入下面这个注册表文件:

```c
Windows Registry Editor Version 5.00

[HKEY_CLASSES_ROOT\.md]
@="TyporaMarkdownFile"
"PerceivedType"="text"
"Content Type"="text/plain"

[HKEY_CLASSES_ROOT\.md\ShellNew]
"NullFile"=""
```
<img src="https://i.loli.net/2019/05/27/5ceb5abdde7a957471.png" alt="Typora打开.png" title="Typora打开.png" height="50%" width="50%"/>

## 操作方法

- 直接将相应的代码复制下来，然后新建一个 TXT 文本文件，使用 notepad++ 等文本编辑器打开，将代码复制进去，然后另存为`md.reg`文件，注意后缀名是 reg ，文件名为任意都可以，建议使用英文文件名。或者保存之后再修改文件名和后缀名也可以。（或者直接新建一个文本文件，修改文件名和后缀为 md.reg ,然后使用 Notepad++打开，复制代码进去保存即可）
- 最后以 管理员身份 打开编辑好的 reg 文件，点击确定，即可实现右键新建一个 md 文件的快捷键。



---

有其他问题可以在下面留言



推荐阅读：[Markdown 编辑器Typora](https://ipydev.com/article/18/)





