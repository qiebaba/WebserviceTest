from suds.client import Client


class OperationWebservice:

    @staticmethod
    def send_request(url, method, data):
        # send_code_url = "http://120.24.235.105:9010/sms-service-war-1.0/ws/smsFacade.ws?wsdl"
        client = Client(url=url)
        print(client)
        # data = {"client_ip": "127.0.0.1", "mobile": "13897895651", "tmpl_id": 1}
        # result = client.service.method(data)
        result = client.service.__getattr__(method)(data)
        print(result)
        return result


do_request = OperationWebservice()
