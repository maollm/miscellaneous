# encoding: utf-8
"""
config mirrors for pip(windows）
create pip.ini for pip as follow:
    [global]
    index-url=http://mirrors.aliyun.com/pypi/simple/
    [install]
    trusted-host=mirrors.aliyun.com
pip.ini should be create at HOMEPATH of windows

author: maollm
mail: maollm@126.com
"""
import os
from shutil import copy
from configparser import ConfigParser

def generate_ini_for_pip(filename):
    conf = ConfigParser()
    conf.add_section('global')
    conf.set('global', 'index-url', 'http://mirrors.aliyun.com/pypi/simple/')
    conf.add_section('install')
    conf.set('install', 'trusted-host', 'mirrors.aliyun.com ')

    # write to file
    with open(filename, "w") as f:
        conf.write(f)

    print(u'创建pip.ini文件：{0}'.format(filename))

if __name__ == '__main__':
    print(u'设置pip国内镜像。')
    print(u'创建pip.ini文件')
    print(u'\t[global]')
    print(u'\tindex-url=http://mirrors.aliyun.com/pypi/simple/')
    print(u'\t[install]')
    print(u'\ttrusted-host=mirrors.aliyun.com')
    print()

    os.chdir('c:/')
    home_path = os.path.abspath(os.environ.get('HOMEPATH'))
    if not home_path:
        print(u'环境变量HOMEPATH不存在，设置pip镜像失败！')
        exit()

    # print(home_path)
    # os.chdir(home_path)

    pip_conf_path = os.path.join(home_path, 'pip')
    if not os.path.exists(pip_conf_path):
        os.mkdir(pip_conf_path)

    pip_conf_file = os.path.join(pip_conf_path, 'pip.ini')
    if not os.path.exists(pip_conf_file):
        generate_ini_for_pip(pip_conf_file)
    else:
        backup_file = pip_conf_file + '.bak'
        copy(pip_conf_file, backup_file)
        print(u'文件已经存在：{0}，\n备份该文件：{1}'.format(pip_conf_file, backup_file))
        # 创建pip.ini
        generate_ini_for_pip(pip_conf_file)
