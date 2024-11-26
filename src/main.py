import cv2
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import image as mpimg
from matplotlib import ticker
from PIL import Image

img = Image.open('img/e_coli_90s.jpg')
print(img.info.get('dpi'))

dpi = 100

fig = plt.figure(figsize=(float(img.size[0]), float(img.size[1])))
ax = fig.add_subplot(111)

# Remove whitespace from around the image
fig.subplots_adjust(left=0,right=1,bottom=0,top=1)

interval = img.size[0] / 10
loc = ticker.MultipleLocator(base=interval)
ax.xaxis.set_major_locator(loc)
ax.yaxis.set_major_locator(loc)

# Add the grid
ax.grid(which='major', axis='both', linestyle='-')

ax.imshow(img)
plt.show()