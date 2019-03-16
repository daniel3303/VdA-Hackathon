#!/usr/bin/env python3

import mysql.connector
import yaml
import os

trainCustomQuestions = False

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
            file.write("- "+item+"\n")

def get_custom_questions(settings):
    if(trainCustomQuestions != True):
        return []

    cnx = mysql.connector.connect(user=settings["user"], password=settings["password"], host=settings["host"],
                                  database=settings["database"])
    cursor = cnx.cursor()

    query = ("SELECT id, text, answer_id FROM question ORDER BY answer_id ASC")
    cursor.execute(query)

    questions = []
    for (id, text, answer_id) in cursor:
        questions.append((text, answer_id))

    cursor.close()
    cnx.close()

    return questions

def get_custom_answers(settings):
    if (trainCustomQuestions != True):
        return []

    cnx = mysql.connector.connect(user=settings["user"], password=settings["password"], host=settings["host"],
                                  database=settings["database"])
    cursor = cnx.cursor()

    query = ("SELECT id, text FROM answer ORDER BY id ASC")
    cursor.execute(query)

    answers = []
    for (id, text) in cursor:
        answers.append((id, text))

    cursor.close()
    cnx.close()

    return answers



def update_custom_answers_train(questions):
    if len(questions) > 0:
        with open('data/nlu/custom_answer/custom_answer_train.md', 'w+') as file:
            lastAnswerId = None
            for question in questions:
                strippedText = question[0].strip('\n')
                if(lastAnswerId != question[1]):
                    file.write("## intent:custom_answer_"+str(question[1])+"\n")
                    lastAnswerId = question[1]
                file.write("- " + strippedText + "\n")
    else:
        if os.path.exists("data/nlu/custom_answer/custom_answer_train.md"):
            os.remove("data/nlu/custom_answer/custom_answer_train.md")


def get_custom_domain():
    with open("data/dialogue/domain_custom.yml", 'r') as domain:
        try:
            return yaml.load(domain)
        except yaml.YAMLError as exc:
            exit("Error while reading domain_custom.yml config file")

def generate_domain(dbSettings):
    customDomain = get_custom_domain()
    customAnswers = get_custom_answers(dbSettings)

    # register intents
    for answer in customAnswers:
        customDomain["intents"].append("custom_answer_"+str(answer[0]))

    with open('data/dialogue/domain.yml', 'w+') as file:
        file.write(yaml.dump(customDomain))

    # register utter templates
    for answer in customAnswers:
        customDomain["templates"]["utter_custom_answer_"+str(answer[0])] = [{ "text": answer[1] }]

    # register utter actions
    for answer in customAnswers:
        customDomain["actions"].append("utter_custom_answer_" + str(answer[0]))

    with open('data/dialogue/domain.yml', 'w+') as file:
        file.write(yaml.dump(customDomain))


def generate_story():
    customAnswers = get_custom_answers(dbSettings)

    with open("data/dialogue/stories.md", 'w+') as story:
        #copy custom stories to the top of the file
        with open("data/dialogue/stories_custom.md", 'r') as customStory:
            for line in customStory:
                story.write(line)

        # generate new stories
        for answer in customAnswers:
            # first story
            story.write("\n##\n")
            story.write("* custom_answer_"+str(answer[0]))
            story.write("\n\t- utter_custom_answer_" + str(answer[0]) + "\n")

            # second story
            story.write("\n##\n")
            story.write("* greet\n")
            story.write("\t- utter_greet\n")
            story.write("\t- utter_ask_name\n")
            story.write("* custom_answer_" + str(answer[0]))
            story.write("\n\t- utter_custom_answer_" + str(answer[0]) + "\n")




if __name__ == "__main__":


    dbSettings = load_database_config()

    concepts = load_concepts(dbSettings)
    store_lookup_table(concepts, "concept")

    customQuestions = get_custom_questions(dbSettings)

    update_custom_answers_train(customQuestions)

    generate_domain(dbSettings)

    generate_story()