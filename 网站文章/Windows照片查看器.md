## Windows照片查看器

因为现在的 Windows 10是没有`照片查看器`的

但是我还是觉得以前的这个自带的图片查看软件好用

下面说说如何找回这个软件



## 修改注册表

新建一个文件`photo.reg`

写入下面的代码并保存

````c
Windows Registry Editor Version 5.00

 ; Change Extension's File Type

 [HKEY_CURRENT_USER\Software\Classes\.jpg]

 @="PhotoViewer.FileAssoc.Tiff"

 ; Change Extension's File Type

 [HKEY_CURRENT_USER\Software\Classes\.jpeg]

 @="PhotoViewer.FileAssoc.Tiff"

 ; Change Extension's File Type

 [HKEY_CURRENT_USER\Software\Classes\.gif]

 @="PhotoViewer.FileAssoc.Tiff"

 ; Change Extension's File Type

 [HKEY_CURRENT_USER\Software\Classes\.png]

 @="PhotoViewer.FileAssoc.Tiff"

 ; Change Extension's File Type

 [HKEY_CURRENT_USER\Software\Classes\.bmp]

 @="PhotoViewer.FileAssoc.Tiff"

 ; Change Extension's File Type

 [HKEY_CURRENT_USER\Software\Classes\.tiff]

 @="PhotoViewer.FileAssoc.Tiff"

 ; Change Extension's File Type

 [HKEY_CURRENT_USER\Software\Classes\.ico]

 @="PhotoViewer.FileAssoc.Tiff"
````

然后双击打开，下面一路确认就可以了



## 使用

在`设置`→`默认程序`里选择`Windows照片查看器`为默认的照片查看器即可



现在也可以在图片打开方式里看到有`Windows照片查看器`了



---

有其他问题下方留言