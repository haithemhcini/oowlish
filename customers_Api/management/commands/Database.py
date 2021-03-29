
from django.core.management.base import BaseCommand, CommandError

import pandas as pd
import mysql.connector


class Command(BaseCommand):
    def handle(self, *args, **options):
        print('  customers.csv importd into your database')
    # Import CSV
    data = pd.read_csv("customers_geo.csv")

    # Data Structures
    df = pd.DataFrame(data, columns=['id', 'first_name', 'last_name',
                                     'email', 'gender', 'company', 'city', 'title', 'lat', 'lng'])

    # Connect to MySQL
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password=""
    )
    cursor = db.cursor()

    # Create Database
    cursor.execute("CREATE DATABASE oowlish")

    # Create Table
    cursor.execute('CREATE TABLE `oowlish`.`customers` ( `id` INT NOT NULL  , `first_name` VARCHAR(255) , `last_name` VARCHAR(255)  , `email` VARCHAR(255)  , `gender` VARCHAR(10)  , `company` VARCHAR(255)  , `city` VARCHAR(255)  , `title` VARCHAR(255)  , `lat` FLOAT  , `lng` FLOAT  , PRIMARY KEY (`id`)) ENGINE = MyISAM;')

    # Insert DataFrame to Table
    for row in df.itertuples():
        sql = "INSERT INTO oowlish.customers (id, first_name, last_name, email, gender, company, city, title, lat, lng) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (row.id, row.first_name, row.last_name, row.email, row.gender,
               row.company, row.city, row.title, row.lat, row.lng)
        cursor.execute(sql, val)
        db.commit()
