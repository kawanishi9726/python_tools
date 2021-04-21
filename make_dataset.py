import sys
import os
import glob
from PIL import Image

def resize(in_dir,out_dir,width,height):
    os.makedirs(out_dir, exist_ok=True)

    files = glob.glob(in_dir+"/*.jpg")
    num = len(glob.glob(out_dir+"/*.jpg"))

    for i,f in zip(range(len(files)),files):
        img = Image.open(f)
        img_resize = img.resize((width,height))
        root, ext = os.path.splitext(f)
        basename = os.path.basename(root)
        img_resize.save(os.path.join(out_dir, str(num + i) + ext))
        
def make_dataset(in_dir,out_dir,size):
    
    dir_names = os.listdir(path=in_dir)
    print(dir_names)
    data = []
    for dir_name in dir_names:
        resize(in_dir+"/"+dir_name,out_dir,size,size)
        files = glob.glob(in_dir+"/"+dir_name+"/*.jpg")
        data += [dir_name]*len(files)
        
    print(len(data))
    f = open(out_dir+"/data.csv", "w")
    f.write(",".join(data))

make_dataset(sys.argv[1],sys.argv[2],int(sys.argv[3]))