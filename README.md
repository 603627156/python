* python 综合学习之路
https://github.com/603627156

更新：
      git pull
提交：
      git add .
      git commit -m "first commit:bo.tang:"
      git push	


2.命令行添加代码

第一次使用
git clone git@github.com:51reboot/actual-14-homework.git
cd actual-14-homework
mkdir woniu
echo  print 123 >> woniu/zuoye.py
git add .
git commit -m "first commit:joy:"

git push -u origin master

后面添加代码，只需要下面三行即可
git add .
git commit -m "first commit"
git push -u origin master
用命令行操作，要添加ssh的公钥到github里，操作方法

创建SSH key的方法很简单，执行如下命令就可以：
ssh-keygen
生成的SSH key文件保存在中～/.ssh/id_rsa.pub

然后用文本编辑工具打开该文件，我用的是vim,所以命令是：
vim ~/.ssh/id_rsa.pub

接着拷贝.ssh/id_rsa.pub文件内的所以内容，将它粘帖到github帐号管理中的添加SSH key界面中。
打开github帐号管理中的添加SSH key界面的步骤如下：
1. 登录github
2. 点击右上方的Accounting settings图标
3. 选择 SSH key
4. 点击 Add SSH key
在出现的界面中填写SSH key的名称，填一个你自己喜欢的名称即可，然后将上面拷贝的~/.ssh/id_rsa.pub文件内容粘帖到key一栏，在点击“add key”按钮就可以了。
添加过程github会提示你输入一次你的github密码

添加完成后再次执行git clone就可以成功克隆github上的代码库了。
