def say_hi():
    print("Bonjour")
    print("Je suis l'assistant virtuel de Tangente Consulting")


def say_bye():
    print("Au revoir")


def ask_question():
    print("comment puis-je vous aider ?")


def ask_other_question():
    other_question = input("Une autre question? (Y/n) :")
    return other_question


def answer_response():
    print("Je ne comprends pas votre question")


def respond_to_the_question():
    response = input()
    return response


nombre_question = 0
running = True
while running:
    if nombre_question == 0:
        say_hi()
    ask_question()
    response = respond_to_the_question()
    answer_response()
    nombre_question += 1
    other_question = ask_other_question()
    if other_question == "Y":
        running = True
    else:
        say_bye()
        running = False


# robot dit bonjour et demande "comment puis-je vous aider ?"
# tu poses une question
# analyse de la question
# si le bot comprend la question, réponse en rapport
# sinon réponse "je ne comprends pas"
