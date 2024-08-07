import requests
try:
    from builder import buildPostData
except:
    from .builder import buildPostData
import json
import sys


class Compiler:
    def __init__(self, lang: str, data: str) -> None:
        self.lang = lang
        self.data = data
        self.api_url = "https://wandbox.org/api/compile.ndjson"
        self.headers = {'Content-type': 'application/json'}
        self.output = ""
        self.supported_langs = [
                    #'bash',
                    'c',
                    #'csharp',
                    'cpp',
                    #'cs',
                    'go',
                    'golang',
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

        # self.postData()
        # self.sendData()
        # self.parseResponse()

    def postData(self) -> bool:
        if self.data and self.lang in self.supported_langs:
            data = buildPostData(self.lang, self.data)
            self.data = data
            return self.sendData()
        return False

    def parseResponse(self) -> bool:
        try:
            std = ["stdout", "stderr", "compilermessagee"]
            data = self.output
            data = data.split("\n")
            data = [json.loads(data[i]) for i in range(len(data) - 1)]
            stdout = ""
            exit_code = ""
            for x in data:
                for k, v in x.items():
                    if v.lower() in std:
                        stdout += x['data']
                    if v == "ExitCode":
                        exit_code = x['data']
            output = {"exit_code": exit_code, "body": stdout}
            self.output = output
            return True
        except Exception:
            return False

    def sendData(self) -> bool:
        if self.data: 
            res = requests.post(self.api_url, self.data)
            if res.status_code == 404:
                print(res.text)
                exit(1)
            self.output = res.text
            return self.parseResponse()
        return False

    def getResponse(self):
        return self.output


def argparser():
    args = sys.argv[1:]
    if len(args) < 2:
        return print("Error! 2 arguments expected. Usage: python main.py [lanaguage] [code]")
    lang = args[0]
    code = args[1]
    res = (main(lang, code))
    print(res['body'])
    print("Exited with return code: " + str(res['exit_code']))


def main(lang: str, data: str) -> dict:
    c = Compiler(lang, data)
    if c.postData():
        return c.getResponse()
    else:
        return {"body": "Erro! Não foi possível executar!", "exit_code": 127}


if __name__ == "__main__":
    # print(main("py", 'print("hello")'));
    argparser()

