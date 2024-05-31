from mysql.connector import connect, Error
from connection_detail import sql_details


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



def get_data_by_label(label):
    label_id = get_label_id_by_name(label)[0][0]
    vehicle_ids = get_vehicle_id_by_labelid(label_id)
    
    result = []
    for vehicle_id in vehicle_ids[:10]:
        result.extend(get_car_by_id(vehicle_id[0]))

    return result

print(get_data_by_label("geschikt voor fietsers"))