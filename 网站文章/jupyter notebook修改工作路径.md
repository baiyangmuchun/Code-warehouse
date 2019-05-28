## jupyter notebook修改工作路径

最近换了电脑，所以需要重新安装 anaconda，然后自然也就是需要修改 `jupyter notebook`的工作路径



## 打开jupyter notebook

直接打开或者在命令行输入`jupyter notebook`（加入了系统路径的情况下）

如果没有直接弹出浏览器窗口，那么重新选择默认浏览器即可



## 修改工作路径

操作方法：

1 选择一个用于存放config文件的文件夹

2 在cmd中进入该文件夹的路径

3在cmd中 输入命令`jupyter notebook --generate-config`

4 此时在该文件夹中便生成一个notebook的config文件，文件名是“jupyter_notebook_config.py”

5 打开该文件，修改

`# The directory to use for notebooks and kernels`下面的

`# c.NotebookApp.notebook_dir = ""`为

`c.NotebookApp.notebook_dir = "指定的工作路径"`（注意将#号删除）

------

配置文件位置 (默认)
`C:\Users\用户名.jupyter\jupyter_notebook_config.py`

如果选择了存放路径，那么配置文件就在这个存放路径下



## 其他更多的配置

其他的配置也同样是修改这个配置文件，具体操作可以参考文档：[Jupyter官网](https://jupyter.org/)



---

其他问题可以在下面留言