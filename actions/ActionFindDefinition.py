from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
import mysql.connector
import yaml

class ActionFindDefinition(Action):

    databaseConfig = None

    def __init__(self):
        with open("config/database.yml", 'r') as databaseConfig:
            try:
                self.databaseConfig = yaml.load(databaseConfig)
            except yaml.YAMLError as exc:
                exit("Error while reading database config file")


    def name(self):
        return "action_give_definition"

    def run(self, dispatcher, tracker, domain):
        entities = tracker.latest_message['entities']
        concept = ""

        #confidence / value
        for entity in entities:
            if entity["entity"] == 'concept':
                concept = entity["value"]
                break


        #concept = "Benfica"
        query = "select name, description from concept where name='{0}' limit 1".format(concept)
        print(query)

        cnx = mysql.connector.connect(user=self.databaseConfig["user"], password=self.databaseConfig["password"], host=self.databaseConfig["host"],
                                      database=self.databaseConfig["database"])
        cursor = cnx.cursor()
        cursor.execute(query)
        result = cursor.fetchall()

        conceptDescription = ""
        if result != []:
            conceptDescription = result[0][1]
        else:
            conceptDescription = "Desculpa, não conheço esse conceito."

        cursor.close()
        cnx.close()

        dispatcher.utter_message(conceptDescription)


if __name__ == "__main__":
    action = ActionFindDefinition()
    #action.run(None, None, None)
