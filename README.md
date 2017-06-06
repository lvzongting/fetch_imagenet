# fetch_imagenet
fetch imagenet from list to build own train data 



## USE curl
Fetch command
```bash
$ nohup cat filelist | xargs -n4 curl -L &>output &`
```

File structure
```
http:/www.somedomain.com/my/file/number-one.txt
--create-dirs
-o
a-directory/hierarchy/number-one.txt
```

## USE aria
```bash
$ aria2c -i filelist
```

File structure
```
http://server/file1.iso
  dir=/iso_images
  out=file1.img
http://server/file2.iso
  dir=/iso_images
  out=file2.img
```
