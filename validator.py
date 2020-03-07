from lxml import etree
import os


def validate(xml_path: str, xsd_path: str, filename: str) -> bool:

    xmlschema_doc = etree.parse(xsd_path)
    xmlschema = etree.XMLSchema(xmlschema_doc)

    #xml_doc = etree.parse(xml_path)
    # parse xml
    try:
        xml_doc = etree.parse(xml_path)
        print('XML well formed, syntax ok.')

    # check for file IO error
    except IOError:
        print('Invalid XML File')

    # check for XML syntax errors
    except etree.XMLSyntaxError as err:

        print('XML Syntax Error, see error_syntax.log')
        filename = filename+'error_syntax.log'
        createLog(filename,err.error_log)

    except:
        print('Unknown error, exiting.')
        

    # validate against schema
    try:
        xmlschema.assertValid(xml_doc)
        print('XML valid, schema validation ok.')

    except etree.DocumentInvalid as err:
        print('Schema validation error, see error_schema.log')
        filename = filename+'error_syntax.log'
        errorLog = ""
        for error in err.error_log:
            errorLog += "ERROR ON LINE " + str(error.line) + " " + str(error.message.encode("utf-8")) + "\n\n"
        createLog(filename,errorLog)
        

    except:
        print('Unknown error, exiting.')
        
    result = xmlschema.validate(xml_doc)

    return result

def createLog(filename:str, error_log:str):
    currentdir = os.getcwd()
    logdir = os.path.join(currentdir,'logs')

    if not os.path.exists(logdir):
        os.mkdir(logdir)
        print("Log Directory created ")
    else:    
        print("Log Directory already exists")
    
    filedir = os.path.join(logdir,filename)
    with open(filedir, 'w') as error_log_file:
        error_log_file.write(str(error_log))
    
