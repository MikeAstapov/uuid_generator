import uuid6



def uid_generate():
    new = uuid6.uuid6().int
    return new



uid_generate()