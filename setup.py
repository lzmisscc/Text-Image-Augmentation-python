# coding:utf-8

from setuptools import setup, find_packages
# or
# from distutils.core import setup

setup(
        name='ocraug',     # 包名字
        version='1.0',   # 包版本
        description='This is a test of the setup',   # 简单描述
        author='huoty',  # 作者
        author_email='sudohuoty@163.com',  # 作者邮箱
        url='https://www.konghy.com',      # 包的主页
        packages=find_packages(where='ocraug', exclude=(), include=('*',))
)