pswd = file( "/etc/passwd", "r" )
for aLine in pswd :
    fields= aLine.split( ":" )
    print (fields[0], fields[1])
pswd.close()