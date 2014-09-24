软路由锐捷认证辅助脚本
================

本脚本功能是在锐捷掉线后能自动恢复网络认证
把官方下载的锐捷放进本目录下
地址 http://nc.hust.edu.cn/download/soft/Linux%20SU%20V1.01%E7%89%88.tar.gz

├── cron
├── README
├── README.md
├── rjdaemon-sample.sh
├── rjsupplicant.sh
├── x64
└── x86

复制 rjdaemon-sample.sh 为 rjdaemon.sh
修改其中的账号密码，然后把cron添加到crontab中。
日志存放在 /tmp/rj.log 中

