#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import logging.handlers
import requests
import base64
import json
import argparse
import time
import os

parser = argparse.ArgumentParser(description='Send notification to Stratum instance about new litecoin block.')
parser.add_argument('--blockhash', dest='blockhash', type=str)
parser.add_argument('--netcode', dest='netcode', type=str)

parser.add_argument('--litecoin_rpc_host', dest='litecoin_rpc_host', type=str)
parser.add_argument('--litecoin_rpc_port', dest='litecoin_rpc_port', type=int)
parser.add_argument('--litecoin_rpc_user', dest='litecoin_rpc_user', type=str)
parser.add_argument('--litecoin_rpc_password', dest='litecoin_rpc_password', type=str)

parser.add_argument('--redis_host', dest='redis_host', type=str)
parser.add_argument('--redis_port', dest='redis_port', type=int)

args = parser.parse_args()

logdir = '/var/lib/litecoind/{}/logs'.format('livenet' if args.netcode.upper() == 'LTC' else 'testnet')
if not os.path.exists(logdir):
    os.makedirs(logdir)
logfile = logdir + "/block_notify.log"
handler = logging.handlers.RotatingFileHandler(
            filename=logfile,
            maxBytes=1024 * 1024,
            backupCount=5)
fmt = '%(asctime)s - %(filename)s:%(lineno)s - %(name)s - %(message)s'

formatter = logging.Formatter(fmt)
handler.setFormatter(formatter)
logger = logging.getLogger('BlockNotify')
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

import redis


def get_block(host, port, user, password, blockhash):
    data = json.dumps({'jsonrpc': '2.0', 'method': 'getblock', 'params': [blockhash, False], 'id': '1'})
    headers = {'Content-Type': 'text/json', 'Authorization': 'Basic %s' % base64.b64encode('%s:%s' % (user, password))}
    r = requests.post('http://%s:%d' % (host, port), data=data, headers=headers)
    return json.loads(r.text)['result']

try:
    start = time.time()
    r = redis.StrictRedis(args.redis_host, args.redis_port)
    rawblock = get_block(args.litecoin_rpc_host, args.litecoin_rpc_port, args.litecoin_rpc_user, args.litecoin_rpc_password, args.blockhash)

    r.publish('%s.wallet_blocknotify' % args.netcode, json.dumps({
        'blockhash':        args.blockhash,
        'rawblock':         rawblock
    }))
    logger.info("[%s] Notify done hash %s in %.03f sec" % (args.netcode, args.blockhash, time.time() - start))

except Exception, ex:
    logger.error("[%s] Notify failed, reason: %s hash %s" % (args.netcode, str(ex), args.blockhash))
