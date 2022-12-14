import requests

class Agent:
    hosts = [{"host": "nasa", "url": "https://ntrs.nasa.gov/api/"}]

    def __init__(self, host=None, method=None, headers=[], body={}, endpoint=None, queryparams=[]):
        for item in Agent.hosts:
            if(str(item["host"]).upper() == str(host).upper()):
                self.host = item
                break
            else:
                self.host = None
        if(self.host == None):
            raise Exception("Host não cadastrado")
        self.endpoint = endpoint
        self.method = method
        self.headers = headers
        self.body = body
        print(queryparams)
        self.queryparams = Agent.biuldQueryParamsText(self, queryparams)

    def getURL(self):
        print(str(self.host["url"]) + str(self.endpoint) + str(self.queryparams))
        return str(self.host["url"]) + str(self.endpoint) + str(self.queryparams)
    
    def biuldQueryParamsText(self, params):
        ret = ""
        for param in params:
            for key in param.keys():
                if(ret == ""):
                    ret += "?"+key+"="+param[key]
                else:
                    ret += "&"+key+"="+param[key]
        return ret

    def sendRequest(self):
        if(str(self.method).upper() == "GET"):
            return requests.get(url=self.getURL()).json()
        if(str(self.method).upper() == "POST"):
            return requests.post(url=self.getURL()).json()


