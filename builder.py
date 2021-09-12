from src.python import buildPython
from src.cpp import buildCPP
from src.c import buildC
from src.php import buildPHP
from src.typescript import buildTS
from src.rust import buildRust
from src.javascript import buildJS
from src.java import buildJava


def buildPostData(lang: str, data: str) -> str:
    if lang in ["python", "py"]:
        return buildPython(data)
    if lang == "cpp":
        return buildCPP(data)
    if lang == "c":
        return buildC(data)
    if lang == "php":
        return buildPHP(data)
    if lang in ["js", "javascript"]:
        return buildJS(data)
    if lang in ["ts", "typescript"]:
        return buildTS(data)
    if lang == "java":
        return buildJava(data)
    if lang in ["rs", "rust"]:
        return buildRust(data)

