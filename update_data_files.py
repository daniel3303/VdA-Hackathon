#!/usr/bin/env python

import mysql.connector
import yaml


def load_database_config():
    with open("config/database.yml", 'r') as databaseConfig:
        try:
            return yaml.load(databaseConfig)
        except yaml.YAMLError as exc:
            exit("Error while reading database config file")

def load_concepts(settings):
    cnx = mysql.connector.connect(user=settings["user"], password=settings["password"], host=settings["host"], database=settings["database"])
    cursor = cnx.cursor()

    query = ("SELECT id, name FROM concept")

    cursor.execute(query)

    concepts = []
    for (id, name) in cursor:
        concepts.append(name)

    cursor.close()
    cnx.close()
    return concepts

def store_lookup_table(list, name):
    with open('data/nlu/'+name+'/'+name+'_lookup.md', 'w+') as file:
        file.write("## lookup:"+name+"\n")
        for item in list:
            file.write(item+"\n")




if __name__ == "__main__":
    dbSettings = load_database_config()
    concepts = load_concepts(dbSettings)
    store_lookup_table(concepts, "concept")