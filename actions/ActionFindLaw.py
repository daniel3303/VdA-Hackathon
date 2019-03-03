from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
import mysql.connector
import yaml

class ActionFindLaw(Action):

    databaseConfig = None

    def __init__(self):
        with open("config/database.yml", 'r') as databaseConfig:
            try:
                self.databaseConfig = yaml.load(databaseConfig)
            except yaml.YAMLError as exc:
                exit("Error while reading database config file")


    def name(self):
        return "action_give_law"

    def run(self, dispatcher, tracker, domain):
        entities = tracker.latest_message['entities']
        print(entities)

        dispatcher.utter_message("Procurar lei")


