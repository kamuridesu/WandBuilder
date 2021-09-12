import requests
from builder import buildPostData
import json


class Compiler:
    def __init__(self, lang: str, data: str) -> None:
        self.lang = lang
        self.data = data
        self.api_url = "https://wandbox.org/api/compile.ndjson"
        self.headers = {'Content-type': 'application/json'}
        self.output = ""
        self.postData()
        self.sendData()
        self.parseResponse()

    def postData(self) -> bool:
        supported_langs = [
                    #'bash',
                    'c',
                    #'csharp',
                    'cpp',
                    #'cs',
                    #'go',
                    #'golang',
                    #'haskel',
                    #'julia',
                    'java',
                    'js',
                    'javascript',
                    #'lua',
                    'php',
                    #'pascal',
                    #'perl',
                    'py',
                    'python',
                    #'r',
                    #'ruby',
                    'rust',
                    'rs',
                    #'sql',
                    'typescript',
                    'ts',
                ]
        if self.data and self.lang in supported_langs:
            data = buildPostData(self.lang, self.data)
            self.data = data
            return True
        return False

    def parseResponse(self):
        data = self.output
        data = data.split("\n")
        data = [json.loads(data[i]) for i in range(len(data) - 1)][1:3]
        output = {"exit_code": data[1]['data'], "body": data[0]['data']}
        self.output = output

    def sendData(self) -> bool:
        if self.data: 
            res = requests.post(self.api_url, self.data)
            self.output = res.text

    def getResponse(self):
        return self.output


def main(lang: str, data: str) -> dict:
    c = Compiler(lang, data)
    return c.getResponse()


if __name__ == "__main__":
    print(main("py", 'print("hello")'));
