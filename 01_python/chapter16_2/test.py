from PIL import Image, ImageFilter
import numpy as np

# 이미지 읽기
# im = Image.open('python.jpg')  # static 메서드, factory 함수(해당 객체를 만들어주는 함수)
# # im 가 이미지 객체의 인스턴스
#
# print(im.size)  # 이미지 사이즈 출력, 튜플로 출력됨
#
# # im.save('python.jpg') 만약 png 일때 jpg 로 변환하고 jpg 파일도 생성됨
#
# im.show()  # 윈도우에 있는 이미지 뷰어로 연결 후 실행은 종료 됨

# 이미지 색상 변경
# convert : "L" (gray), "RGB", "RGBA", "CMYK"
im = Image.open('python.jpg').convert("L")  # 메서드 체이닝
# im = Image.open('')
# im = convert("L")
# 원본은 바뀌지 않음
im.show()

# 썸네일 만들기, 크기 변경
im = Image.open('python.jpg')

size = (64, 64)  # 가로세로 길이가 다르면 긴쪽에 64로 맞추고 비율 유지
im.thumbnail(size)  # 원본이 바뀜

im.save('python_thumb.jpg')
im.show()
print(im.size)

# 이미지 잘라내기
im = Image.open('python.jpg')
cropImage = im.crop((100, 100, 150, 150))  # (좌, 상, 우, 하)좌표
# weith, height는 50, 50

cropImage.save('python_crop.jpg')
cropImage.show()
print(cropImage.size)

# 가운데 정사각형 자르기 - 정보 손실 발생
# 정보손실 막기위해서는 이미지보다 큰 정사각형 먼저 만들어서 위에 덮어쓰기
def center_crop(im):
    crop_size = min(im.size)

    left = (im.size[0] - crop_size) // 2  # 가로 - (자를 사이즈/2의 몫) = 50
    top = (im.size[1] - crop_size) // 2  # 0
    right = (im.size[0] + crop_size) // 2
    bottom = (im.size[1] + crop_size) // 2

    return im.crop((left, top, right, bottom))


im = Image.open('python.jpg')
cropImage = center_crop(im)
cropImage.save('python_crop.jpg')
cropImage.show()

# 이미지 회전 및 Resize
im = Image.open('python.jpg')

img2 = im.resize((600, 600))  # 크기 변경
img2.save('python_600.jpg')
img2.show()

img3 = im.rotate(90)  # 90도 회전
img3.save('python_rotate.jpg')
img3.show()

# 이미지 필터링
im = Image.open('python.jpg')
blurImage = im.filter(ImageFilter.BLUR)

blurImage.save('python_blur.png')
blurImage.show()

# numpy 배열 예제
im = Image.open('python.jpg')

# Image => numpy array(픽셀 단위로 작업할 때, 인공지능의 입출력할 때)
im2arr = np.array(im)  # im2arr.shape: height x width x channel(3차원 데이터로 나타남)

# numpy array => Image(픽셀 단위를 다시 이미지로)
arr2im = Image.fromarray(im2arr)
