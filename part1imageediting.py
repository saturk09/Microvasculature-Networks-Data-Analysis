import cv2
import numpy as np
def main():
# Add Your Image File Name Here
# If the program can't find the image in your folder, right click on image and
# copy path. Then, paste the entire path into the image variable definition
fileName = 'finishedDrawing.jpg'
#"C:
\Users\mroli\Downloads\Image_Skeletonization\Image_Skeletonization\miniNetwork.png"
# "C:\\Users\\mroli\\Downloads\\Image_Skeletonization\\Image_Skeletonization\
\finishedDrawing.jpg"
image = cv2.imread("C:\\Users\\mroli\\Downloads\\Image_Skeletonization\
\Image_Skeletonization\\miniNetwork.png") #use fileName if not working
# Call Thinning / Skeletonization Function
skeleton(image, showImg=0, saveSkeleton=1, OutFileName='myCenterlineImage')
# 1 ~ True
# 0 ~ False
def skeleton(image, showImg=0, saveSkeleton=1, OutFileName='Output'):
image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
thinned = cv2.ximgproc.thinning(image,
thinningType=cv2.ximgproc.THINNING_ZHANGSUEN)
thres = np.mean(image)
Pz, Px = thinned.shape
for i in range(Pz):
for j in range(Px):
if (thinned[i, j] != 0):
image[i,j] = 0
elif (thinned[i, j] == 0 and image[i,j] != 0):
image[i,j] = 255
else:
image[i,j] = 0
if saveSkeleton == 1:
cv2.imwrite(f'{OutFileName}.png', thinned)
if showImg == 1:
cv2.imshow("Original", image)
cv2.imshow("Skeleton", thinned)
cv2.waitKey(0)
if __name__ == "__main__":
main()
