import datetime
from models import SolarWindsSQLSettings, OrionMap, Owner
import getpass

def get_sql_settings():
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
    return sql_settings

def test_sql_settings(sql_settings):
    tested = False
    with sql_settings.connect() as connection:
        if connection:
            print("Connection successful!")
            return True
        else:
            print("Connection failed. Please try again.")
            return False


def display_maps(sql_settings):
    orion_maps_list = sql_settings.get_orion_maps()
    for orion_map in orion_maps_list:
        print(orion_map)

def main_menu(sql_settings_set, sql_connection_tested, sql_settings):
    print()
    print("------------------------------------------------------------")
    print("Welcome to SolarWinds Orion Map Owner Editor (SOMOE)!")
    print("Please select an option:")
    print("1. Enter SQL Server credentials")
    print("2. Display current maps and owners")
    if sql_settings_set == True:
        print("t. Test SQL Server connection")
    print("x. Exit")
    print("SQL Settings Set: " + str(sql_settings_set) + " | SQL Connection Tested: " + str(sql_connection_tested))
    print("------------------------------------------------------------")
    print()

    choice = input("Enter your choice: ")

    if choice == "1":
        sql_settings = get_sql_settings()
        sql_settings_set = True
        print(sql_settings)
    elif choice == "2":
        display_maps(sql_settings)
    elif choice == "t" and sql_settings_set == True:
        tested = test_sql_settings(sql_settings)
        if tested:
            sql_connection_tested = True
    elif choice == "x":
        print("Exiting...")
        exit()
    else:
        print("Invalid choice. Please try again.")

    return sql_settings_set, sql_connection_tested, sql_settings

def main():
    sql_settings_set = False
    sql_connection_tested = False
    sql_settings = None

    while True:
        sql_settings_set, sql_connection_tested, sql_settings = main_menu(sql_settings_set, sql_connection_tested, sql_settings)


if __name__ == "__main__":
    main()