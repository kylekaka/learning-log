# 学习笔记项目
最近读《Python编程从入门到实践》这本书，书里有一个Django的实践项目，自己就开始动手跟着做一下这个项目。
这个项目是一个在线日志系统，能够让用户记录所学习的各种主题的知识。
另外利用selenium完成了主要功能点的自动化测试，还有尝试编写了简单的单元测试代码。
现在基本上已经完成，并将它推送到github上留作备份和分享。
github网址：https://github.com/kylekaka/learning-log

# 项目部署方法

## 1.使用git clone源代码
使用下面命令复制源代码到你本机上：
```
$ git clone
```

## 2.在本地开发环境运行
新建虚拟环境：
```
$ virtualenv ll_env
```
然后激活虚拟环境：
```
$ source ll_env/bin/activate
```
使用pip命令安装依赖的包，需要安装的包名称在“requirements.txt”文件中，建议一个一个的安装每个第三方包。
```
$ sudo pip3 install Django
```
创建数据库：
```
$ python3 manage.py migrate
```
运行服务：
```
$ python3 manage.py runserver
```
最后打开浏览器，输入网址：http://localhost:8000/； 
来查看项目首页。

## 3.利用heroku部署到线上
请参考《利用Heroku部署Django web应用》，链接：https://my.oschina.net/u/3247573/blog/832351

## 4.使用Jenkins进行持续集成
TODO
