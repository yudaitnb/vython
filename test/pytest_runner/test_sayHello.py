from src.transpiler.compiler import Compiler as TC
from src.interpreter.compiler import Compiler as IC
from src.interpreter.syntax.semantics import *
from test.pytest_runner.forTest import *

def test():
    # テスト用のソースコードを読み込む
    with open("test/sample_program/basic/sayHello.py", "r") as f:
        code = f.read()

    # コンパイラのインスタンスを作成
    result_i = IC(code,False).get_result_fullpath()
    result_t = TC(code,False,False).get_result_fullpath()

    # 結果を検証
    assert result_t == "Alice\n30\nHello, my name is Alice\nBob\n25\nHello, my name is Bob\n"
