# ubuntu部署seafile服务端

## 1. 安装docker

[官方文档](https://docs.docker.com/engine/install/ubuntu/)
_分为 apt 安装和 dpkg 本地安装两种方式_（**推荐本地安装**）

### _Install using the repository_

```bash
sudo apt-get update
sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg-agent \
    software-properties-common

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

sudo apt-key fingerprint 0EBFCD88

sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"

# 安装最新版本
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io

# 查看可安装的docker版本
apt-cache madison docker-ce # 

# 安装特定版本
sudo apt-get install docker-ce=<VERSION_STRING> docker-ce-cli=<VERSION_STRING> containerd.io

```

### _Install from a package_

**一般apt安装docker-ce的下载过程会很慢，可以去**<https://download.docker.com/linux/ubuntu/dists/>**下载之后安装**

* > cat /etc/\*release\* # 查看系统版本</br>
* 进入网站之后选择对应的系统版本文件夹，进入pool/stable/，选择amd64, armhf, or arm64之后，选择想要安装的版本的docker-ce docker-ce-cli contaided.io下载后用如下命令安装。
* > dpkg -i docker-ce\*.deb 

### Install using convenience script

You can run the script with the `DRY_RUN=1` option to learn what steps the script will execute during installation:

```
curl -fsSL https://get.docker.com -o get-docker.sh
$ DRY_RUN=1 sh ./get-docker.sh
```
### docker换源
Docker 使用 /etc/docker/daemon.json（Linux） 或者 %programdata%\docker\config\daemon.json（Windows） 来配置 Daemon。
```bash
{ 
    "registry-mirrors": [
        "https://docker.mirrors.ustc.edu.cn",
        "https://registry.docker-cn.com",
        "https://cr.console.aliyun.com/"]
}
```

[参考](https://lug.ustc.edu.cn/wiki/mirrors/help/docker/)



## 2. docker-compose部署

[官方文档](https://cloud.seafile.com/published/seafile-manual-cn/docker/%E7%94%A8Docker%E9%83%A8%E7%BD%B2Seafile.md)

1. 安装docker-compose

   > sudo apt-get update
   >
   > sudo apt-get install docker-compose

2. 配置docker-compose.yml 
   docker-compose.yml下载路径 [社区版](https://docs.seafile.com/d/cb1d3f97106847abbf31/files/?p=/docker/docker-compose.yml) [专业版](https://docs.seafile.com/d/cb1d3f97106847abbf31/files/?p=/docker/pro-edition/docker-compose.yml)

   需要配置的部分文档中都会有# Requested的注释，注意seafile一栏下的端口- "80:80"(前面的80为服务器端口，后面的80为docker内部端口，一般按需要修改前一个80端口，比如这里修改为- "8000:80")

3. 启动docker

   > docker-compose up -d # -d是后台运行，如果想要看运行信息，可以不加

   **运行问题：** ERROR: Couldn't connect to Docker daemon at http+docker://localunixsocket - is it running?
   **解决办法：** 将当前用户加入docker组

   > sudo gpasswd -a ${USER} docker 
   或者
   > sudo usermod -aG docker $USER

   然后切换到其它用户，再切换回来就正常了。
   **参考：**[解决 ERROR: Couldn't connect to Docker daemon at http+docker://localunixsocket - is it running?](https://blog.csdn.net/xiojing825/article/details/79494408)

4. 网页端配置
   * 登录云服务器控制台开放端口，比如我在步骤2中配置的端口为8000；
   * 打开网页 <http://yourip:8000，输入账号密码登录；>
   * 点击头像->系统设置->设置，分别修改**SERVICE_URL**与**FILE_SERVER_ROOT**为<http://yourip:8000>和<http://yourip:8000/seafhttp>(注意这里一定要填对端口，默认没有端口是因为默认为80端口，在http中可以省略，如果步骤2中修改了端口，这里一定要进行修改，否则客户端无法登录以及正常的上传文件)；

## 3. 其它问题

### 1. **文件历史页面Page unavailable**

**分析**：查看seafile/log/seahub.log，显示AttributeError: 'NoneType' object has no attribute 'get_file_history_suffix'

**原因**：从专业版更换到社区版，专业版的配置文件没有删除

**解决办法**：删除seafile/conf目录下的seafevents.conf文件，重新启动seafile和seahub

[参考:Failed to view file’s history](https://forum.seafile.com/t/resolved-failed-to-view-files-history/9743/2)


# 2. seafile数据迁移
## 1. 源服务器端备份
我们假设您的 seafile 数据卷路径是 /opt/seafile-data，并且您想将备份数据存放到 /opt/seafile-backup 目录下。

您可以创建一个类似以下 /opt/seafile-backup 的目录结构：
```
/opt/seafile-backup

---- databases/  用来存放 MySQL 容器的备份数据

---- data/  用来存放 Seafile 容器的备份数据
```
要备份的数据文件：
```
# 注意这里的conf目录内的文件是配置文件，需要备份，但是环境不同时，不能在新的服务器上进行恢复，否则会page-unavailable，只是作为参考
/opt/seafile-data/seafile/conf  # configuration files

/opt/seafile-data/seafile/seafile-data # data of seafile

/opt/seafile-data/seafile/seahub-data # data of seahub
```

- 备份数据库
```
# 建议每次将数据库备份到一个单独的文件中。至少在一周内不要覆盖旧的数据库备份。

cd /opt/seafile-backup/databases

docker exec -it seafile-mysql mysqldump  -uroot -p[passwd] --opt ccnet_db > ccnet_db.sql

docker exec -it seafile-mysql mysqldump  -uroot -p[passwd] --opt seafile_db > seafile_db.sql

docker exec -it seafile-mysql mysqldump  -uroot -p[passwd] --opt seahub_db > seahub_db.sql

# 注意备份数据库时加上-p[passwd], [passwd]为你的mysql密码，官方教程没有加，实际恢复时无法恢复数据库
```

- 备份 Seafile 资料库数据
```
# 方法1 cp 复制
cp -R /opt/seafile-data/seafile /opt/seafile-backup/data/

# 方法2 rsync增量备份
rsync -az --delete /opt/seafile-data/seafile /opt/seafile-backup/data/

# --delete 参数是让目标目录与源目录保持完全一致，如果不加，源目录中删除的文件，目标目录仍会保留，可根据自己情况选择。
# -z 是在传输过程中压缩数据，对于文件类文件能够有效提高效率
```

## 2. 目标服务器恢复数据
- 恢复数据库
```
docker cp /opt/seafile-backup/databases/ccnet_db.sql seafile-mysql:/tmp/ccnet_db.sql
docker cp /opt/seafile-backup/databases/seafile_db.sql seafile-mysql:/tmp/seafile_db.sql
docker cp /opt/seafile-backup/databases/seahub_db.sql seafile-mysql:/tmp/seahub_db.sql

docker exec -it seafile-mysql /bin/sh -c "mysql -uroot -p[passwd] ccnet_db < /tmp/ccnet_db.sql"
docker exec -it seafile-mysql /bin/sh -c "mysql -uroot -p[passwd] seafile_db < /tmp/seafile_db.sql"
docker exec -it seafile-mysql /bin/sh -c "mysql -uroot -p[passwd] seahub_db < /tmp/seahub_db.sql"

# 同1中也要加上-p[passwd]，否则会没有访问权限
```

- 恢复数据
```
rsync -az --delete /opt/seafile-backup/data/seafile/seafile-data /opt/seafile-data/seafile/
rsync -az --delete /opt/seafile-backup/data/seafile/seahub-data /opt/seafile-data/seafile/
```

## 3. 其它问题
- 迁移数据后，新的seafile服务器启动后，无法访问文件
```
具体描述: 网页端上传下载文件，显示Bad access token

docker-compose up 查看log显示：
Error: the user running the script ("root") is not the owner of "/shared/seafile/seafile-data" folder

解决办法：修改 /opt/seafile-data的所有者为root
sudo chown -R root /opt/seafile-data
```

**参考**：
[Docker部署seafile](https://cloud.seafile.com/published/seafile-manual-cn/docker/%E7%94%A8Docker%E9%83%A8%E7%BD%B2Seafile.md)
[迁移本地Seafile到docker](https://bbs.seafile.com/t/topic/10958)





## onlyoffice部署问题

[OnlyOffice 打开文档时提示下载失败](https://blog.csdn.net/m0_53401243/article/details/133869439)

[配置onlyoffice](https://cloud.seafile.com/published/seafile-manual-cn/deploy/only_office.md)

[令牌错误](https://bbs.seafile.com/t/topic/16165/15)

