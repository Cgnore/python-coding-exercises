print("Welcome to the Witcher universe, You are a Witcher!")

direction = input('''
You're at a cross road. Where do you want to go?
    Type  "left" or "right"
''')
if direction == "left" or direction ==  "Left" or direction == "LEFT":
    tavern = input('''
    You reached at the tavern. Some bandits tried to fight with you and swore to tou, what will you do?
        Type  "calm" or "fight"
''')
    if tavern == "Calm" or tavern == "calm" or tavern == "CALM":
        print("You stay calmed. They split to your face. But you ended up with your drink and took a really good bath")
    elif tavern == "fight" or tavern == "Fight" or tavern == "FIGHT":
        print("You started to fight. People around you are became frightened. You asked for the beer, no one answered. You turned to your path with a bad mood.")
    else:
        print("You typed wrong. Please try again later...")
elif direction == "right" or direction == "Right" or direction == "RIGHT":
    sword = input('''
    You saw an ormnivore... and decided to kill. You will swing your sword. Which way will you swing?
        Type  "left", "right", "up" or "down"
''')
    if sword == "left" or sword == "Left" or sword == "LEFT":
        print("You killed the ormnivore. Take the beast's head as a reward. Turned to your path...")
    elif sword == "up" or sword == "Up" or sword == "UP":
        print("You missed the beast. He caught you on your neck. You died and became a meal for the ormnivore...")
    elif sword == "down" or sword == "Down" or sword == "DOWN":
        print("You woke up. Understood that it was a really bad dream. Kissed Yeneffer on her neck...")
    elif sword == sword == "right" or sword == "Right" or sword == "RIGHT":
        print("You missed the beast. Take he caught you on your leg. With a few scratches, you decided to escape...")
    else:
        print("You typed wrong. Please try again later...")
else:
    print("You typed wrong. Please try again later...")
