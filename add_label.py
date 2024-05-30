import pandas as pd

# Lees de dataset in
dataset = pd.read_csv('car_details_v4.csv' , sep=';')
print(dataset.columns)

# Bekijk de kolomnamen om te controleren welke namen worden gebruikt


# Kolomnamen aanpassen aan de juiste naam
# Hier vervang je 'Seating Capacity' door de juiste naam van de kolom in je dataset
def add_labels(row):
    labels = []
    
    # Geschikt voor gezinnen: Seating capacity >= 5
    if row['Seating Capacity'] >= 5:
        labels.append('geschikt voor gezinnen')
    
    # Geschikt voor studenten: Seating capacity <= 3
    if row['Seating Capacity'] <= 3:
        labels.append('geschikt voor studenten')
    
    return ', '.join(labels)

# Voeg een nieuwe kolom 'Labels' toe aan de dataset met de bijbehorende labels voor elke auto
dataset['Labels'] = dataset.apply(add_labels, axis=1)

# Sla de dataset op met de toegevoegde labelkolom
dataset.to_csv('vehicle_dataset_with_labels.csv', index=False)
