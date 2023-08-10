def chat():

    users=[ "hi","how are you","can you help me","your name",
    "how's your day going",
    "tell me something interesting",
    "what's your favorite color",
    "do you like to travel",
    "what's your favorite food",
    "can you recommend a good book",
    "what is the weather like today",
    "tell me a joke"]

    bot=["Hello!","iam fine you","yes tell","im jarvis",
    "It's been a good day so far, thanks!",
    "Sure! Did you know that honey never spoils?",
    "I'm just a bot, so I don't have favorite colors.",
    "I wish I could travel, but I'm here to assist you!",
    "I don't eat, but I've heard pizza is popular.",
    "Have you tried 'The Alchemist' by Paulo Coelho?",
    "I'm not sure about the weather. You can check online.",
    "Why don't scientists trust atoms? Because they make up everything!"]

    user_input=input('you:')

    user_input=user_input.lower()

    i=0
    for user in users:

        if user_input==user:

            print('bot:'+bot[i])

            return chat()

        i =i+1

chat()

