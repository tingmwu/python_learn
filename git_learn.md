# git 使用

*学习git的基本使用*

## 1. 创建仓库

### 方式 1 git init

*任意建立一个文件夹，右键git bash, 输入git init将会在创建当前文件夹为一个本地git仓库*

> $ mkdir test  
> $ cd test   
> $ git init  


### 方式 2 git clone 


*直接将git仓库中的在线仓库克隆到本地*

> $ git clone xxxxx  

*xxxxx是你在仓库复制的链接，如下图所示*

![avatar](./imag/git_clone.PNG)


## 2. 本地库基本操作
### git add

> $ git add+文件名.文件类型

*例如，我在文件夹里添加了一个test.txt，
也就是说我修改了test.txt，所以我在Git
Bash中可以写git add test.txt 来添加我的修改记录。但是你发现上一条git
add test.txt失败了，因为我在本地仓库中从没对这个进行我操作，所以没有修改记录，因此无法添加修改记录。*

> git add -A    # 提交所有变换    
> git add -u    # 提交被修改和被删除的文件  
> git add .     # 提交新文件和被修改的文件(**不包括被删除的文件**)

### git diff
**查看文档变换**
> git diff &emsp;# 查看所有文档变化<br>
> git diff 文件名.文件类型   &emsp; # 查看某个文件的变化<br>   

### cat 文件名.文件类型
    查看该文件内容

### git reset --soft HEAD^(或者版本号)
```
首先使用 git log 查看版本号 
如果输出太多 可以使用 git log --pretty=oneline

HEAD^的意思是上一个版本，也可以写成HEAD~1
如果你进行了2次commit，想都撤回，可以使用HEAD~2

--mixed 
意思是：不删除工作空间改动代码，撤销commit，并且撤销git add . 操作
这个为默认参数,git reset --mixed HEAD^ 和 git reset HEAD^ 效果是一样的。
 
--soft  
不删除工作空间改动代码，撤销commit，不撤销git add . 
 
--hard
删除工作空间改动代码，撤销commit，撤销git add . 

注意完成这个操作后，就恢复到了上一次的commit状态。

顺便说一下，如果commit注释写错了，只是想改一下注释，只需要：
git commit --amend

此时会进入默认vim编辑器，修改注释完毕后保存就好了
```

**回退后要返回最新版本**
> git reset --hard 最新版本的版本号

*如何已经关闭了命令行窗口，无法查看之前git log的版本号*
> git reflog # 查看之前的提交和回退记录

## 3. 链接远程仓库 
[详细说明点这里](https://www.runoob.com/git/git-remote-repo.html)
由于你的本地 Git 仓库和 GitHub 仓库之间的传输是通过SSH加密的，所以我们需要配置验证信息：
使用以下命令生成 SSH Key：
> ssh-keygen -t rsa -C "youremail@example.com"

后面的 your_email@youremail.com 改为你在 Github 上注册的邮箱，之后会要求确认路径和输入密码，我们这使用默认的一路回车就行。成功的话会在 ~/ 下生成 .ssh 文件夹，进去，打开 id_rsa.pub，复制里面的 key。

回到 github 上，进入 Account => Settings（账户配置）=> SSH and GPG keys => NEW SSH key。

![avatar](./imag/ssh.PNG)


- 方式1 https地址
> 优点：可以直接复制图中的地址进行连接  
> 缺点： 每次连接都需要登录自己的github账号
- 方式2 ssh地址
> 优点：只需登录一次  
> 缺点： 须在本地和git仓库进行配置

**具体步骤**

1. 链接远程仓库 
> git remote add [shortname] [url]  
eg: 
> git remote add origin git@github.com:tingmwu/python_learn.git       

2. 查看远程库
> git remote -v

3. 提交修改并上传
> git add -A    # 增加修改  
> git commit -m '你的备注信息' # 提交修改
 
4. 进行同步

> git push -u origin master

    *由于远程库是空的，我们第一次推送master分支时，加上了 –u参数，Git不但会把本地的master分支内容推送的远程新的master分支，还会把本地的master分支和远程的master分支关联起来，在以后的推送或者拉取时就可以简化命令，只输入（如下）就OK。*

> git push origin master

     

<!-- <meta http-equiv="refresh" content="5"> -->

## 4. git同时推送多个远程仓库
### 方法1
> git remote set-url --add origin https://github.com/demo.git(新增的远程库链接)

### 方法2
**修改.git/config**
```bash
[remote "origin"]
	url = git@gitee.com:tingmwu/gray-segment.git
    url = 新的远程库链接
	fetch = +refs/heads/*:refs/remotes/origin/*
```