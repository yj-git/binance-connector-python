from binance.lib.utils import get_uuid, purge_map, websocket_api_ed25519_signature


# 身份验证请求
def logon(self, **kwargs):
    parameters = purge_map(kwargs)

    payload = {
        "id": parameters.pop("id", get_uuid()),
        "method": "session.logon",
        "params": websocket_api_ed25519_signature(api_key=self.api_key, private_key=self.private_key, private_key_pass=self.private_key_pass, parameters=parameters),
    }

    self.send(payload)


# 查询会话状态
def status(self, **kwargs):
    parameters = purge_map(kwargs)

    payload = {
        "id": parameters.pop("id", get_uuid()),
        "method": "session.status"
    }

    self.send(payload)


# 退出会话
def logout(self, **kwargs):
    parameters = purge_map(kwargs)

    payload = {
        "id": parameters.pop("id", get_uuid()),
        "method": "session.logout"
    }

    self.send(payload)
