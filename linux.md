# linux学习

## apt 更换国内源

> *修改 /etc/apt/sources.list 文件即可，将内容更换为任意一种国内源即可*

**国内源：**

1.阿里源

```
deb-src http://archive.ubuntu.com/ubuntu xenial main restricted #Added by software-properties
deb http://mirrors.aliyun.com/ubuntu/ xenial main restricted
deb-src http://mirrors.aliyun.com/ubuntu/ xenial main restricted multiverse universe #Added by software-properties
deb http://mirrors.aliyun.com/ubuntu/ xenial-updates main restricted
deb-src http://mirrors.aliyun.com/ubuntu/ xenial-updates main restricted multiverse universe #Added by software-properties
deb http://mirrors.aliyun.com/ubuntu/ xenial universe
deb http://mirrors.aliyun.com/ubuntu/ xenial-updates universe
deb http://mirrors.aliyun.com/ubuntu/ xenial multiverse
deb http://mirrors.aliyun.com/ubuntu/ xenial-updates multiverse
deb http://mirrors.aliyun.com/ubuntu/ xenial-backports main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ xenial-backports main restricted universe multiverse #Added by software-properties
deb http://archive.canonical.com/ubuntu xenial partner
deb-src http://archive.canonical.com/ubuntu xenial partner
deb http://mirrors.aliyun.com/ubuntu/ xenial-security main restricted
deb-src http://mirrors.aliyun.com/ubuntu/ xenial-security main restricted multiverse universe #Added by software-properties
deb http://mirrors.aliyun.com/ubuntu/ xenial-security universe
deb http://mirrors.aliyun.com/ubuntu/ xenial-security multiverse
```

2.东北大学
```
deb-src http://mirror.neu.edu.cn/ubuntu/ xenial main restricted #Added by software-properties

deb http://mirror.neu.edu.cn/ubuntu/ xenial main restricted

deb-src http://mirror.neu.edu.cn/ubuntu/ xenial restricted multiverse universe #Added by software-properties

deb http://mirror.neu.edu.cn/ubuntu/ xenial-updates main restricted

deb-src http://mirror.neu.edu.cn/ubuntu/ xenial-updates main restricted multiverse universe #Added by software-properties

deb http://mirror.neu.edu.cn/ubuntu/ xenial universe

deb http://mirror.neu.edu.cn/ubuntu/ xenial-updates universe

deb http://mirror.neu.edu.cn/ubuntu/ xenial multiverse

deb http://mirror.neu.edu.cn/ubuntu/ xenial-updates multiverse

deb http://mirror.neu.edu.cn/ubuntu/ xenial-backports main restricted universe multiverse

deb-src http://mirror.neu.edu.cn/ubuntu/ xenial-backports main restricted universe multiverse #Added by software-properties

deb http://archive.canonical.com/ubuntu xenial partner deb-src http://archive.canonical.com/ubuntu xenial partner

deb http://mirror.neu.edu.cn/ubuntu/ xenial-security main restricted

deb-src http://mirror.neu.edu.cn/ubuntu/ xenial-security main restricted multiverse universe #Added by software-properties

deb http://mirror.neu.edu.cn/ubuntu/ xenial-security universe

deb http://mirror.neu.edu.cn/ubuntu/ xenial-security multiverse
```
3.清华大学
```
deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial main restricted

deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-updates main restricted

deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial universe

deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-updates universe

deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial multiverse

deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-updates multiverse

deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-backports main restricted universe multiverse

deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-security main restricted

deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-security universe deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-security multiverse
```
## pip更换国内源

> *linux下 Linux下，修改 ~/.pip/pip.conf。*
```sh
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple

[install]
trusted-host=pypi.tuna.tsinghua.edu.cn

# 或者
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```


> *windows下，直接在user目录中创建一个pip目录，如：C:\Users\xx\pip，新建文件pip.ini。内容同上。*



> 临时使用 ， pip install -i https://pypi.tuna.tsinghua.edu.cn/simple package

*其他国内源*
清华：https://pypi.tuna.tsinghua.edu.cn/simple

阿里云：http://mirrors.aliyun.com/pypi/simple/

中国科技大学 https://pypi.mirrors.ustc.edu.cn/simple/

华中理工大学：http://pypi.hustunique.com/

山东理工大学：http://pypi.sdutlinux.org/ 

豆瓣：http://pypi.douban.com/simple/

## 安装Anaconda后设置
**1. 设置环境变量**

*linux下*
```sh
vim ~/.bashrc # 当前用户生效
vim /etc/profile # 所有用户生效

export PATH=~/anaconda3/bin:$PATH  # 添加到文件末尾

source ~/.bashrc # 使环境变量生效
```

*Windows下*
```
添加以下路径到环境变量(你安装anaconda的路径)
D:\Anaconda3
D:\Anaconda3\Scripts
D:\Anaconda3\Library\bin
```

**2. conda换源**
```sh
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/

conda config --set show_channel_urls yes
```

*其他源：*
```sh
# 1. 中科大
conda config --add channels https://mirrors.ustc.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.ustc.edu.cn/anaconda/pkgs/main/
# 2.清华
conda config --add https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
```

**3. 设置conda默认环境**(不是必须)
```sh
vim ~/.bashrc
在文件末尾添加 source activate myenv 
```



# VS code通过SSH远程编辑服务器文件
## 1. 安装ssh环境
> 方法1：使用open ssh，win10可打开设置=>应用=>管理可选功能=>安装open sss客户端和服务器端
（**设置里找不到可[通过powershell安装](https://docs.microsoft.com/zh-cn/windows-server/administration/openssh/openssh_install_firstuse)**）

> 或者如果有git自带ssh，那么直接使用git

## 2. 生成公钥

*1.建立ssh信任(确认自己本机的公钥是否存在%USERPROFILE%\.ssh\id_rsa.pub,不存在就生成,命令是：*

> ssh-keygen -t rsa -P ''

**加上-P ''的意思是设置一个空密码，也可以不加，不加的话要按三次回车**


*2. 然后把公钥id_rsa.pub的内容追加到服务器/home/.ssh/authorized_keys文件里。**这样做不用每次启动vscode都输入密码了***

*公钥追加到服务器可以采用以下方式*
> scp /root/.ssh/id_rsa.pub root@192.168.1.181:/root/.ssh/authorized_keys

(**其中/root/.ssh/id_rsa.pub为你本地公钥路径；root为你的服务器用户名；192.168.1.181为你的服务器ip；**)

*3. authorized_keys的权限要是600!!!*
> chmod 600 /root/.ssh/authorized_keys

## 3. vs code连接
*1. 安装Remote SSH插件*

*2. 点击左下角一个对尖括号标志*

![avatar](./imag/Snipaste_2020-07-11_00-14-32.PNG)

*3. 打开Remote-SSH: Open Configuration File...,然后配置文件内容,例如*
```
Host root
    HostName 47.97.221.121
    Port 22
    User root
    IdentityFile C:\Users\%user%\.ssh\id_rsa
```

*4. 选择connect host之后就可以操作了*

# linux系统迁移
## tar方法
1. 打包
    ```bash
    # ============打包=======================
    cd /
    tar -cvpzf backup.tar.gz --exclude=/backup.tar.gz --one-file-system /  # 适用于只有一个分区
    
    # 如果打包后的压缩包太大，可以分卷压缩，有两种方法
    tar -cvpz --exclude=/backup.tar.gz --one-file-system / | split -d -b 2048m - backup.tar.gz
    
    # 或者完整压缩完之后再分割
    split -d -b 3900m /path/to/backup.tar.gz /name/of/backup.tar.gz
    
    ```
2. 还原

- 将打包好的文件拷贝到U盘或者其它存储介质，利用linux-live进入系统；
- 进入live系统后，搜索disk工具，将待安装系统的硬盘格式化，并新建一个分区用作安装系统（如果打包的系统有多个分区，那也建立对应分区）；
- 利用fdisk查看硬盘设备, 找到自己的分区，例如/dev/sda1
  
    > fdisk -l  # 查看分区命令
- 挂载分区
  
    > mount /dev/sda1 /mnt   # 将 /dev/sda1 挂载到 /mnt(自己选择其它目录也可以)
- 解压系统
    > sudo tar -xvpzf /path/to/backup.tar.gz -C /mnt --numeric-owner # 单个压缩包采用这种方式

    > cat backup.tar.gz* | tar -xvpz -C /mnt --numeric-owner  # 分卷压缩采用这种方式
- 修改UUID
    ```bash
    # 查看/dev/sda1的 UUID
    blkid 或者 lsblk -f 
    
    # 修改UUID
    sudo vi /mnt/etc/fstab # 将 文件中 /dev/sda1的UUID替换为上面的UUID
    sudo vi /mnt/etc/initramfs-tools/conf.d/resume（这里存储swap分区UUID，如果没有swap分区可以删除）
    ```

- 修复grub
    ```bash
    # 挂载分区
    for f in dev proc sys ; do mount --bind /$f /mnt/$f ; done 
    
    # 设置 /mnt为系统路径
    sudo chroot /mnt # 退出用exit
    
    # 修复grub
    sudo grub-install /dev/sda # 注意这里sda后面不要加数字
    sudo update-grub
    (ps: 可以试试直接grub-install --root-directory=/mnt /dev/sda, 可能就不需要挂载分区再用chroot进入啥的)
    
    # 修复没有错误的话就可以使用exit退出，然后用umount /mnt取消挂载，或者直接重启拔出U盘就可以了
    ```
    **参考**

<a href='https://help.ubuntu.com/community/BackupYourSystem/TAR'>1. Ubuntu Documentation BackupYourSystem/TAR<a><br/>
<a href='https://askubuntu.com/questions/235362/trying-to-reinstall-grub-2-cannot-find-a-device-for-boot-is-dev-mounted'>2. Trying to reinstall GRUB 2, cannot find a device for /boot (is /dev mounted?)</a></br>
<a href='https://jiajunhuang.com/articles/2020_05_22-linux_clone_sys.md.html'>3. Linux系统迁移记录(从HDD到SSD)</a></br>
[4. Ubuntu10.10 “grub rescue no such device”问题解决方案](https://codeleading.com/article/802780019/)
[Ubuntu – How does /etc/initramfs-tools/conf.d/resume work](https://itectec.com/ubuntu/ubuntu-how-does-etc-initramfs-tools-conf-d-resume-work/)

[5. Ubuntu20.04系统迁移（将efi系统迁移到新硬盘）](https://www.jianshu.com/p/8b067b9bab2c)



# 问题总结
## 1. Git clone 速度过慢解决办法

### 使用github的镜像网站进行访问
> github.com.**cnpmjs**.org，我们将原本的网站中的github.com 进行替换。
>
> 例如上例子中替换为https://github.com.cnpmjs.org/graykode/nlp-tutorial

## 2. Debian安装miniconda后出现CondaHTTPError: HTTP 000 CONNECTION FAILED
[原文](https://github.com/conda/conda/issues/9948)
> 解决办法：更换miniconda安装版本为**4.7.12**(*开始使用版本为4.8.3*)

<<<<<<< HEAD
*ps: 安装anaconda后想更换安装路径，需要修改anaconda3/bin/conda中的内容*
## 3. sudo: unable to resolve host xxxxx

> sudo vi /etc/hosts
> 
将**127.0.0.1 localhost** 改为 **127.0.0.1 localhost xxxx**(你的主机名)

*ps:修改主机名 **vi /etc/hostname** 然后 **sudo reboot***

## 4. linux下sudo更改文件权限报错xxxis not in the sudoers file. This incident will be reported
> sudo chmod 600 /etc/sudoers
> 
> sudo vi /etc/sudoers
在 **root ALL=(ALL) ALL** 下添加 **xxx ALL=(ALL) ALL**
```
youuser ALL=(ALL) ALL
%youuser ALL=(ALL) ALL
youuser ALL=(ALL) NOPASSWD: ALL
%youuser ALL=(ALL) NOPASSWD: ALL

第一行:允许用户youuser执行sudo命令(需要输入密码).
第二行:允许用户组youuser里面的用户执行sudo命令(需要输入密码).
第三行:允许用户youuser执行sudo命令,并且在执行的时候不输入密码.
第四行:允许用户组youuser里面的用户执行sudo命令,并且在执行的时候不输入密码.
```

## 5 执行sudo apt-get update报错
**1. 换源**
```
这是因为镜像源除出了问题，一般都会推荐使用国内的镜像源，比如163或者阿里云或者清华大学的镜像服务器 （强烈建议使用清华镜像）

清华镜像源官网：https://mirrors.tuna.tsinghua.edu.cn/help/ubuntu/

将镜像源文本添加到/etc/apt/sources.list文件里
```
**2. 仍然报错，更换DNS**
> sudo vi /etc/resolv.conf

在其中添加：
```
nameserver 127.0.1.1
#这里用的是阿里云的DNS服务器
nameserver 223.5.5.5  
nameserver 223.6.6.6
```

**3. WSL重启后，设置的DNS失效**
> sudo vim /etc/wsl.conf

*添加以下内容*
```sh
[network]
generateResolvConf = false
```

*重新启动wsl*
> wsl -d “your wsl name”

*再修改/etc/resolv.conf*

[参考文章：wsl手動設置dns不被重置為默認](https://www.ucamc.com/e-learning/computer-skills/421-wsl%E6%89%8B%E5%8B%95%E8%A8%AD%E7%BD%AEdns%E4%B8%8D%E8%A2%AB%E9%87%8D%E7%BD%AE%E7%82%BA%E9%BB%98%E8%AA%8D)

## 6. ssh问题总结
### 1. ssh连接出现Permission denied, please try again.
*进入被连主机的/etc/ssh/sshd_config这个文件*
> vi /etc/ssh/sshd_config

*找到 **PermitRootLogin prohibit-password**，改为 **PermitRootLogin yes***

*重启 ssh 服务：*
> /etc/init.d/ssh restart

### 2. ssh连接掉线
修改C:\ProgramData\ssh\sshd_config文件sshd_config
> ClientAliveInterval 30 # 30s给客户端发送一次心跳

> ClientAliveCountMax 3  # 此客户端没有返回心跳，断开连接

**Reference**<br>
[(20200328已解决)ssh经常掉线](https://blog.csdn.net/The_Time_Runner/article/details/105210287)

### 3. windows添加authorized_keys无效
1) 添加authorized_keys到c盘用户下的.ssh;
2) 修改C:\ProgramData\ssh\sshd_config文件，注释最后两行保存；
    ```
    #Match Group administrators
    #       AuthorizedKeysFile __PROGRAMDATA__/ssh/administrators_authorized_keys
    ```
3) 重启sshd服务。

- **linux下出现同样问题**）<br>
```
查看日志/var/log/secure如果显示Authentication refused: bad ownership or modes for directory /home/user/.ssh
    只需chmod -R 700 ~/.ssh
如果显示的是/home/user的权限有问题，修改 /home/usr的权限为700就可以了（不加 -R 参数）
因为用户目录以及 .ssh目录权限只能是用户自己，authorized_keys的权限为600
```
**参考：**
[SSH Authentication Refused: Bad Ownership or Modes for Directory](https://chemicloud.com/kb/article/ssh-authentication-refused-bad-ownership-or-modes-for-directory/)

### 4. 修改windows的ssh默认shell为powershell
    在运行 OpenSSH Server 的 Windows 系统的注册表中添加一个配置项，注册表路径为 HKEY_LOCAL_MACHINE\SOFTWARE\OpenSSH，项的名称为 DefaultShell，项的值为 C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe。

或者以管理员身份启动 PowerShell，然后执行下面的命令完成注册表项的添加：
> New-ItemProperty -Path "HKLM:\SOFTWARE\OpenSSH" -Name DefaultShell -Value "C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe" -PropertyType String -Force

**Reference**<br>
[Windows 支持OpenSSH 了！ - sparkdev](https://www.cnblogs.com/sparkdev/p/10166061.html)

## 7. sudo: unable to resolve host xxxxx
> sudo vi /etc/hosts
> 
将**127.0.0.1 localhost** 改为 **127.0.0.1 localhost xxxx**(你的主机名)

*ps:修改主机名 **vi /etc/hostname** 然后 **sudo reboot***

## 8. linux下sudo更改文件权限报错xxxis not in the sudoers file. This incident will be reported
> sudo chmod 600 /etc/sudoers
> 
> sudo vi /etc/sudoers
在 **root ALL=(ALL) ALL** 下添加 **xxx ALL=(ALL) ALL**
```
youuser ALL=(ALL) ALL
%youuser ALL=(ALL) ALL
youuser ALL=(ALL) NOPASSWD: ALL
%youuser ALL=(ALL) NOPASSWD: ALL

第一行:允许用户youuser执行sudo命令(需要输入密码).
第二行:允许用户组youuser里面的用户执行sudo命令(需要输入密码).
第三行:允许用户youuser执行sudo命令,并且在执行的时候不输入密码.
第四行:允许用户组youuser里面的用户执行sudo命令,并且在执行的时候不输入密码.
```

## 9.增加swap空间大小
```sh
# 查看交换空间大小
free -m

# 创建一个 Swap 文件
sudo fallocate -l 1G /swap/swapfile # 如果不存在fallocate命令采用下面步骤

mkdir /swap
cd /swap
sudo dd if=/dev/zero of=swapfile bs=1024 count=4 # bs为块大小（默认单位为字节），count为块的数量，所以空间大小为 1024 * 2000000


# 激活swap文件
sudo mkswap -f swapfile # 生成文件转为Swap文件
sudo chmod 0600 ./swapfile  
sudo swapon ./swapfile

# 卸载swap文件
sudo swapoff ./swapfile

# 查看交换分区文件
swapon -s

如果需要一直保持这个 swap ，可以把它写入 /etc/fstab 文件。
/swap/swapfile swap swap defaults 0 0
```

参考：[How to Create Swap File on Linux](https://help.ubuntu.com/community/SwapFaq)


调整Swappiness值
```sh
# Swappiness是Linux内核属性，它定义系统多久使用一次swap交换空间。 它的值可以在0到100之间。较低的值将使内核尽可能避免交换，而较高的值将使内核更积极地使用交换空间。

cat /proc/sys/vm/swappiness # 查看swappiness值

sudo sysctl vm.swappiness=10 # 修改

# 让swapiness启动后保持不变
# 在/etc/sysctl.conf添加vm.swappiness=10
```
参考：[如何在Ubuntu 20.04上添加swap交换空间](https://www.myfreax.com/how-to-add-swap-space-on-ubuntu-20-04/)