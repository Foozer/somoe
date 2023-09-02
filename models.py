import pymssql

class SolarWindsSQLSettings:
    def __init__(self, ip_address, username, password, database="SolarWindsOrion", port=1433):
        self.ip_address = ip_address
        self.username = username
        self.password = password
        self.database = database
        self.port = port

    def __str__(self):
        return f"SQLSettings({self.ip_address}, {self.username}, {self.database}, {self.port})"

    def connect(self):
        try:
            conn = pymssql.connect(server=self.ip_address, user=self.username, password=self.password, 
                                   database=self.database, port=self.port)
            return conn
        except pymssql.Error as e:
            print(f"Error connecting to database: {e}")
            return None

    
    

class OrionMap:
    def __init__(self, display_name, owner, created_date, edited_date):
        self.display_name = display_name
        self.owner = owner
        self.created_date = created_date
        self.edited_date = edited_date

    def __str__(self):
        return f"OrionMap({self.display_name}, {self.owner}, {self.created_date}, {self.edited_date})"
    

class Owner:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Owner({self.name})"