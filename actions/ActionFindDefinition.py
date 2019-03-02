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
        concepts = []

        #confidence / value
        for entity in entities:
            if entity["entity"] == 'concept':
                concepts.append(entity["value"])

        message = ""
        if len(concepts) > 0:
            cnx = mysql.connector.connect(user=self.databaseConfig["user"], password=self.databaseConfig["password"],
                                          host=self.databaseConfig["host"],
                                          database=self.databaseConfig["database"])
            cursor = cnx.cursor()
            for concept in concepts:
                query = "select name, description from concept where name='{0}' OR '{0}' LIKE CONCAT('%', name, '%')  limit 1".format(concept)
                print(query)


                cursor.execute(query)
                result = cursor.fetchall()

                if result != []:
                    dispatcher.utter_message(result[0][1])
                else:
                    dispatcher.utter_message("Desculpa, não conheço o conceito {0}.".format(concept))

            cursor.close()
            cnx.close()
        else:
            dispatcher.utter_message("Desculpa, não conheço esse conceito.")




if __name__ == "__main__":
    action = ActionFindDefinition()
    #action.run(None, None, None)
