from PIL import Image
import numpy as np
import random
# import Image
import os
import re


def mat2vec(x):
    m = x.shape[0]*x.shape[1]
    tmp1 = np.zeros(m)

    c = 0
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            tmp1[c] = x[i, j]
            c += 1
    return tmp1


def create_W(x):
    if len(x.shape) != 1:
        print("The input is not vector")
        return
    else:
        w = np.zeros([len(x), len(x)])
        for i in range(len(x)):
            for j in range(i, len(x)):
                if i == j:
                    w[i, j] = 0
                else:
                    w[i, j] = x[i]*x[j]
                    w[j, i] = w[i, j]
    return w


def readImg2array(file, size, threshold=145):
    pilIN = Image.open(file).convert(mode="L")
    pilIN = pilIN.resize(size)
    imgArray = np.asarray(pilIN, dtype=np.uint8)
    x = np.zeros(imgArray.shape, dtype=np.float)
    x[imgArray > threshold] = 1
    x[x == 0] = -1
    return x


def array2img(data, outFile=None):

    # data is 1 or -1 matrix
    y = np.zeros(data.shape, dtype=np.uint8)
    y[data == 1] = 255
    y[data == -1] = 0
    img = Image.fromarray(y, mode="L")
    if outFile is not None:
        img.save(outFile)
    return img


def update(w, y_vec, theta=0.5, time=100):
    for s in range(time):
        m = len(y_vec)
        i = random.randint(0, m-1)
        u = np.dot(w[i][:], y_vec) - theta

        if u > 0:
            y_vec[i] = 1
        elif u < 0:
            y_vec[i] = -1

    return y_vec


def hopfield(train_files, test_files, theta=0.5, time=1000, size=(100, 100), threshold=60, current_path=None, des=None):

    print("Importing images and creating weight matrix....")

    num_files = 0
    for path in train_files:
        print(path)
        x = readImg2array(file=path, size=size, threshold=threshold)
        x_vec = mat2vec(x)
        print(len(x_vec))
        if num_files == 0:
            w = create_W(x_vec)
            num_files = 1
        else:
            tmp_w = create_W(x_vec)
            w = w + tmp_w
            num_files += 1

    print("Weight matrix is done!!")

    counter = 0
    for path in test_files:
        y = readImg2array(file=path, size=size, threshold=threshold)
        oshape = y.shape
        y_img = array2img(y)
        # y_img.show()
        print("Imported test data")

        y_vec = mat2vec(y)
        print("Updating...")
        y_vec_after = update(w=w, y_vec=y_vec, theta=theta, time=time)
        y_vec_after = y_vec_after.reshape(oshape)
        if current_path is not None:
            outfile = current_path+"/after_"+str(counter)+".jpeg"
            array2img(y_vec_after, outFile=outfile)
        else:
            after_img = array2img(y_vec_after, outFile=None)
            after_img.save("answer/"+des.split('/')[1]+"/"+str(counter)+".bmp")
            acc = 0
            for i in range(len(y_vec_after)):
                for j in range(len(y_vec_after[i])):
                    if y[i][j] == y_vec_after[i][j]:
                        acc += 1
            print(des, acc/(len(y_vec_after)*len(y_vec_after[0]))*100)
        counter += 1
