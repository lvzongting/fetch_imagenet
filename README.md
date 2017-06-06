# fetch_imagenet
fetch imagenet from list to build own train data 

label list => url list => download list

get url list
```
http://www.image-net.org/api/text/imagenet.synset.geturls.getmapping?wnid=[wnid]
```

## USE curl
Fetch command
```bash
$ nohup cat downloadlist | xargs -n4 curl -L &>output &`
```

downloadlist File structure
```
http:/www.somedomain.com/my/file/number-one.txt
--create-dirs
-o
a-directory/hierarchy/number-one.txt
```

## USE aria2
```bash
$ aria2c -i downloadlist
```

downloadlist File structure
```
http://server/file1.iso
  dir=/iso_images
  out=file1.img
http://server/file2.iso
  dir=/iso_images
  out=file2.img
```
