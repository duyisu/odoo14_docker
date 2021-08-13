# Odoo14 docker 容器
## odoo
>docker-compose.yml同级目录床架 addons,config,web文件夹
>用来存放自定义app，odoo配置文件
>
[点击跳转官网](https://www.wingnew.com)
![title](https://www.leppysoft.com/web/image/website/1/logo/%E6%B1%9F%E8%A5%BF%E4%BA%91%E7%89%9B%E7%A7%91%E6%8A%80?unique=ef3e9b8)
## nginx
* 端口80反向代理8069
其他配置放到nginx/conf.d目录下即可

## postgresql
* 当前目录创建data文件夹，存放数据文件

## 使用
docker-compose up --detach

