
def database_config(DATABASE_URL):
    '''This function returns [user, password, host, db] from DATABASE_URL'''

    col = []
    for i in range(len(DATABASE_URL)):
        if(DATABASE_URL[i] == ':'):
            col.append(i)

    user = DATABASE_URL[col[0]+3 : col[1]]
    at = 0
    ques = 0
    for i in range(len(DATABASE_URL)):
        if(DATABASE_URL[i] == '@'):
            at = i
            break
    password = DATABASE_URL[col[1]+1 : at]

    slash = []

    for i in range(len(DATABASE_URL)):
        if(DATABASE_URL[i] == '/'):
            slash.append(i)

    host = DATABASE_URL[at+1 : slash[2]]


    for i in range(len(DATABASE_URL)):
        if(DATABASE_URL[i] == '?'):
            ques = i

    db = DATABASE_URL[slash[2]+1 : ques]
    output = [user, password, host, db]
    return output