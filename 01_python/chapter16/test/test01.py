# 같은 디렉토리가 아닐 때도 가능
# 워킹 디렉토리이면 모듈화 가능
import util
import sys

print(util.INCH)

for path in sys.path:
    print(path)

# 패키지 : 모듈을 모아놓은 디렉토리
# __init__.py 가 반드시 존재해야 함(내용은 없어도 됨)

