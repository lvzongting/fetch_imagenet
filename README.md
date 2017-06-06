# fetch_imagenet
fetch imagenet from list to build own train data 

##USE curl
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
