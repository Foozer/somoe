import datetime
from models import SolarWindsSQLSettings, OrionMap, Owner
import getpass

SQL_SETTINGS_SET = False
sql_settings = None

def get_sql_settings():
    global SQL_SETTINGS_SET
    ip_address = input("Enter the IP address of the SQL Server: ")
    username = input("Enter the username for the SQL Server: ")
    password = getpass.getpass("Enter the password for the SQL Server: ")
    database = input("Enter the name of the SolarWinds database (default: SolarWindsOrion): ")
    port = input("Enter the port number of the SQL Server (default: 1433): ")

    if database == "":
        database = "SolarWindsOrion"
    if port == "":
        port = 1433

    sql_settings = SolarWindsSQLSettings(ip_address, username, password, database, port)
    SQL_SETTINGS_SET = True
    return sql_settings

def test_sql_settings(sql_settings):
    if SQL_SETTINGS_SET == False:
        print("SQL Server settings not set. Please set them first.")
        return
    else:
        print("SQL Server settings set. Testing connection...")
        connection = sql_settings.connect()
        if connection:
            print("Connection successful!")
            connection.close()
        else:
            print("Connection failed. Please try again.")
        return


def main_menu():
    global sql_settings
    print()
    print("------------------------------------------------------------")
    print("Welcome to SolarWinds Orion Map Owner Editor (SOMOE)!")
    print("Please select an option:")
    print("1. Enter SQL Server credentials")
    print("2. Display current maps and owners")
    if SQL_SETTINGS_SET == True:
        print("t. Test SQL Server connection")
    print("x. Exit")
    print("SQL Settings Set: " + str(SQL_SETTINGS_SET))
    print("------------------------------------------------------------")
    print()



    choice = input("Enter your choice: ")

    if choice == "1":
        sql_settings = get_sql_settings()
        print(sql_settings)
    elif choice == "2":
        print("Displaying current maps and owners...")
        print("Maps:")
        print("Owners:")
    elif choice == "t":
        test_sql_settings(sql_settings)
    elif choice == "x":
        print("Exiting...")
        exit()
    else:
        print("Invalid choice. Please try again.")


def main():
    while True:
        main_menu()


if __name__ == "__main__":
    main()