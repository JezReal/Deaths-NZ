import csv
import pymongo


def get_collection():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    database = client['births_deaths']
    collection = database['births_deaths']

    return collection


def import_data_to_database():
    collection = get_collection()
    collection.drop()
    print('Collection dropped')

    collection = get_collection()
    data = []

    with open('bd-dec21-deaths-by-sex-and-age.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0

        for row in csv_reader:
            if line_count != 0:
                if row[2] != 'Total' and row[1] != 'Total':
                    current_data = {
                        'Period': row[0],
                        'Sex': row[1],
                        'Age': row[2],
                        'Count': row[3]
                    }
                    data.append(current_data)

            line_count += 1

    collection.insert_many(data)


def get_male_deaths_from_2010():
    collection = get_collection()

    result = collection.find({'Period': '2010', 'Sex': 'Male'})

    return result


def get_total_deaths():
    collection = get_collection()

    result = collection.find({}, {'_id': 0, 'Age': 0})

    return result


def get_total_male_deaths():
    collection = get_collection()

    result = collection.find({'Sex': 'Male'}, {'_id': 0, 'Sex': 0})

    return result


def get_total_female_deaths():
    collection = get_collection()

    result = collection.find({'Sex': 'Female'}, {'_id': 0, 'Sex': 0})

    return result


def get_total_deaths_by_year(year):
    collection = get_collection()

    result = collection.find({'Period': year}, {'_id': 0, 'Sex': 0})

    return result


def get_total_deaths_by_age_group(age_group):
    collection = get_collection()

    result = collection.find({'Age': age_group}, {'_id': 0, 'Sex': 0})

    return result
