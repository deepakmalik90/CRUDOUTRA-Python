#convert into class
import sys
import os
import controller
def application(environ, start_response):

    status_codes    =   {200:"200 OK",404:"404 Not Found"}  
    status          =   status_codes[200]   
    POST    =   {}
    args    =   sys.stdin.read().split('&')
    for arg in args: 
        t   =   arg.split('=')
        if len(t)>1 :
            k,v =   arg.split('=')
            POST[k] =   v

    GET     =   {}
    args    =   environ["QUERY_STRING"].split('&')
    for arg in args: 
        t   =   arg.split('=')
        if len(t)>1 :
            k,v =   arg.split('=')
            GET[k] =   v

    URL     =   environ["PATH_INFO"].split('/')

    output  =   ''    

    if(len(URL)>3):
       response         =   controller.init(URL,GET,POST) 
       output           =   response['output']  
       status           =   status_codes[response['status']]   
    else:
        status          =   status_codes[404]     


    response_headers = [('Content-type', 'text/json'),('Content-Length', str(len(output)))]
    start_response(status, response_headers)

    return [output]


    # Phase 1 - Fixing Things (Replacing, Growing, Removing, Adding)
    # Phase 2 - Improving Things (No Hairs, Height, Spotless Skin, Muscular Body, Stamina, Strength)
    # Phase 3 - Modifying Thins ()