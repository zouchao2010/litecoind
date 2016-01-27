#!/usr/bin/env bash

#copy livenet conf
if [ ! -d /var/lib/litecoind/livenet ]; then
    cp -r /opt/litecoind/livenet /var/lib/litecoind/
fi

#copy testnet conf
if [ ! -d /var/lib/litecoind/testnet ]; then
    cp -r /opt/litecoind/testnet /var/lib/litecoind/
fi

#copy notify script
if [ ! -f /var/lib/litecoind/block_notify.py ]; then
    cp /opt/litecoind/block_notify.py /var/lib/litecoind/
    chmod 755 /var/lib/litecoind/block_notify.py
fi

#run litecoind
if [ $TESTNET -eq 0 ];
then
    litecoind -datadir=/var/lib/litecoind/livenet
else
    litecoind -datadir=/var/lib/litecoind/testnet
fi

bash
