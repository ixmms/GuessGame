import random

attemptsList = []


def ScoreDisplay():
  if not attemptsList:
      print('There is currently no high score, it\'s yours for the taking!')

  else:
      print(f'The current high score is {min(attemptsList)} attempts')


def startPlaying():
   attempts = 0
   rand_num = random.randint(1, 100)
   print('Welcome to the guessing game!')
   player_name = input('What\'s your name? ')
   playYes = input(f'Hello, {player_name}, would you like to play?'
       '(Enter Yes/No): ')

   if playYes.lower() != 'yes':
      print('Alright')
      exit()
   else:
       ScoreDisplay()

   while playYes.lower() == 'yes':
       try:
           guess = int(input('Pick a number between 1 and 100: '))
           if guess < 1 or guess > 100:
               raise ValueError('Please type a number between 1 and 100')

           attempts += 1
           attemptsList.append(attempts)

           if guess == rand_num:
               print('WOW!, You did it!')
               print(f'It took you {attempts} attempts')
               playYes = input(
                   'Would you like to play again? (Enter Yes/No): ')
               if playYes.lower() != 'yes':
                   print('Seems like you\'ve loved it! Have a good day!')
                   break
               else:
                   attempts = 0
                   rand_num = random.randint(1, 100)
                   ScoreDisplay()
                   continue
           else:
               if guess > rand_num:
                   print('It\'s lower')
               elif guess < rand_num:
                   print('It\'s higher')

       except ValueError as err:
           print('That\'s an invalid value. Try again!')
           print(err)


if __name__ == '__main__':
   startPlaying()
