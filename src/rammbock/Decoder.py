def string2object(message, data):
    splitted = data.split()
    print message.header
    print splitted[:len(message.header)]
    _get_headers_from_list(message, splitted[:len(message.header)], message.header)
    _get_ies_from_list(message,splitted[len(message.header):])

def _get_headers_from_list(message, all_headers, headers_schema):
    message.header += [[headers_schema[i], all_headers[i]] for i in range(len(headers_schema))]
        
def _get_ies_from_list(message, splitted):
    message.ie += [[splitted[i][:-1], splitted[i+1]] for i in range(0,len(splitted),2)]