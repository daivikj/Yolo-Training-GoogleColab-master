import os,sys
folder = 'C:/Users/daivi/Yolo-Training-GoogleColab-master/annotated'
for filename in os.listdir(folder):
       infilename = os.path.join(folder,filename)
       if not os.path.isfile(infilename): continue
       oldbase = os.path.splitext(filename)
       newname = infilename.replace('.png', '.jpg')
       output = os.rename(infilename, newname)

