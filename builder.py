try:
    from src.runners import *
except:
    from .src.runners import *


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
    if lang in ["sh", "bash"]:
        return buildBash(data)
    if lang in ['csharp', 'cs']:
        return buildCSharp(data)
    if lang in ['go', 'golang']:
        return buildGo(data)
    if lang in ['haskell', 'hs']:
        return buildHaskell(data)
    if lang in ['julia', 'jl']:
        return buildJulia(data)
    if lang in ['lua', 'l']:
        return buildLua(data)
    if lang in ['pas', 'pascal']:
        return buildPascal(data)
    if lang in ['perl', 'pl']:
        return buildPerl(data)
    if lang in ['r', 'rlang']:
        return buildR(data)
    if lang in ['ruby', 'rb']:
        return buildRuby(data)
    if lang in ["golang", "go"]:
        return buildGo(data)

