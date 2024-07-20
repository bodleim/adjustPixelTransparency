from PIL import Image
import numpy as np
import cv2
import matplotlib.pyplot as plt
from tqdm import tqdm # indicate progression degree module

resize_degree = 1

def pixel_transparency(imgPath):
	img = Image.open(imgPath)

	img = img.resize((int(img.size[0]*(resize_degree)), int(img.size[1]*(resize_degree))))

	# rgba data of origin img
	imgData = img.convert("RGBA")

	# put in numpy array
	imgData_np = np.array(imgData)

	# grayscaling
	gray = img.convert("L")

	# after grayscale, convert RGBA
	gray_RGBA = gray.convert("RGBA")

	# gray_RGBA in numpy array
	gray_RGBA_np = np.array(gray_RGBA)

	# put in numpy array
	gray_np = np.array(gray)

	allpixel_amount = gray.width * gray.height # number of pixels to process
	print('가로 픽셀: ' + str(gray.width) + '\n세로 픽셀: ' + str(gray.height)
      	+ '\n변형을 진행할 총 픽셀 수: ' + str(gray.width * gray.height))
	
	print(gray_RGBA_np)

	# save brightness of pixels in numpy array
	brightness_values = np.array(gray).flatten()

	print("Brightness values: ", brightness_values)

	# img processing
	newData = gray_RGBA_np

	pixel_pos = 0 # now pixel position (flatten index)

	print('start.')

	# img Alpha change and save
	for i in tqdm(range(gray_RGBA_np.shape[0])):
	    	for j in range(gray_RGBA_np.shape[1]):
        		#print(str(pixel_pos))
        			newData[i, j, 3] = brightness_values[pixel_pos]
	        		pixel_pos = pixel_pos + 1 # count

	#newData = newData.astype("uint8") <- 그레이스케일 이미지는 필요 없음
	edited_img = Image.fromarray(newData, "RGBA")

	# grayscale while maintaining transparency
	edited_img = edited_img.rotate(270, expand=1)
	print("end processing. \n\n")
	print("[result]\n" + str(newData))
