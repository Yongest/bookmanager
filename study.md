安装Python时，出现pip不是命令的情况。
sogou--->下载python

新买的服务器：
apt-get install nginx 时出现Unable to locate package
sudo apt-get update， 这命令作用是：同步 /etc/apt/sources.list 和 /etc/apt/sources.list.d 中列出的源的索引，这样才能获取到最新的软件包。
    ```
        /usr/sbin/nginx  #主程序
        /etc/nginx   #存放配置文件
        /usr/share/nginx  #存放静态文件
        /var/log/nginx  #存放日志
    ```
修改数据库引擎后，运行 python manage.py makemigrations 报错    
RuntimeError: 'cryptography' package is required for sha256_password or caching_sha2_password auth methods
pip install cryptography

在同一平级目录中引入模块报错，没有找到这个模块

echo $HOME   $HOME 代表是你用来登录的那个用户的家目录
lsb_release -a  查看版本信息

cd /etc/apt 
ls
sources.list 备注、镜像源、修改镜像
sudo apt-get update 更新
使用其他源下载
我们可以直接在pip命令中使用-i参数来指定镜像地址，例如：
pip install pyinstaller -i https://pypi.tuna.tsinghua.edu.cn/simple