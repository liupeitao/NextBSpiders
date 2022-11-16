# -*- coding: utf-8 -*-
# @Time     : 2022/11/16 17:12:14
# @Author   : ddvv
# @Site     : https://ddvvmmzz.github.io
# @File     : setup.py
# @Software : Visual Studio Code
# @WeChat   : NextB


import setuptools


def do_setup(**kwargs):
    try:
        setuptools.setup(**kwargs)
    except (SystemExit, Exception) as e:
        exit(1)


long_description = """

基于scrapy框架的爬虫项目

## 准备

在使用Telegram的爬虫之前，需要获取自己telegram的`api_id`和`api_hash`：

1. 使用开发者的帐户（如电话号码）登录到Telegram帐户，登录地址：(https://my.telegram.org/auth)[https://my.telegram.org/auth]
2. 单击API开发工具
3. 在出现创建新应用程序窗口中，填写申请详情。不用输入任何URL，只用修改两个字段（`App title`和`Short name`）
4. 最后单击创建应用程序，生成`api_id`和`api_hash`。申请的`api_id`和`api_hash`是永久的，自己注意保密。

## 安装

```
pip install NextBSpiders
```

## 爬虫配置文件格式

```json
{
    "api_id": "",                           // telgram的api_id，申请方式见《准备》
    "api_hash": "",                         // telgram的api_hash，申请方式见《准备》
    "session_name": "c:/xxxx/xxxx.session", // 保存telegram的登录session
    "sqlite_db_name": "C:/xxxx/xxxx.db",    // 保存telegram的sqlite数据库地址
    "proxy": {                              // 代理信息，目前测试了clash代理
        "protocal": "socks5",               // 代理协议，目前仅测试了socks5协议
        "ip": "127.0.0.1",                  // 代理地址
        "port": 7890                        // 代理端口
    },
    "group": {                              // 爬取的群组信息
        "group_id": 1575910766,             // 群组ID
        "limit": 10,                        // 单次爬取条数，建议不超过3000
        "last_message_id": -1,              // 起始消息ID，-1表示从最早一条开始爬取
        "offset_date": ""                   // 起始时间，留空表示从最早一条开始爬取，格式形如："2020-01-01 00:00:00"
    }
}
```
## 支持的爬虫列表

|爬虫名称|备注|
|----|----|
|telegramScanMessages|telegram的消息爬虫|

## 命令行工具

|命令|功能|备注|
|----|----|----|
|nextb-telegram-run-spider|执行telegram爬虫|如`nextb-telegram-run-spider.exe -c .\my.json`|
|nextb-telegram-create-table|创建telegram数据表|如`nextb-telegram-create-table.exe -c .\my.json`|
|nextb-telegram-clear-dialog|清理telegram对话框|如`nextb-telegram-clear-dialog.exe -c .\my.json`|
|nextb-telegram-get-dialog|获取telegram对话框|如`nextb-telegram-get-dialog.exe -c .\my.json`|
|nextb-telegram-get-message|获取telegramq群组聊天消息|如`nextb-telegram-get-message.exe -c .\my.json`|

## 使用方式

1. 按需求配置好`config.json`文件，此时必填项包括：`api_id`、`api_hash`、`session_name`、`sqlite_db_name`，`proxy`代理选项根据实际网络情况填写，**如果不需要代理，则`proxy`填空字典：`"proxy": {}`**
2. 初始化sqlite存储数据库：`nextb-telegram-create-table -c $config.json`
3. 利用获取对话框功能，初始化telegram的登陆状态：`nextb-telegram-get-dialog -c $config.json`
4. 在终端中数据`登录账户（如手机号，带国家号）`，在telegram的app中获取登录验证码，输入到终端，完成登录，初始化登录状态数据库
5. 从获取的群组中选择`group_id`，填充到配置文件中
6. 测试消息爬取，初始化登录状态数据库中的数据：`nextb-telegram-get-message -c $config.json`
7. 使用`scrapy`爬虫开始爬取指定群组消息并存入数据库：`nextb-telegram-run-spider.exe -c $config.json`

## 注意事项

1. 每个telegram爬虫配置文件中的`session_name`和`sqlite_db_name`需要独立使用，避免出现`sqlite`数据库读写暂用问题
"""

do_setup(
    name="NextBSpiders",
    version="1.0.0",
    author="ddvv",
    author_email="dadavivi512@gmail.com",
    description="基于scrapy的telegram爬虫",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/a232319779/NextBSpiders",
    packages=setuptools.find_packages(exclude=["tests"]),
    entry_points={
        "console_scripts": [
            "nextb-telegram-run-spider = NextBSpiders.cli.telegram_run_spider:run",
            "nextb-telegram-create-table = NextBSpiders.cli.telegram_create_table:run",
            "nextb-telegram-clear-dialog = NextBSpiders.cli.telegram_clear_dialog:run",
            "nextb-telegram-get-dialog = NextBSpiders.cli.telegram_get_dialog:run",
            "nextb-telegram-get-message = NextBSpiders.cli.telegram_get_message:run",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    keywords=[],
    license="MIT",
    include_package_data=True,
    install_requires=[
        "Scrapy==2.6.1",
        "setuptools==58.0.4",
        "SQLAlchemy==1.4.31",
        "Telethon==1.24.0",
        "Twisted==22.4.0",
        "pysocks==1.7.1",
    ],
)
