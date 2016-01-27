# litecoind

## build
```shell
docker build -t zouchao2010/litecoind .

```

## pull
```shell
docker pull zouchao2010/litecoind

```
  
## run(创建并运行一个容器，退出时删除容器)
```shell
docker run  --name litecoind \
            -h litecoind \
            -p 19332:19332 \
            -p 19333:19333 \
            -v /data/litecoind:/var/lib/litecoind \
            -e TESTNET=1 \
            -it --rm zouchao2010/litecoind
            
```
  
## run(创建并运行一个容器，以守护进程方式)
```shell
docker run  --name litecoind \
            --restart=always \
            -m 2048m \
            -h litecoind \
            -p 19332:19332 \
            -p 19333:19333 \
            -v /data/litecoind:/var/lib/litecoind \
            -e TESTNET=1 \
            -dt zouchao2010/litecoind
            
```

## start|stop|restart(已存在的容器)
```shell
docker start|stop|restart litecoind

```

## exec(使用已运行的容器执行命令)
```shell
docker exec -it litecoind /bin/bash

```


## dependency
```shell
docker run  --name redis \
            -h redis \
            -p 6379:6379 \
            -v /data/redis:/data \
            -dt redis
            
```
