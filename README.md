源：https://github.com/jiaran1315/start_GenshinImpact

# start_GenshinImpact
基于检测屏幕全白而运行原神的程序
* A program that runs Genshin Impact based on detecting that the screen is completely white
* 运行环境在Python3.11  其他版本自行测试


## 所运用的库
* PIL (Python Imaging Library，也称为 Pillow): 用于图像处理。
* pypiwin32：用于获取程序运行情况。
如果您没有安装上述库，您需要运行以下命令来安装它：
```pip
pip install Pillow
pip install pypiwin32
```

# 请修改config.ini文件
```ini
[Paths]
#填写原神文件所在路径
genshinimpact_path = 原神所在路径
```
