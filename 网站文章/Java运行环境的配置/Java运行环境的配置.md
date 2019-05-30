## Java运行环境的配置

## JDK JRE简介

Java运行环境，即需要安装`JDK`或者`JRE`
下面简单介绍一下 `JDK` 和 `JRE` 吧

> JRE： Java Runtime Environment
> JDK：Java Development Kit<br>
> JRE顾名思义是java运行时环境，包含了java虚拟机，java基础类库。是使用java语言编写的程序运行所需要的软件环境，是提供给想运行java程序的用户使用的。<br>
> JDK顾名思义是java开发工具包，是程序员使用java语言编写java程序所需的开发工具包，是提供给程序员使用的。JDK包含了JRE，同时还包含了编译java源码的编译器javac，还包含了很多java程序调试和分析的工具：jconsole，jvisualvm等工具软件，还包含了java程序编写所需的文档和demo例子程序。<br>
> 如果你需要运行java程序，只需安装JRE就可以了。如果你需要编写java程序，需要安装JDK。<br>
> JRE根据不同操作系统（如：windows，linux等）和不同JRE提供商（IBM,ORACLE等）有很多版本，最常用的是Oracle公司收购SUN公司的JRE版本。



## JDK下载

下载：[官网下载](https://www.oracle.com/technetwork/java/javase/downloads/index.html)

<img src="https://i.loli.net/2019/05/20/5ce28a49aef9458864.png" alt="下载JDK&JRE.png" title="下载JDK&JRE.png" width="50%" height="50%"/>



下面我们只安装`JDK`即可，因为会同时安装`JRE`

- [JDK-Java SE Development Kit 10.0.2下载](https://www.oracle.com/technetwork/java/javase/downloads/jdk10-downloads-4416644.html)

<img src="https://i.loli.net/2019/05/20/5ce28a49afb7587768.png" alt="下载JDK.png" title="下载JDK.png" width="50%" height="50%"/>



## 安装JDK

选择安装目录，其中安装过程中会出现两次提示 。
①安装 jdk ，②安装 jre 。
个人建议两个安装在同一文件夹的不同子文件夹中。
因为 `jdk` 和 `jre` 不能安装在同一文件夹的根目录下，`jdk` 和 `jre` 安装在同一文件夹极易出错。按照下面步骤操作即可。

<img src="https://i.loli.net/2019/05/20/5ce28a49867b411007.png" alt="安装JDK1.png" title="安装JDK1.png" width="50%" height="50%"/>

<img src="https://i.loli.net/2019/05/20/5ce28a49907a892615.png" alt="安装JDK2.png" title="安装JDK2.png" width="50%" height="50%"/>

<img src="https://i.loli.net/2019/05/20/5ce28a498e48244526.png" alt="安装JDK3.png" title="安装JDK3.png" width="50%" height="50%"/>

此时安装已经完成。



## 环境变量配置

环境变量配置：这里以Windows 10 为例子，其他Windows系统也是类似的。

- 环境变量配置（均在`系统变量`下操作）
  - 右键`此电脑`→`属性`→`高级系统设置`→`环境变量`
  - ①新建`JAVA_HOME` 系统变量，变量值是jdk的安装目录。「上面我设置的JDK安装目录为`C:\Program Files\Java\jdk-10.0.2`」
  - ②新建 `CLASSPATH` 系统变量，变量填写 `.;%JAVA_HOME%\lib;%JAVA_HOME%\lib\tools.jar`（注意最前面有一点）
  - ③寻找 `Path` 变量→`编辑`，变量值最后输入 `%JAVA_HOME%\bin;%JAVA_HOME%\jre\bin;`
    注意原有的变量值后面没有 `;` 号的话，得加上去。
  - ④全部`确定`,退出
  - ⑤系统变量配置完成。

<img src="https://i.loli.net/2019/05/20/5ce28a49afb3612607.png" alt="配置环境变量1.png" title="配置环境变量1.png" width="50%" height="50%"/>

<img src="https://i.loli.net/2019/05/20/5ce28a49b06ac58163.png" alt="配置环境变量2.png" title="配置环境变量2.png" width="50%" height="50%"/>

<img src="https://i.loli.net/2019/05/20/5ce28a49b851315937.png" alt="配置环境变量3.png" title="配置环境变量3.png" width="50%" height="50%"/>

- 检验是否配置成功
  - `win + R`输入`cmd`进入命令提示符交互模式
  - 输入`java --version`（注：java 和 --version 之间有空格）
  - 出现如下图所示表示配置成功

<img src="https://i.loli.net/2019/05/20/5ce28a49a906143508.png" alt="配置环境变量4.png" title="配置环境变量4.png" width="50%" height="50%"/>

- 这样配置好之后，就可以写Java程序了，也可以配置`Eclipse + PyDev`编写 Python程序.



---

win7的话配置过程是一样的，只是win7在配置过程的那个窗口稍微难看一点。



大家配置过程遇到其他问题也可以在下方评论留言。

