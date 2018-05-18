## 简介

在线教育系统Demo

注释很详细，都在代码里，可以作为Django入门项目之一

如果你觉得还不错，帮我点个star吧

### 环境
- Python 3.6
- Django 1.11
- MySQL 5.7
- 安装环境 `pip install -r requirements.txt`



### 依赖
其他依赖在`requirements.txt`中了  

安装依赖库  
`pip install -r requirements.txt`

如果有需要，你也生成这样一个依赖  
`pip freeze >./requirements.txt`

如果CentOS 7出现mysqlclient安装失败，则先安装
```
yum install gcc mariadb-devel
然后在安装
pip install mysqlclient
```

### 数据库
除了依赖和settings之外，还没有建数据库和表

所以，运行migrate命令，创建数据库和数据表吧

```python
python manage.py makemigrations

python manage.py migrate
```