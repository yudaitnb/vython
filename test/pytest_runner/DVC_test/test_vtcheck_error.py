from src.transpiler.compiler import Compiler as TC

def test():
    # テスト用のソースコードを読み込む
    with open("test/sample_program/DVC/vtcheck_error.py", "r") as f:
        code = f.read()

    # コンパイラのインスタンスを作成し、実行
    result_t = TC(code, "vython").get_result_fullpath()

    assert result_t.message == "Version Error 1:\nincompatibly updated\n"
    assert str(type(result_t)) == "<class 'VersionError'>"