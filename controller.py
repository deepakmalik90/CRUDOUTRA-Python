#convert into class
def init(URL,GET,POST):

    api_versions    =   {'v1'}
    resources       =   {'user'}
    response        =   {'output':' error ','status':404}

    api_version =   URL[2]
    resource    =   URL[3]

    if(api_version not in api_versions):
        return response

    if(resource not in resources):
        return response

    response    =   getattr(
                                getattr(
                                            getattr(
                                                        __import__('api.'+api_version+'.'+resource),
                                                        api_version
                                                    ),
                                            resource
                                        ),
                                        resource.capitalize()
                            )(URL,GET,POST)
    return(response.run())


        

