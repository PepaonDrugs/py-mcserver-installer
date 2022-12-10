# py-mcserver-installer

This python file is a simple minecraft server installer for windows

## Usage

After you run the scipt enter your install path

```bash
Input the path (C:/Users/example/Desktop/example/): 
```
Enter here your path like "C:/Users/example/Desktop/example/" the / at the end is important

### Please dont use directroys with spaces in it "c:/user/example/mc server/" this wont work

it will then try to create the path if it doesn`t exist

```bash
try:
    print("creating path if not already exist")
    os.mkdir(createpath)
except FileExistsError:
    print("Folder is already there")    
else:
    print("Folder Created")

```
It will ask you for your server.jar download link

use somting like [paper](https://papermc.io//), [purpur](https://purpurmc.org/) 
or [vanilla](https://www.minecraft.net/en-us/download/server)

it will download the file 
```bash
Downloading... this could take a while

```

```bash
Do you agree the Eula (true/false) :
```
you have to agree to the eula if you want to use it.



It will ask you if the right java version is already installed please proceed the instalation



It will download [Ngrok](https://ngrok.com/) to auto "portforward" if you like to do that
