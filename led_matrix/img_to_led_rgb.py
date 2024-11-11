from PIL import Image
import glob
#import numpy as np

formats = [".png", ".jpg", ".jpeg"]

def check(j):
  r = 0
  for k in formats:
    if k in j:
      r = 1
      break
  return r

files = [i.split("/", 1)[1] for i in glob.glob('./*') if check(i)]
file = 0;

try:
  file = files[0];
  im = Image.open(file)
except IndexError:
  print("no file found")
  print("upload image")
  exit()

print("file name:\t" + file)
sx, sy = im.size
im = im.convert("RGB")
im_data = im.getdata()
print("dimensions:\t{}x, {}y".format(sx, sy))

xy = lambda x,y: y*sx+x 
i=0
f = open("dest.txt", "w")
f.write('{')
print("writing to dest.txt")
for v in range(sy):
  for u in range(sx):
    i = xy(u,v)
    if i == sy*sx-1:
      f.write("{},{},{}".format(im_data[i][0], im_data[i][1], im_data[i][2]))
    else:
      f.write("{},{},{},".format(im_data[i][0], im_data[i][1], im_data[i][2]))
f.write("};")
f.close()
print("done")

