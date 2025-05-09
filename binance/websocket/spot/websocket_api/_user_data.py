from binance.lib.utils import get_uuid


# 订阅用户数据流 create by cyj
def subscribe_user_data(self, id=None):
    """Start user data stream (USER_STREAM)

    Args:
        id (str): A unique id for the request

    Message sent:

    .. code-block:: json

        {
            "id": "d3df8a21-98ea-4fe0-8f4e-0fcea5d418b7",
            "method": "userDataStream.subscribe",
            "params": {
                "apiKey": "vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A"
            }
        }

    Response:

    .. code-block:: json
        账户更新
        {
          "e": "outboundAccountPosition", // 事件类型
          "E": 1564034571105,             // 事件时间
          "u": 1564034571073,             // 账户末次更新时间戳
          "B": [                          // 余额
            {
              "a": "ETH",                 // 资产名称
              "f": "10000.000000",        // 可用余额
              "l": "0.000000"             // 冻结余额
            }
          ]
        }

        余额更新
        {
          "e": "balanceUpdate",         // Event Type
          "E": 1573200697110,           // Event Time
          "a": "ABC",                   // Asset
          "d": "100.00000000",          // Balance Delta
          "T": 1573200697068            // Clear Time
        }

        订单更新
        {
          "e": "executionReport",        // 事件类型
          "E": 1499405658658,            // 事件时间
          "s": "ETHBTC",                 // 交易对
          "c": "mUvoqJxFIILMdfAW5iGSOW", // clientOrderId
          "S": "BUY",                    // 订单方向
          "o": "LIMIT",                  // 订单类型
          "f": "GTC",                    // 有效方式
          "q": "1.00000000",             // 订单原始数量
          "p": "0.10264410",             // 订单原始价格
          "P": "0.00000000",             // 止盈止损单触发价格
          "F": "0.00000000",             // 冰山订单数量
          "g": -1,                       // OCO订单 OrderListId
          "C": "",                       // 原始订单自定义ID（原始订单，指撤单操作的对象。撤单本身被视为另一个订单）
          "x": "NEW",                    // 本次事件的具体执行类型
          "X": "NEW",                    // 订单的当前状态
          "r": "NONE",                   // 订单被拒绝的原因；请参阅订单被拒绝的原因（下文）了解更多信息
          "i": 4293153,                  // orderId
          "l": "0.00000000",             // 订单末次成交量
          "z": "0.00000000",             // 订单累计已成交量
          "L": "0.00000000",             // 订单末次成交价格
          "n": "0",                      // 手续费数量
          "N": null,                     // 手续费资产类别
          "T": 1499405658657,            // 成交时间
          "I": 8641984,                  // Execution ID
          "w": true,                     // 订单是否在订单簿上？
          "m": false,                    // 该成交是作为挂单成交吗？
          "M": false,                    // 请忽略
          "O": 1499405658657,            // 订单创建时间
          "Z": "0.00000000",             // 订单累计已成交金额
          "Y": "0.00000000",             // 订单末次成交金额
          "Q": "0.00000000",             // Quote Order Quantity
          "D": 1668680518494,            // 追踪时间; 这仅在追踪止损订单已被激活时可见
          "W": 1499405658657,            // Working Time; 订单被添加到 order book 的时间
          "V": "NONE"                    // SelfTradePreventionMode
        }

        Listen Key 已过期
        {
          "e": "listenKeyExpired",  // 事件类型
          "E": 1699596037418,      // 事件时间
          "listenKey": "OfYGbUzi3PraNagEkdKuFwUHn48brFsItTdsuiIXrucEvD0rhRXZ7I6URWfE8YE8"
        }
    """

    if not id:
        id = get_uuid()

    payload = {
        "id": id,
        "method": "userDataStream.subscribe"
    }

    self.send(payload)


# 取消订阅用户数据流 create by cyj
def unsubscribe_user_data(self, id=None):
    """Stop user data stream

    Args:
        id (str): A unique id for the request

    Message sent:

    .. code-block:: json

        {
            "id": "d3df8a21-98ea-4fe0-8f4e-0fcea5d418b7",
            "method": "userDataStream.unsubscribe"
        }

    """

    if not id:
        id = get_uuid()

    payload = {
        "id": id,
        "method": "userDataStream.unsubscribe"
    }

    self.send(payload)


def user_data_start(self, id=None):
    """Start user data stream (USER_STREAM)

    Args:
        id (str): A unique id for the request

    Message sent:

    .. code-block:: json

        {
            "id": "d3df8a61-98ea-4fe0-8f4e-0fcea5d418b0",
            "method": "userDataStream.start",
            "params": {
                "apiKey": "vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A"
            }
        }

    Response:

    .. code-block:: json

        {
            "id": "d3df8a61-98ea-4fe0-8f4e-0fcea5d418b0",
            "status": 200,
            "result": {
                "listenKey": "xs0mRXdAKlIPDRFrlPcw0qI41Eh3ixNntmymGyhrhgqo7L6FuLaWArTD7RLP"
            },
            "rateLimits": [
                {
                "rateLimitType": "REQUEST_WEIGHT",
                "interval": "MINUTE",
                "intervalNum": 1,
                "limit": 1200,
                "count": 1
                }
            ]
        }


    """

    if not id:
        id = get_uuid()

    payload = {
        "id": id,
        "method": "userDataStream.start",
        "params": {"apiKey": self.api_key},
    }

    self.send(payload)


def user_data_ping(self, listenKey: str, id=None):
    """Keepalive a user data stream to prevent a time out.

    Args:
        listenKey (str): The listen key from the user data stream
        id (str): A unique id for the request

    Message sent:

    .. code-block:: json

        {
            "id": "815d5fce-0880-4287-a567-80badf004c74",
            "method": "userDataStream.ping",
            "params": {
                "listenKey": "xs0mRXdAKlIPDRFrlPcw0qI41Eh3ixNntmymGyhrhgqo7L6FuLaWArTD7RLP",
                "apiKey": "vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A"
            }
        }


    Response:

    .. code-block:: json

        {
            "id": "815d5fce-0880-4287-a567-80badf004c74",
            "status": 200,
            "response": {},
            "rateLimits": [
                {
                "rateLimitType": "REQUEST_WEIGHT",
                "interval": "MINUTE",
                "intervalNum": 1,
                "limit": 1200,
                "count": 1
                }
            ]
        }


    """

    if not id:
        id = get_uuid()

    payload = {
        "id": id,
        "method": "userDataStream.ping",
        "params": {"apiKey": self.api_key, "listenKey": listenKey},
    }

    self.send(payload)


def user_data_stop(self, listenKey: str, id=None):
    """Stop user data stream

    Args:
        listenKey (str): The listen key from the user data stream
        id (str): A unique id for the request

    Message sent:

    .. code-block:: json

        {
            "id": "819e1b1b-8c06-485b-a13e-131326c69599",
            "method": "userDataStream.stop",
            "params": {
                "listenKey": "xs0mRXdAKlIPDRFrlPcw0qI41Eh3ixNntmymGyhrhgqo7L6FuLaWArTD7RLP",
                "apiKey": "vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A"
            }
        }

    Response:

    .. code-block:: json

        {
            "id": "819e1b1b-8c06-485b-a13e-131326c69599",
            "status": 200,
            "response": {},
            "rateLimits": [
                {
                "rateLimitType": "REQUEST_WEIGHT",
                "interval": "MINUTE",
                "intervalNum": 1,
                "limit": 1200,
                "count": 1
                }
            ]
        }

    """

    if not id:
        id = get_uuid()

    payload = {
        "id": id,
        "method": "userDataStream.stop",
        "params": {"apiKey": self.api_key, "listenKey": listenKey},
    }

    self.send(payload)
