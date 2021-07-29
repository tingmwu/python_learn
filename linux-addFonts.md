## linux 下设置 安装字体
### 设置默认字体
```
sudo apt install locale // 安装语言管理软件
sudo dpkg-reconfigure locales // 设置语言

```
进入设置界面后，空格键为选择/取消，Tab键为切换到确认选择
选择en_us.UTF-8，以及所有的zh_CN选项，回车保存退出

```
sudo vim /etc/default/locale
```

### 安装字体

```sh
# 字体目录
/usr/share/fonts
/usr/local/share/fonts # 推荐该目录，初始没有字体，方便管理
~/.fonts # 一般需要用户自建，仅适用于当前用于

# 安装之后，更新字体缓存
sudo fc-cache [你添加字体的目录]

# 查看字体
fc-list
```
