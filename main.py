from hopfield import hopfield


train_paths = []
path = "train/"

for j in ['16/', '32/', '64/']:

    train_paths.append(path+j)


test_paths = []
path = "test/"
for j in ['16', '32', '64']:
    for k in ['-10/', '-30/', '-60/']:

        test_paths.append(path+j+k)

# print(train_paths)
# print(test_paths)

for i in test_paths:
    test = []
    train = []
    for j in "ABCDEFGHIJ":
        test.append(i+j+".bmp")
    t = "train/"+i.split('/')[1].split('-')[0]+"/"
    for j in "ABCDEFGHIJ":
        train.append(t+j+".bmp")
    print(test)
    print(train)
    print('-----')
    # print(i.split('/')[1])
    hopfield(train_files=train, test_files=test, theta=0.5,
             time=20000, size=(100, 100), threshold=60, des=i)
