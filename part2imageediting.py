import cv2
import numpy as np
def main():
# User Input Section
# Enter Your FilePath Here
file_path = 'NetworkRGB.png'
# Read Image File
image = cv2.imread(file_path)
# Call Split RGB Function (Saves 3 Images)
split_RGB(image)
# Define X-Coords and Z-Coords
x_dim = 540
z_dim = 820
# Assign Y-Coord for Colors
R_Ycord = 5
B_Ycord = 25
G_Ycord = 40
# Add Clockwise Rotation to Image
rotate = 90
# End of User Input Section
Ycoords = [R_Ycord, B_Ycord, G_Ycord]
# Loop through 3 images
RGB_arr = ['red.png', 'blue.png', 'green.png']
for i, file in enumerate(RGB_arr):
# Call Function to Process Image to Binary
# Add Any Image Rotation
thresh_img = process_image(file_path=file, rotation=rotate,
show_image=False)
# Call Function to Obtain Centerline Coordinates
# (Reduction Factor ~ 4-5 Recommended to Keep Total Points/Coord File <
3000)
points = map_image(thresh=thresh_img, x_dim=x_dim, y_dim=Ycoords[i],
z_dim=z_dim, reduction_factor=5)
# Call Function to Save Points File
write_to_file(points=points, out_file_name=f'Points{i+1}
_YCoord_{Ycoords[i]}')
def split_RGB(image):
# Check if the image was loaded properly
if image is None:
print("Error: Could not read the image.")
return
# Split the image into its RGB components
blue_channel, green_channel, red_channel = cv2.split(image)
# Create blank channels for the other colors
zeros_channel = np.zeros_like(blue_channel)
# Create images with only red, green, and blue channels
red_image = cv2.merge((zeros_channel, zeros_channel, red_channel))
green_image = cv2.merge((zeros_channel, green_channel, zeros_channel))
blue_image = cv2.merge((blue_channel, zeros_channel, zeros_channel))
# Save the images
cv2.imwrite('red.png', red_image)
cv2.imwrite('green.png', green_image)
cv2.imwrite('blue.png', blue_image)
def write_to_file(points, out_file_name='Output'):
Npoints = int(len(points[:,1]))
with open(f"{out_file_name}.pts", 'w', newline='') as file:
for i in range(Npoints):
file.write(f'{points[i,0]} {points[i,1]} {points[i,2]}\n')
def process_image(file_path: str, rotation=90, show_image=False):
image = cv2.imread(file_path) # Put in the file path / name in here and load
into python
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # Turns the image to gray scale
_, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV *
cv2.THRESH_OTSU) # Applies a threshold --> Black or White
try:
match rotation:
case 0:
thresh = thresh
case 90:
thresh = cv2.rotate(thresh, cv2.ROTATE_90_CLOCKWISE)
case 180:
thresh = cv2.rotate(thresh, cv2.ROTATE_180)
case 270:
thresh = cv2.rotate(thresh, cv2.ROTATE_90_COUNTERCLOCKWISE)
case _:
raise ValueError("Error: Invalid Image Rotation (Only Accepts 90°,
180°, 270°)")
except:
print('Invalid Image Rotation (Only Accepts 90°, 180°, 270°)')
if show_image != False:
# Display the Original and Processed Image
cv2.imshow("Original Image", image)
cv2.imshow("Processed Image", thresh)
# Display the images until a key is pressed
cv2.waitKey(0)
cv2.destroyAllWindows()
return thresh
def map_image(thresh, x_dim: float, y_dim: float, z_dim: float,
reduction_factor=1):
x = []
y = []
z = []
x_dim = x_dim
z_dim = z_dim
y_dim = y_dim
image = thresh
width, height = image.shape
for i in range(0, height):
for j in range(0, width):
if image[j, i] == 255:
x.append(j * (x_dim/width))
z.append(i * (z_dim/height))
y.append(y_dim)
points = np.vstack((x,y,z)).transpose()
factor= reduction_factor
points = points[::factor]
return points
if __name__ == '__main__':
main()
