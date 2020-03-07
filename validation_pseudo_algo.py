for each document-
    validate against extract_schema
    if(valid):
        return true
    else:
        pull content of 'version'
        validate against version_schema
        if(valid):
            return true
        else
            pull content of 'composition'
            validate against composition_schema
            if(valid):
                return true
            else:
                if(ResolvableErrors()==true):
                    resolve errors
                    return true
                else:
                    return false

                    