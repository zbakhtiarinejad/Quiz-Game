print('Wellcome to the quiz game...')


while True:
    playing = input('do you wanna play "type yes/y if you do, and type no if you dont?" ')
    user_input = playing.lower()
    if user_input == 'yes' or user_input == 'y':
        print('lets start the game!')
        break
    elif user_input == 'no':
        print('ok, maybe next time!')
        quit()  
    else:
        print('I didnt understand that')




score = 0

answer = input('what does CPU stand for? ')
if answer.lower() == 'central processing unit':
    print('correct!')
    score += 1
else:
    print('incorrect!\nThe correct answer is "central processing unit"')

answer = input('what does GPU stand for? ')
if answer.lower() == 'graphics processing unit':
    print('correct!')
    score += 1
else:
    print('incorrect!\nThe correct answer is "graphics processing unit"')

answer = input('what does RAM stand for? ')
if answer.lower() == 'random access memory':
    print('correct!')
    score += 1
else:
    print('incorrect!\nThe correct answer is "random access memory"')

answer = input('what does PSU stand for? ')
if answer.lower() == 'power supply unit':
    print('correct!')  
    score += 1 
else:   
    print('incorrect!\nThe correct answer is "power supply unit"')

print('your score is ' + str(score/4 * 100) + '%')
print(f'you got {score} questions correct out of 4')
