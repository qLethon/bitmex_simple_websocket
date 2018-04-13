# bitmex_simple_websocket

This is simple library for receiving realtime data from the [BitMEX WebSocket API](https://www.bitmex.com/app/wsAPI).

## Requirements

websocket-client

## Installation

```pip install bitmex-simple-websocket```

## Usage

If client received data then on_message function is called.
You can override on_message function to do what you want when received data.

To subscribe to unauthenticated data:
```
from bitmex_simple_websocket import BitMEXWebSocket
import json

class MyBitMEXWebsocket(BitMEXWebSocket):
    def on_message(self, ws, message):
        data = json.loads(message)
        if 'table' in data and data['table'] == 'tradeBin1m':
            print(data['data'][0])

bitmex = MyBitMEXWebsocket(endpoint='wss://www.bitmex.com/realtime?subscribe=tradeBin1m:XBTUSD')
```

To subscribe to authenticated data:
```
from bitmex_simple_websocket import BitMEXWebSocket
import json

class MyBitMEXWebsocket(BitMEXWebSocket):
    def on_message(self, ws, message):
        data = json.loads(message)
        if 'table' in data and data['table'] == 'order':
            print(data['data'][0])

bitmex = MyBitMEXWebsocket(endpoint='wss://www.bitmex.com/realtime?subscribe=order:XBTUSD',
api_key=YOUR_API_KEY,
api_secret=YOUR_API_SECRET)
```

## Donate

BTC(Segwit): bc1q57792ln850wc2538udg0fr6vdq5f2ajyf2tnyx