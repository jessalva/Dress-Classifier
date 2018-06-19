import os
from PIL import Image

path = './data/'
out = './preprocessed/'
datadir = os.listdir(path)

def resize():
    n =0
    for dir in datadir:
        dirpath = path+dir+'/'
        classdir = os.listdir(dirpath)
        for classes in classdir:
            classpath = dirpath + classes + '/'
            filedir = os.listdir(classpath)
            for file in filedir:
                if(os.path.isfile(classpath+file)):
                    n = n+1
                    print(str(n)+' processed : Last Processed : '+classpath+file)
                    im = Image.open(classpath+file)
                    imResize = im.resize((224,224),Image.ANTIALIAS)
                    imResize.save(out+dir+'/'+classes+'/'+file,'JPEG',quality=90)
resize()