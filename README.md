# fetch_imagenet
fetch imagenet from list to build own train data 

label list => url list => download list

label.lst
```
n02114548
n02138441
n02174001
n02950826
n02971356
```

get url list
```
http://www.image-net.org/api/text/imagenet.synset.geturls.getmapping?wnid=[wnid]
```

## USE curl
Fetch command
```bash
$ nohup cat download.lst | xargs -n4 curl -L &>output &`
```

download.lst File structure
```
http:/www.somedomain.com/my/file/number-one.txt
--create-dirs
-o
a-directory/hierarchy/number-one.txt
```

## USE aria2
```bash
$ aria2c -c -i download.lst -j 10 -t 5
```

download.lst File structure
```
http://server/file1.iso
  dir=/iso_images
  out=file1.img
http://server/file2.iso
  dir=/iso_images
  out=file2.img
```

## dir structure
```
-- label.lst
-- download.lst
-- label    
  |-- label.lst    
  |-- n02114548.lst    
  |-- n02138441.lst    
  |-- n02174001.lst    
  |-- n02950826.lst   
  |-- n02971356.lst    
-- image    
  |-- n02114548   
    |--00000001.jpg   
    |--00000002.jpg
    |--00000003.jpg
  |-- n02138441
    |--00000001.jpg
    |--00000002.jpg
    |--00000003.jpg
```
## delete all images not jpeg
```bash
$ for D in *; do echo $D; (cd $D && file * --mime-type |grep -v jpeg |cut -d ':' -f 1|xargs rm); done
```

## monitor the download process
```bash
$ watch 'for D in *; do echo $D; find $D -type f| wc -l; done'
O.R.
$ watch 'for D in *; do printf $D; printf "   ";find $D -type f| wc -l | xargs printf ;printf "   "; done'
```
![](https://img.vim-cn.com/b8/a45430b844b90806c92490f78d8504a47cdf33.png)
