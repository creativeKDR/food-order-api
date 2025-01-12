
Dev = True

if Dev:
    userName = 'dbAdmin'
    password = 'zKDCkMj6UHlUp[6_'
    server = 'localhost'
    dbName = 'foodappdb'
    port = 3306
else:
    userName = ''
    password = ''
    server = ''
    dbName = ''
    port = ''

SQLALCHEMY_DATABASE_URL = f"mysql+mysqlconnector://{userName}:{password}@{server}:{port}/{dbName}"
