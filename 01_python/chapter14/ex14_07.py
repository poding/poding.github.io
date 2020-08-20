# 파일 관리 함수
# shutil = shell utility 의 약자
import shutil

shutil.copy("live.txt", "live2.txt")

import os

files = os.listdir('/home..')  # 파일경로 X 디렉토리 경로여야 함, 디렉토리 경로가 리스트로 리턴 됨
for f in files:
    print(f)

# 디렉토리 관리 함수
def dumpDir(path):
    files = os.listdir(path)
    for f in files:
        fullPath = os.path.join(path, f)  # 디렉토리와 파일 결합할 때 사용하는 함수
        if os.path.isdir(fullPath):
            print("[%s]"%fullPath)
            dumpDir(fullPath)  # 재귀호출
        else:
            print("\t" + f)

dumpDir("/home..")

