from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
import mysql.connector
import yaml
import requests

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

        legalDocument = None
        article = None
        number = None
        paragraph = None

        for entity in entities:
            if(entity["entity"] == "concept"):
                legalDocument = entity["value"]
            elif(entity["entity"] == "article"):
                article = int(entity["value"])
            elif (entity["entity"] == "number"):
                number = int(entity["value"])
            elif (entity["entity"] == "paragraph"):
                paragraph = entity["value"]

        if legalDocument is None:
            return dispatcher.utter_message("Desculpa, não sei dar uma resposta jurídica à tua pergunta.")

        legalDocumentJson = self.getJsonLegalDocument(legalDocument)
        if legalDocumentJson == []:
            return dispatcher.utter_message("Desculpa, não sei dar uma resposta jurídica à tua pergunta.")

        legalDocumentJson = legalDocumentJson[0]


        if legalDocument is not None and article is None:
            text = self.getLegalDocument(legalDocumentJson)

            if text is None:
                return dispatcher.utter_message("Não consegui encontrar o "+legalDocument+".")
            return dispatcher.utter_message(text)

        elif legalDocument is not None and article is not None and number is None:
            text = self.getArticle(legalDocumentJson, article)

            if text is None:
                return dispatcher.utter_message(
                    "Não consegui encontrar o artigo " + str(article) + "º do " + legalDocument + ".")
            return dispatcher.utter_message(text)

        elif legalDocument is not None and article is not None and number is not None and paragraph is None:
            text = self.getNumber(legalDocumentJson, article, number)

            if text is None:
                return dispatcher.utter_message(
                    "Não consegui encontrar o número "+ str(number) +" do artigo " + str(article) + "º do " + legalDocument + ".")
            return dispatcher.utter_message(text)

        elif legalDocument is not None and article is not None and number is not None and paragraph is not None:
            text = self.getParagraph(legalDocumentJson, article, number, paragraph)

            if text is None:
                return dispatcher.utter_message(
                    "Não consegui encontrar a alínea " + str(paragraph) +") do número " + str(number) + " do artigo " + str(article) + "º do " + legalDocument + ".")

            return dispatcher.utter_message(text)

        return "This should not happen"




    def getLegalDocument(self, legalDocumentJson):
        text = ""
        for article in legalDocumentJson["articles"]:
            text = text + self.getArticle(legalDocumentJson, article["number"]) + "\n"

        return text


    def getArticle(self, legalDocumentJson, article):
        articleJson = None
        text = "Artigo " + str(article) + "º\n"
        for articleI in legalDocumentJson["articles"]:
            if articleI["number"] == article:
                articleJson = articleI
                break

        if articleJson is None:
            return None

        for number in articleJson["numbers"]:
            text = text + self.getNumber(legalDocumentJson, article, number["number"]) + "\n"

        return text



    def getNumber(self, legalDocumentJson, article, number):
        articleJson = None
        numberJson = None
        text = ""
        for articleI in legalDocumentJson["articles"]:
            if articleI["number"] == article:
                articleJson = articleI
                break

        if articleJson is None:
            return None

        for numberI in articleJson["numbers"]:
            if numberI["number"] == number:
                numberJson = numberI
                break

        if numberJson is None:
            return None

        for paragraph in numberJson["paragraphs"]:
            text = text + self.getParagraph(legalDocumentJson, article, number, paragraph["letter"]) + "\n"

        return text



    def getParagraph(self, legalDocumentJson, article, number, paragraph):
        articleJson = None
        numberJson = None
        paragraphJson = None

        text = ""
        for articleI in legalDocumentJson["articles"]:
            if articleI["number"] == article:
                articleJson = articleI
                break

        if articleJson is None:
            return None

        for numberI in articleJson["numbers"]:
            if numberI["number"] == number:
                numberJson = numberI
                break

        if numberJson is None:
            return None

        for paragraphI in numberJson["paragraphs"]:
            if paragraph == paragraphI["letter"]:
                paragraphJson = paragraphI
                break

        if paragraphJson is None:
            return None


        return paragraphJson["description"]



    def getJsonLegalDocument(self, name):
        restUrl = self.databaseConfig["rest_url"]

        response = requests.get(restUrl + "/legal-documents", {"name": name})

        return response.json()["resources"]



