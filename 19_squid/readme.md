## 使用
    
    $ docker run -d --name squid-container -e TZ=UTC -p 3128:3128 registry.cn-beijing.aliyuncs.com/livenowhy/squid:latest
    
    -e TZ=UTC       时区
    -p 3128:3128    暴露端口
    -v /path/to/logs:/var/log/squid	     日志
    -v /path/to/data:/var/spool/squid    缓存(运行数据)
    -v /path/to/main/config:/etc/squid/squid.conf    主配置文件
    -v /path/to/config/snippet:/etc/squid/conf.d/snippet.conf	Configuration snippets included by squid.conf