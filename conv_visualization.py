import numpy as np
from PIL import Image
from skimage.color import gray2rgb


data = np.load('conv2.npy')
n,ih,iw,k = data.shape

def normalize_weights(image):
    p,q = image.shape
    # print image.shape

    rgb_im = np.zeros((p,q,3),dtype=np.uint8)


    try:
        i,j = np.where(image>=0)
        # print i

        rgb_im[i,j,0] = (((image[i,j] - image[i,j].min()) / (image[i,j].max() - image[i,j].min())) * 255.9).astype(np.uint8)

        i,j = np.where(image<0)

        rgb_im[i,j,2] = (((image[i,j] - image[i,j].min()) / (image[i,j].max() - image[i,j].min())) * 255.9).astype(np.uint8)

    except Exception as e:
        print e

    return rgb_im




s = 39

mw = s*(iw+1)
mh = s*(ih+1)



for ik in range(k):

    print "the master image will by %d by %d" % (mw, mh)
    print "creating image..."
    master = Image.new(
        mode='RGB',
        size=(mw, mh),
        color=(0,0,0))  # fully transparent

    for i in range(s):
        for j in range(s):
            lx = (iw+1)*i
            ly = (ih+1)*j

            # I8 = (((data[s*i + j,:,:,0] - data[s*i + j,:,:,0].min()) / (data[s*i + j,:,:,0].max() - data[s*i + j,:,:,0].min())) * 255.9).astype(np.uint8)
            I8 = normalize_weights(data[s*i + j,:,:,ik])
            # gray_im = np.reshape(I8,(ih,iw))
            # rgb_im = gray2rgb(gray_im)
            # print rgb_im.shape
            im = Image.fromarray(np.reshape(I8,(ih,iw,3)))
            im.save('temp.png')
            image = Image.open('temp.png')
            master.paste(image,(lx,ly))

    print "saving master.png...",
    master.save('conv2/colored_conv2_'+str(ik)+'.png')
    master.show()
    print "saved!"
