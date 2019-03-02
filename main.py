from rasa_nlu.model import Interpreter
import json
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
import time



def format_agent_message(message):
    if(len(message) > 0):
        return message[0]["text"]
    else:
        return "Desculpa, não entendi..."

def main():
    interpreter = RasaNLUInterpreter('models/current/glosa')
    print("Bem-vindo ao Glosa")
    agent = Agent.load('models/dialogue', interpreter=interpreter)

    interpreter2 = Interpreter.load("models/current/glosa")




    while True:
        time.sleep(0.3)
        print("Tu: ", end=" ")
        message = input()
        if message == 'sair':
            break
        response = agent.handle_text(message)
        result = interpreter2.parse(message)
        print(json.dumps(result, indent=2))

        print("Glosa: ", end=" ")
        print(format_agent_message(response))




if __name__ == "__main__":
    main()



# python -m rasa_core.run -d models/dialogue -u models/current/glosa --port 5002 --credentials config/credentials.yml