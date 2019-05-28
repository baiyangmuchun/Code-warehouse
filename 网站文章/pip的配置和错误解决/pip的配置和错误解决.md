## pip的配置和错误解决

## 更新pip

```python
python -m pip install --upgrade pip
```



## pip安装包报错

```python
ERROR: Could not install packages due to an EnvironmentError: [WinError 5] 拒绝访问。: 'C:\\Program Files\\Python36\\Lib\\site-packages\\kivy.deps.gstreamer-0.1.15.dist-info'
Consider using the `--user` option or check the permissions.
```

使用管理员打开 `cmd`可以解决



## 配置 pip 国内源

`win + S`打开“文件资源管理器” 地址栏 输入 `%APPDATA% `按回车，打开程序自定义设置文件夹，然后，创建名为 `pip`  的文件夹，用于存放 pip 配置文件 `pip.ini`

```ini
# 配置阿里云 pip 源

[global]
index-url=http://mirrors.aliyun.com/pypi/simple/
 
[install]
trusted-host=mirrors.aliyun.com
```

<img src="https://i.loli.net/2019/05/28/5cece3c00be0129981.png" alt="pip配置.png" title="pip配置.png" height="50%" width="50%"/>



测试：安装kivy.deps.gstreamer，大概是100M左右

`python -m pip install kivy.deps.gstreamer`

<img src="https://i.loli.net/2019/05/28/5cece3c001a2940443.png" alt="测试pip.png" title="测试pip.png" height="50%" width="50%"/>



---

到这里就结束了，有其他问题后续再更新

