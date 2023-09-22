import websocket        # pip install websocket-client
import json
import pandas as pd     # pip install pandas

#Set up an endpoint at https://github.com/binance-us/binance-us-api-docs/blob/master/web-socket-streams.md
endpoint = "wss://stream.binance.com:9443/ws"
# Transforming a python dictionary to a json object and then providing some paramters for that parameter
# Send a message to the binance server
our_msg = json.dumps({'method':'SUBSCRIBE',
                    'params':['btcusdt@ticker'],
                    'id':1 })

sub_msg = json.dumps({
  "method": "LIST_SUBSCRIPTIONS",
  "id": 3
})

#print(our_msg)

# Websocket infrastructure, websocket library documentation
def on_open(ws):
    ws.send(sub_msg)

# Whats happening when receive message from the server
# The message in json format translated to python dictionary
def on_message(ws,message):
    out = json.loads(message)
    print(out)

ws = websocket.WebSocketApp(endpoint, on_message=on_message,
                                on_open=on_open)

ws.run_forever()

