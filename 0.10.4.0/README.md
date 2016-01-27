# litecoind

## build
```shell
docker build -t zouchao2010/litecoind:0.10.4.0 .

```

## pull
```shell
docker pull zouchao2010/litecoind:0.10.4.0

```
  
## run(创建并运行一个容器，退出时删除容器)
```shell
docker run  --name litecoind-0.10.4.0 \
            -h litecoind-0112 \
            -p 19332:19332 \
            -p 19333:19333 \
            -v /data/litecoind-0.10.4.0:/var/lib/litecoind \
            -e TESTNET=1 \
            -it --rm zouchao2010/litecoind:0.10.4.0
            
```
  
## run(创建并运行一个容器，以守护进程方式)
```shell
docker run  --name litecoind-0.10.4.0 \
            --restart=always \
            -m 2048m \
            -h litecoind-0112 \
            -p 19332:19332 \
            -p 19333:19333 \
            -v /data/litecoind-0.10.4.0:/var/lib/litecoind \
            -e TESTNET=1 \
            -dt zouchao2010/litecoind:0.10.4.0
            
```

## start|stop|restart(已存在的容器)
```shell
docker start|stop|restart litecoind-0.10.4.0

```

## exec(使用已运行的容器执行命令)
```shell
docker exec -it litecoind-0.10.4.0 /bin/bash

```


## dependency
```shell
docker run  --name redis \
            -h redis \
            -p 6379:6379 \
            -v /data/redis:/data \
            -dt redis
            
```
