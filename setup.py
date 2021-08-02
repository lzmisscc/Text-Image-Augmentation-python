# coding:utf-8

from setuptools import setup, find_packages
# or
# from distutils.core import setup

setup(
        name='ocraug',     # 包名字
        version='1.0',   # 包版本
        description='ocr aug',   # 简单描述
        author='liuzhuang',  # 作者
        author_email='18437961053@163.com',  # 作者邮箱
        packages=find_packages(where='ocraug'),                 # 包
)