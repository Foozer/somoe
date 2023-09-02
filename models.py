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
        

    def get_orion_maps(self):
        connection = self.connect()
        if not connection:
            print("Error: Could not establish a connection to the database.")
            return []

        cursor = connection.cursor()
        orion_maps_list = []

        query = "SELECT TOP (1000) [DisplayName], [AccountID],[UpdateDateTime],[CreateDateTime] FROM [SolarWindsOrion].[dbo].[Maps_Projects]"
        

        try:
            cursor.execute(query)
            for row in cursor.fetchall():
                orion_map = OrionMap(row[0], row[1], row[2], row[3])
                orion_maps_list.append(orion_map)
        except pymssql.Error as e:
            print(f"Error fetching data: {e}")
        finally:
            connection.close()

        return orion_maps_list

    
    

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