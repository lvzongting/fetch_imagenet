#!/usr/bin/env python
#-*- encoding:utf-8 -*-

import os
import glob
import time
import urllib
from requests.exceptions import ConnectionError

label_file = open('label.lst')
label_path = 'label/'
map_url    = 'http://www.image-net.org/api/text/imagenet.synset.geturls.getmapping?wnid='

if not os.path.exists(label_path):
    os.makedirs(label_path)

for line in label_file.readlines():
    line = line[:-1]
    if os.path.isfile(label_path+line+'.lst'):
        print 'Already exist %s' % line
        continue

    try:
        print 'Fetching...',map_url+line, label_path+line+'.lst'
        urllib.urlretrieve(map_url+line, label_path+line+'.lst')
    except ConnectionError, e:
        print 'could not download %s' % line
        continue
    time.sleep(1.5)

num_class    = 1000
len_name      = len(str(num_class))
image_path    = 'image/'
d_file        = open('download.lst','w')

'''
download.lst example
http://server/file1.iso
  dir=/iso_images
  out=file1.img
http://server/file2.iso
  dir=/iso_images
  out=file2.img
then download images using aria2 
$aria2c -c -i download.lst -j 10 -t 10
monitor
$ watch "for D in *; do echo $D; find $D -type f| wc -l; done"
'''

for filename in glob.glob(label_path + '*.lst'):
    flag = 1
    url_file = open(filename)   
    for line in url_file.readlines():
        try:
            line = line.split(' ')[1][:-1]
        except:
            print line
            continue
        #print line 
        #print '  dir=' + image_path + filename.split('/')[-1][:-4]
        #print '  out=' + str(flag).zfill(len_name)+ '.jpg'
        d_file.write(line + '\r\n')
        d_file.write('  dir=' + image_path + filename.split('/')[-1][:-4] + '\r\n')
        d_file.write('  out=' + str(flag).zfill(len_name)+ '.jpg' + '\r\n')
        if flag >= num_class: break
        flag = flag + 1
    print filename+' done!'
    #break
   
d_file.close() 
    
    

