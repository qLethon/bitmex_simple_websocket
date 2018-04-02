import websocket
import json
import time, urllib, hmac, hashlib

class BitMEXWebSocket:

    def __init__(self, endpoint, api_key=None, api_secret=None):

        self.endpoint = endpoint

        if api_key is not None and api_secret is None:
            raise ValueError('api_secret is required if api_key is provided')
        if api_key is None and api_secret is not None:
            raise ValueError('api_key is required if api_secret is provided')

        self.api_key = api_key
        self.api_secret = api_secret

        websocket.enableTrace(True)
        ws = websocket.WebSocketApp(self.endpoint,
                                on_message = self.on_message,
                                on_error = self.on_error,
                                on_close = self.on_close,
                                header = self._get_auth())
        ws.on_open = self.on_open
        ws.run_forever()

    def on_message(self, ws, message):
        data = json.loads(message)
        print(data)
        print()

    def on_error(self, ws, error):
        print(error)

    def on_close(self, ws):
        print('close')

    def on_open(self, ws):
        print('open')

    def _get_auth(self):
        if self.api_key:
            nonce = self._generate_nonce()
            return [
                "api-nonce: " + str(nonce),
                "api-signature: " + self._generate_signature(self.api_secret, 'GET', '/realtime', nonce, ''),
                "api-key:" + self.api_key
            ]
        else:
            return []
    
    def _generate_nonce(self):
        return int(round(time.time() * 1000))

    def _generate_signature(self, secret, verb, url, nonce, data):
        """Generate a request signature compatible with BitMEX."""
        # Parse the url so we can remove the base and extract just the path.
        parsedURL = urllib.parse.urlparse(url)
        path = parsedURL.path
        if parsedURL.query:
            path = path + '?' + parsedURL.query

        # print "Computing HMAC: %s" % verb + path + str(nonce) + data
        message = (verb + path + str(nonce) + data).encode('utf-8')

        signature = hmac.new(secret.encode('utf-8'), message, digestmod=hashlib.sha256).hexdigest()
        return signature