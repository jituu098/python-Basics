import random

messages = ['It is certain',
    'It is decidedly so',
    'Yes definitely',
    'Reply hazytryagain',
    'Ask again later',
    'Concentrate and ask again',
    'My reply is no',
    'Outlook not so good',
    'Very doubtful']
## Here randomly select the message from the above list and display it 
## every time it will show random message 
# random.randint()  of the random module fuction choose the randomly
print(messages[random.randint(0, len(messages) -1)])