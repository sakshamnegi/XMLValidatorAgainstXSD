from validator import validate
import os

directory = os.getcwd()
schemadir = directory + '/'+"complete_version.xsd"

for fname in os.listdir('.'):
    if fname.endswith('.xml'):
        name = fname.replace(".xml","")
        print("XML file ",fname)
        fdir = directory+'/'+fname
        if validate(fdir, schemadir,name):
            print('Valid! :)')
        else:
            print('Not valid! :(')
    


