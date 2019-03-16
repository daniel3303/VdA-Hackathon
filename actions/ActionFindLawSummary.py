from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
import mysql.connector
import yaml
import requests
import re

class ActionFindLawSummary(Action):

    databaseConfig = None

    def __init__(self):
        with open("config/database.yml", 'r') as databaseConfig:
            try:
                self.databaseConfig = yaml.load(databaseConfig)
            except yaml.YAMLError as exc:
                exit("Error while reading database config file")

    def name(self):
        return "action_give_law_summary"

    def run(self, dispatcher, tracker, domain):
        legalDocument = tracker.get_slot('lastLegalDocument')
        article = integer_from_string(tracker.get_slot('lastArticle'))


        if(article is None or legalDocument is None):
            return [SlotSet("lastArticle", None), SlotSet("lastLegalDocument", None), SlotSet('lastArticleHasSummary', False)]



        legalDocumentJson = self.getJsonLegalDocument(legalDocument)
        if legalDocumentJson == []:
            dispatcher.utter_message("Desculpa, não sei dar uma resposta jurídica à tua pergunta.")
            return [SlotSet("lastArticle", None), SlotSet("lastLegalDocument", None), SlotSet('lastArticleHasSummary', False)]

        legalDocumentJson = legalDocumentJson[0]



        # Asked for article in a legal document
        if legalDocument is not None and article is not None:
            text = self.getArticleSummary(legalDocumentJson, article)

            if text is None:
                dispatcher.utter_message(
                    "Não consegui encontrar o resumo do artigo " + str(article) + "º do " + legalDocument + ".")
                return [SlotSet("lastArticle", None), SlotSet("lastLegalDocument", None),
                        SlotSet('lastArticleHasSummary', False)]


            dispatcher.utter_message("Aqui vai a explicação do artigo "+str(article)+"º do " + legalDocument + ":")
            dispatcher.utter_message(text)
            return [SlotSet("lastArticle", None), SlotSet("lastLegalDocument", None),
                    SlotSet('lastArticleHasSummary', False)]


        return "This should not happen"


    def getArticleSummary(self, legalDocumentJson, article):
        articleJson = None
        for articleI in legalDocumentJson["articles"]:
            if articleI["number"] == article:
                articleJson = articleI
                break

        if articleJson is None:
            return "Artigo não encontrado."
        elif not 'summary' in articleJson:
            return "Resumo não encontrado."


        text = articleJson["summary"]
        return text


    def getLegalDocumentName(self, legalDocumentJson):
        return legalDocumentJson["name"]


    def articleHasSummary(self, legalDocumentJson, article):
        for articleI in legalDocumentJson["articles"]:
            if articleI["number"] == article:
                if('summary' in articleI and articleI['summary'] != ''):
                    return True
                else:
                    return False
        return False


    def getJsonLegalDocument(self, name):
        restUrl = self.databaseConfig["rest_url"]

        response = requests.get(restUrl + "/legal-documents", {"name": name})

        return response.json()["resources"]

def integer_from_string(string):
    result = [e for e in re.split("[^0-9]", string) if e != '']

    return max(map(int, result))



