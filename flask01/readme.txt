安装虚拟环境
不同项目所依赖的Python版本、module可能不一样，且存在兼容问题，因此为了互不干扰，可以为项目创建虚拟环境
第一步：安装virtualenvwrapper
pip3 install virtualenvwrapper

安装之后，配置virtualenvwrapper环境变量才能在命令行中使用对应命令
vim ~/.zshrc
在.zshrc中添加下面3行
//指定虚拟环境创建的目录
export WORKON_HOME=$HOME/myenv
//指定Python3路径
export VIRTUALENVWRAPPER_PYTHON=/usr/local/bin/python3
// 运行virtualenvwrapper
source /usr/local/bin/virtualenvwrapper.sh

关闭文件，source ~/.zshrc

常用命令：
创建虚拟环境 ： mkvirtualenv env1
查看存在的虚拟环境： lsvirtualenv -b
切换虚拟环境：workon env1
进入到当前虚拟环境目录：cdvirtualenv
查看环境装了哪些包：lssitepackages
复制环境：cpvirtualenv env1 env2
删除环境：rmvirtualenv env1
退出虚拟环境：deactivate