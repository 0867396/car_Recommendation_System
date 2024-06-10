from mysql.connector import connect, Error
from connection_detail import sql_details
import random


def get_car_by_id(vehicle_id):

    try:
        with connect(**sql_details) as connection:
            cursor = connection.cursor()
            cursor.execute(f"SELECT * FROM vehicle where vehicle_id = {vehicle_id}")
            vehicles = cursor.fetchall()
            return vehicles
    except Error as err:
        print(err)



def get_label_id_by_name(label_name):
    try:
        with connect(**sql_details) as connection:
            cursor = connection.cursor()
            cursor.execute(f'SELECT * FROM label where name = "{label_name}"')
            vehicles = cursor.fetchall()
            return vehicles
    except Error as err:
        print(err)

def get_vehicle_id_by_labelid(label_id):
    try:
        with connect(**sql_details) as connection:
            cursor = connection.cursor()
            cursor.execute(f'SELECT * FROM vehicle_label where idlabel = {label_id}')
            vehicles = cursor.fetchall()
            return vehicles
    except Error as err:
        print(err)

def get_history_username(username):
    try:
        with connect(**sql_details) as connection:
            cursor = connection.cursor()
            cursor.execute(f'SELECT idhisotry FROM history where username = "{username}"')
            histories = cursor.fetchall()
            histories = [item[0] for item in histories]  # Extracting the integer from the tuple
            print(histories)
            return histories
    except Error as err:
        print(err)

def get_all_vehicle_ids_from_history_id(history_id):
    try:
        with connect(**sql_details) as connection:
            cursor = connection.cursor()
            cursor.execute(f'SELECT vehicle_id FROM history_vehicle where idhisotry = {history_id}')
            vehicle_ids = cursor.fetchall()
            return vehicle_ids
    except Error as err:
        print(err)

def save_history(username):
    try:
        with connect(**sql_details) as connection:
            cursor = connection.cursor()
            query = '''INSERT INTO history (username) VALUES (%s);'''
            val = (username,)
            cursor.execute(query, val)
            connection.commit()

            # Retrieve the last inserted ID
            cursor.execute('''SELECT LAST_INSERT_ID();''')
            latest_id = cursor.fetchone()[0]

            return latest_id
    except Error as err:
        print(err)


def save_vehicle_history(idhistory, vehicles):
    try:
        with connect(**sql_details) as connection:
            cursor = connection.cursor()
            for i in vehicles:
                print(i[0])
                query = '''INSERT INTO history_vehicle(idhisotry, vehicle_id) VALUES (%s, %s)'''
                val = (idhistory,i[0])
                cursor.execute(query,val)
                connection.commit()
    except Error as err:
        print(err)



def get_data_by_label(label):
    label_id = get_label_id_by_name(label)[0][0]
    vehicle_ids = get_vehicle_id_by_labelid(label_id)

    # Select 10 random vehicle IDs from the list
    random_vehicle_ids = random.sample(vehicle_ids, min(10, len(vehicle_ids)))

    result = []
    for vehicle_id in random_vehicle_ids:
        result.extend(get_car_by_id(vehicle_id[0]))

    return result

print(get_data_by_label("geschikt voor fietsers"))