import requests
import os
import webbrowser
import zipfile



#path

createpath = input('Input the path (C:/Users/example/Desktop/example/)')

#createpath = 'C:/Users/test/Desktop/installer/dl/test/'


#names 
ngrokzip = 'ngrok.zip'
jarname = 'server.jar'
batname = 'start.bat'
eulaname = 'eula.txt'


ngrokpath = createpath + ngrokzip
jarpath = createpath + jarname
batpath = createpath + batname
eulapath = createpath + eulaname

# same path just without the eula ander server.jar




java8 = 'https://www.oracle.com/java/technologies/downloads/#java8-windows'
java11 = 'https://www.oracle.com/java/technologies/downloads/#java11-windows'
java17 = 'https://www.oracle.com/java/technologies/downloads/#java17-windows'

#Path setup


# Creating folder
try:
    print("creating path if not already exist")
    os.mkdir(createpath)
except FileExistsError:
    print("Folder is already there")    
else:
    print("Folder Created")

print("MC server Installer")
url = input('Enter dl link :')



print("Downloading... this could take a while")
myfile = requests.get(url)
open(jarpath , 'wb').write(myfile.content)
value = input('Do you agree the Eula (true/false) :')
if (value == 'false'):
    (exit)


if (value == 'true' ):
    url = 'https://weylyn.net/mcpyinstaller/eula.txt'
    myfile = requests.get(url)
    open(eulapath , 'wb').write(myfile.content)


    print(" Installing server")
    print("Downloading .bat file")
    url = 'https://weylyn.net/mcpyinstaller/start.bat'
    myfile = requests.get(url)
    open(batpath, 'wb').write(myfile.content)
    value = input('is java already downloaded?(true/false):')
    if (value == 'false' ):
        value = input('Are you using JDK version 8(mc1.8.8), 11(mc12.2), or version 17(mc1.17 and higher)')
        if (value == '8' ):
            webbrowser.open(java8)
            print("Execute the.bat file if JDK is installed")
        if (value == '11' ):
            webbrowser.open(java11)
            print("Execute the.bat file if JDK is installed")
        if (value == '17' ):
            webbrowser.open(java17)
            print("Execute the.bat file if JDK is installed")
    if (value == 'true' ):   
        print("The Server will now Start you may need to start it yourself it it fails")
        os.system(batpath)
        value = input('Want to download Ngrok for Portforwarting?(true/false):')
        if (value == 'true' ):
            print("downloading Ngrok")
            url = 'https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-windows-amd64.zip'
            myfile = requests.get(url)
            open(ngrokpath , 'wb').write(myfile.content)
            print("unziping ngrok")
            with zipfile.ZipFile(ngrokpath, 'r') as zip_ref:
                zip_ref.extractall(createpath)
            print ("ngrok unziped, open ngrok.exe and type ngrok tcp (your port)")

