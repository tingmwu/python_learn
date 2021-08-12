# ubuntu18.04 搭建ROS环境

***安装参考：***

[在 Ubuntu 中安装 ROS Melodic](http://wiki.ros.org/cn/melodic/Installation/Ubuntu)

[ROS入门教程-安装并配置ROS环境（melodic版本）](https://www.ncnynl.com/archives/201906/3147.html)

## 1. 安装
### 1.1 设置sources.list
```sh
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'

# 如果下载缓慢也可以使用国内镜像源（推荐）
sudo sh -c '. /etc/lsb-release && echo "deb http://mirrors.tuna.tsinghua.edu.cn/ros/ubuntu/ `lsb_release -cs` main" > /etc/apt/sources.list.d/ros-latest.list' # 清华镜像源
```

### 1.2 设置密钥
```sh
sudo apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654

# 若无法连接到密钥服务器，可以尝试替换上面命令中的 hkp://keyserver.ubuntu.com:80 为 hkp://pgp.mit.edu:80 。

# 你也可以使用curl命令替换apt-key命令，这在使用代理服务器的情况下比较有用：
curl -sSL 'http://keyserver.ubuntu.com/pks/lookup?op=get&search=0xC1CF6E31E6BADE8868B172B4F42ED6FBAB17C654' | sudo apt-key add -
```

### 1.3 安装
```sh
sudo apt update

# 桌面完整版（推荐）： : 包含 ROS、rqt、rviz、机器人通用库、2D/3D 模拟器、导航以及 2D/3D 感知包。
sudo apt install ros-melodic-desktop-full

# 桌面版： 包含 ROS，rqt，rviz 和机器人通用库
sudo apt install ros-melodic-desktop

# ROS-基础包： 包含 ROS 包，构建和通信库。没有图形界面工具。
sudo apt install ros-melodic-ros-base

# 单独的包： 你也可以安装某个指定的ROS软件包（使用软件包名称替换掉下面的PACKAGE）：
sudo apt install ros-melodic-PACKAGE
```
### 1.4 安装依赖
```sh
sudo apt-get install python-rosdep python-rosinstall python-rosinstall-generator python-wstool build-essential
```
### 1.5 初始化 rosdep
```sh
sudo rosdep init
rosdep update

# 如果出现问题，直接跳到后面问题解决
```

### 1.6 设置环境
```sh
echo "source /opt/ros/melodic/setup.bash" >> ~/.bashrc
source ~/.bashrc

# 如果你不只安装了一个 ROS 发行版， ~/.bashrc 只能使用你需要的 ROS 版本的 setup.bash 。

# 如果你只想设置当前 bash 会话的 ROS 环境变量，只需要输入：
source /opt/ros/melodic/setup.bash

# 如果你使用 zsh，那么你需要将上述命令改为：
echo "source /opt/ros/melodic/setup.zsh" >> ~/.zshrc
source ~/.zshrc
```

### 1.7 启动测试
```sh
roscore

# 若正常出现以下信息，说明已经成功安装
   .. logging to /home/ubuntu/.ros/log/cb38e680-dee2-11ea-bae1-70665563e003/roslaunch-nx-1205.log
Checking log directory for disk usage. This may take a while.
Press Ctrl-C to interrupt
Done checking log file disk usage. Usage is <1GB.

started roslaunch server http://nx:36773/
ros_comm version 1.14.7


SUMMARY
========

PARAMETERS
 * /rosdistro: melodic
 * /rosversion: 1.14.7

NODES

auto-starting new master
process[master]: started with pid [1215]
ROS_MASTER_URI=http://nx:11311/

setting /run_id to cb38e680-dee2-11ea-bae1-70665563e003
process[rosout-1]: started with pid [1228]
started core service [/rosout]
```

## 2. 安装过程中问题解决
```
主要是1.5步骤初始化rosdep时出现问题
例如：
sudo rosdep init会出现：
rosdep init/rosdep update error:timeout

rosdep update
ERROR：cannot downlaod default sources list from: xxxxxx
ERROR: unable to process source [https://raw.githubusercontent.com xxx
这两个问题本质上都是一个问题，网络问题
```
*对于以上这些单独的问题，网上有很多种方法，根据网上的反馈，不同的电脑、网络环境效果都不一样，但最后还是靠 [rosdep init/rosdep update error:timeout](https://www.guyuehome.com/34072) 才解决的*

先针对单独的问题说一下网上的解决方案：

### 2.1 对于**sudo rosdep init**出现的问题

- 第一种方法：[sudo rosdep init ERROR: cannot download default sources list from:【closed】](https://blog.csdn.net/u013468614/article/details/102917569)
```sh
#打开hosts文件
sudo vi /etc/hosts

#在文件末尾添加
151.101.84.133  raw.githubusercontent.com

#保存后退出再尝试
```
- 第二种方法：[ROS:sudo rosdep init出错常规方法都无效后解决办法记录](https://zhuanlan.zhihu.com/p/77483614)
```sh
# 手动下载20-default.list文件到 /etc/ros/rosdep/sources.list.d/
wget https://raw.githubusercontent.com/ros/rosdistro/master/rosdep/sources.list.d/20-default.list
# 注意sudo rosdep init失败时，/etc下并没有/ros目录，需要依次逐级新建,然后将20-default.list 拷贝到 /etc/ros/rosdep/sources.list.d/

```
### 2.2 对于**rosdep update**出现的问题
这个问题有很多说是网络问题：

- 方法1：更换DNS
```sh
vi /etc/resolv.conf

# 添加谷歌DNS
nameserver 8.8.8.8
nameserver 8.8.8.4
```
- 方法2：切换网络

*就是切换不同的网络，或者使用手机热点，然后不停的执行 rosdep update，反正就是比较佛系*

- 方法3：修改/etc/ros/rosdep/sources.list.d/20-default.list中的链接

    *因为rosdep update本质就是从20-default.list的链接中下载文件，更新失败是因为文件里指向的链接无法访问，所以修改为能访问的链接就可以了*

文件20-default.list源内容
```sh
# os-specific listings first
yaml https://raw.githubusercontent.com/ros/rosdistro/master/rosdep/osx-homebrew.yaml osx

# generic
yaml https://raw.githubusercontent.com/ros/rosdistro/master/rosdep/base.yaml
yaml https://raw.githubusercontent.com/ros/rosdistro/master/rosdep/python.yaml
yaml https://raw.githubusercontent.com/ros/rosdistro/master/rosdep/ruby.yaml
gbpdistro https://raw.githubusercontent.com/ros/rosdistro/master/releases/fuerte.yaml fuerte
```
将所有raw.githubusercontent.com改为raw.github.com,得到如下最终文档：
```sh
# os-specific listings first
yaml https://raw.github.com/ros/rosdistro/master/rosdep/osx-homebrew.yaml osx

# generic
yaml https://raw.github.com/ros/rosdistro/master/rosdep/base.yaml
yaml https://raw.github.com/ros/rosdistro/master/rosdep/python.yaml
yaml https://raw.github.com/ros/rosdistro/master/rosdep/ruby.yaml
gbpdistro https://raw.github.com/ros/rosdistro/master/releases/fuerte.yaml fuerte
```

### 2.3 **终极解决办法**
参考：[rosdep init/rosdep update error:timeout](https://www.guyuehome.com/34072)

*这个方法本质就是提前将 rosdep update 过程中需要下载的文件提前下载下来，再修改下载的链接地址为本地文件*
```sh
# 1. 手动下载rosdistro文件
git clone https://github.com/ros/rosdistro.git

# 2. 下载之后会得到一个 rosdistro 文件夹， 然后将该文件夹复制到 ros目录
sudo cp -r ./rosdistro /etc/ros/rosdep/sources.list.d/

# 3. 然后分别修改以下三个文件

# 第一个文件
sudo vi /usr/lib/python2.7/dist-packages/rosdep2/sources_list.py
# 将其中的资源路径改为离线路径
DEFAULT_SOURCES_LIST_URL = 'file:/etc/ros/rosdep/sources.list.d/20-default.list'

# 第二个文件
sudo vi /usr/lib/python2.7/dist-packages/rosdep2/rep3.py
# 将其中的资源路径改为离线路径
REP3_TARGETS_URL = 'file:/etc/ros/rosdep/sources.list.d/rosdistro/releases/targets.yaml'

# 第三个文件
sudo vi /usr/lib/python2.7/dist-packages/rosdistro/__init__.py
 
DEFAULT_INDEX_URL = 'file:/etc/ros/rosdep/sources.list.d/rosdistro/index-v4.yaml'

# 4. 下载20-default.list文件到 /etc/ros/rosdep/sources.list.d/
wget https://raw.githubusercontent.com/ros/rosdistro/master/rosdep/sources.list.d/20-default.list

vi /etc/ros/rosdep/sources.list.d/20-default.list

# 修改链接为本地路径
# os-specific listings first
# yaml https://raw.githubusercontent.com/ros/rosdistro/master/rosdep/osx-homebrew.yaml osx
yaml file:/etc/ros/rosdep/sources.list.d/rosdistro/rosdep/osx-homebrew.yaml osx

# generic
# yaml https://raw.githubusercontent.com/ros/rosdistro/master/rosdep/base.yaml
# yaml https://raw.githubusercontent.com/ros/rosdistro/master/rosdep/python.yaml
# yaml https://raw.githubusercontent.com/ros/rosdistro/master/rosdep/ruby.yaml
# gbpdistro https://raw.githubusercontent.com/ros/rosdistro/master/releases/fuerte.yaml fuerte
yaml file:/etc/ros/rosdep/sources.list.d/rosdistro/rosdep/base.yaml
yaml file:/etc/ros/rosdep/sources.list.d/rosdistro/rosdep/python.yaml
yaml file:/etc/ros/rosdep/sources.list.d/rosdistro/rosdep/ruby.yaml
gbpdistro file:/etc/ros/rosdep/sources.list.d/rosdistro/releases/fuerte.yaml fuerte

# newer distributions (Groovy, Hydro, ...) must not be listed anymore, they are being fetched from the rosdistro index.yaml instead
```

