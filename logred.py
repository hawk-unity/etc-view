import os
print("""
--------------------------------------------
instagram : faruk.developer
web site: farukdeveloper.online
youtube: HAWK DEFACER 
--------------------------------------------
         ETC PASSWD VİEW
--------------------------------------------
     
""")
pswd = open( "/etc/passwd", "r" )
for aLine in pswd :
    fields= aLine.split( ":" )
    print (fields[0], fields[1])
pswd.close()
print("--------------------------------------------------------------", "\n" , "\n" , "\n")
print()
print()
print()
print("--------------------------------------------------------------")
os.system("cat /etc/passwd ")
