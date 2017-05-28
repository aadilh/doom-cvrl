from PIL import Image
import numpy as np

frames = np.load('embedding_frames.npy')
n,_ = frames.shape
print n

iw = 84
ih = 84
m = 39

mw = m*(iw+1)
mh = m*(ih+1)


print "the master image will by %d by %d" % (mw, mh)
print "creating image...",
master = Image.new(
    mode='L',
    size=(mw, mh),
    color=(0,))  # fully transparent

print "created."

for i in range(m):
    for j in range(m):
        lx = (1+iw)*i
        ly = (1+ih)*j

        I8 = (((frames[m*i + j] - frames[m*i + j].min()) / (frames[m*i + j].max() - frames[m*i + j].min())) * 255.9).astype(np.uint8)
        im = Image.fromarray(np.reshape(I8,(84,84)))
        im.save('temp.png')
        image = Image.open('temp.png')
        master.paste(image,(lx,ly))
    # print "added."

print "saving master.png...",
master.save('master.png')
master.show()
print "saved!"
