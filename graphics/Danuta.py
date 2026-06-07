
def Danuta():
    user_input = input(': ')
    if user_input == 'Danuta':
        print("Who's calling?")
    elif user_input == 'It is me.':
        print('What..?')
    elif user_input == 'Will you go there?':
        print('Go where?')
        print('What?')
    elif user_input == 'Do you eat':
        print('WHAT THE HELL IS THIS?')
    elif user_input == "":
        print('...')

i = 0
while i <= 10:
    Danuta()
    i += 1
