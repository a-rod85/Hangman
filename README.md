
# HangMan the game

![Skärmbild (29)](https://user-images.githubusercontent.com/102023928/180077016-2bdcbd6c-abd4-45b8-8618-66ff6f8d39bc.png)



##  Aim Of The Site

This site is for users who wish enjoy and test themselves in hangman.
In this game there are 60 words from which will be generated randomly.
The player has 6 guesses to beat getting hangman anf in which the 
gam will be over.




Deployed site can be seen on the link below 
https://hangman2-the-game.herokuapp.com/
##  Games Features

SCREEN TITLE.

![Skärmbild (24)](https://user-images.githubusercontent.com/102023928/180073361-5814d5b4-0dac-4450-95b9-fb9d37a6adb0.png)



The User/ Player is welcomed to the game.
The rules are explained, were after they are asked to enter
in their name.


ENTER NAME AND WOULD YOU LIKE TO PLAY OPTION.

![Skärmbild (20)](https://user-images.githubusercontent.com/102023928/180073824-37078696-35d1-4625-8a05-f59741ada266.png)




Upon entering thier name the player is given the option to
play by either pressying Y = yes or N = no


GAME PLAY

![Skärmbild (27)](https://user-images.githubusercontent.com/102023928/180074006-f2489c71-7c1c-4aa8-8420-891a384109d6.png)



The number of blank spaces shows the user/Player how many
letters are in the word in the word they need to get correct.
They will also be able to see the number of guesses 
which they have left in the game.


INCORRECT GUESS.


![Skärmbild (28)](https://user-images.githubusercontent.com/102023928/180074903-9df0e036-8616-4e0c-9d66-81c34809e297.png)



If the User/Player guesses incorrect the letter will
be shown on the on the screen. This enables them
not to guess the same letter again.(we hope)


CORRECT GUESS


If the letter chosen by the User/Player is in the secret word 
the letter will be replace the designated space. All guessed letters are also displayed for the player to be able to keep track.
The number of turns are not decreased since the guess was correct.


INVALID GUESS


![Skärmbild (21)](https://user-images.githubusercontent.com/102023928/180074763-f6e172b2-a395-44b1-b052-e9625431e367.png)



If the letter chosen by the User/Player is incorrect the number of turns will 
decrease by one and the visual will change showing that the hanging is approaching!! 
The incorrect letter is added to the list of guessed letters.

YOU WIN


![Skärmbild (26)](https://user-images.githubusercontent.com/102023928/180073601-4f107499-3329-4ab2-a1f6-7a554618233c.png)

If the User/Player manages to guess the correct word they win and therefore does not need to hang! They also get to choose whether or not they wish to play again

YOU LOSE


![Skärmbild (22)](https://user-images.githubusercontent.com/102023928/180074564-00c75c92-6dce-4f6c-ae46-55faca5e9d26.png)

The secret word is revealed therefore the player is hung. The player is asked if they wish to play again. 
If so, they do not need to enter name again but the game just runs from the start.



## Tech Stack

This project was created using Python. 
Any other technologies which are present, 
such as JavaScript, are part of the Code Institue template used to create this project.

## Deployment

The page was deployed using Heroku. The procedure to do this was:

1.  Use GitHub to build project.
2.  Push built project code to GitHub.
3.  Navigate to Heroku
4.  Signup and Login to the site.
5.  Select create a new app, select a unique name and region.
6.  Select Buildpack, select Python and save.
7.  Select Buildpacks again and select Nodejs save.
8.  Ensure order of Buildpacks is Python then Nodejs.
9.  Navigate to the deploy tab, choose GitHub as deployment method and connect to you GitHub account.
10. Enter your repository and connect.
11. Select either automatic deploys which automatically deploys whenever you push to GitHub, or manual deploys to deploy manually.

## Testing

The game has been deployed using Heroku and runs in a command line Python Terminal. 
I've tested the site using Chrome, Edge and Firefox browser to make sure it runs as expected.
Below you will see how I tested:





Enter Username

Expected Outcomes: 

When entering the game the player is asked to enter their name. A valid name contains only letters and is required for the player to continue.

Test: 

I tried entering names using letters, numbers, other signs and not entering anything at all.

Result: 

If entering a name and pressing enter the game would run and the name would display as intented. However if anything else was entered, number, signs or even left blank, the player could continue without a name by pressing enter.

Verdict: 

This test failed at this stage since the player was not forced to enter a valid name.

Solution: 

To resolve this issue, I added a "while True" statement, ensuring that game will not run without valid username.

Play or not

Expected Outcomes: 

The player is asked if they want to play, player is supposed to answer by entering either Y, for yes, or N, for no. Any other inputs are expected to return an error message and request the player to choose

Test: 

I tried the correct inputs (Y and N) as well as incorrect inputs, digits, blanks, other signs and letters.

Result: 

Correct inputs progressed the code correctly and incorrect inputs displayed a message prompting the player for the right input.

Verdict: 

Code functioned as intented and did not break at any stage.

The Secret Word

Expected Outcomes:

To run the game, the computer is supposed to select a random word from the words.py file.

Test:

To ensure function was working as intended I made sure that different words were displayed each time a new game started.

Result:

Since some words contains blanks or hyphens, I created a while loop to get the computer to choose another word if that was the case. New words got selected as intended but it was difficult to see how many letters the secret word contained since the underscores representing each letter was all in one line.

Verdict: 

The random word function worked as intented but the display of the secret word needed improvement.

Solution: 

To make it clear how many letters the secret word contains I added blanks between each underscore: " _ ".

Test 2: Ran game again to get computer to choose random word.

Result 2: The blanks make it easy to see how many letters are in the secret word.

Verdict 2: The secret word function runs as intented, presenting new random words, without blanks or hyphens, and the number of letters are also clearly displayed.

Correct Letter

Expected Outcomes: 

Once the game is running, the player is presented with the secret word to guess. From start the player can see how many letters are in the secret word. If the guessed letter is in the secret word, the underscore in the word is supposed to be replaced by the correct letter. Each valid guess is to be displayed in a guessed letters list.

Test: 

Correct inputs; letters, and incorrect inputs; digits, blanks, other signs, were entered to test this function.

Result: 

Correct guesses reveal the letter in the secret word and is also added in the guessed letters list.

Verdict: 

The correct letter guesses work as intended.

Wrong Letter

Expected Outcomes: 

If the guessed letter is not in the word, the player is encouraged to make another guess, if there are still turns to go. The guessed letter is supposed to show in the guessed letters list and hanging stage display change, showing the player that they are one step closer to being hung.

Test:

Correct inputs; letters, and incorrect inputs; digits, blanks, other signs, were entered to test this function.

Result: 

Wrong guesses are added in the guessed letters list, numbers of turns are decreasing and the display for hanging stage changes.

Verdict: The wrong letter guesses work as intended.

Invalid Guess

Expected Outcomes:

If the player inputs an invalid guess, i.e digits, blanks, other signs or a letter that has already been guessed, an error is supposed to be shown, encouraging the player to make another guess.

Test: 

Correct inputs; letters, and incorrect inputs; digits, blanks, other signs, were entered to test this function.

Result: 

If an invalid guess was entered an error is shown and the player is asked to choose one letter. As intented the number of turns reamain the same.

Verdict: 

The invalid guess works as intended.

Player Loses

Expected Outcomes: 

If the player makes 6 valid guesses and still not manages to guess the secret word, the player loses. The visual of the player being hung is displayed. The secret word is revealed and the player is asked if they want to play again.

Test:

Unsuccessful attempts by the player at guessing the secret word were made.

Result: 

A message telling the player they lost appears, the hanging man is displayed and the secret word is revealed. The player is not asked if they wish to play again or not.

Verdict: 

The player loses function doesn't work as intented since the player is not asked if they want to play again.

Solution: 

Add the run_game function to the if turns == 0 statement in the play_game function.


Player wins

Expected Outcomes: 

If the player manages to guess the secret word using no more than 6 guesses, the player wins! The secret word is displayed and the player is asked if they want to play again. they do so by entering Y or N.

Test: 

Successful attempts at guessing the secret word were made.

Result: 

A message telling the player they won apperars, and the secret word is displayed. The player is not asked if they wish to play again or not.

Verdict: 

The player loses function doesn't work as intented since the player is not asked if they want to play again.

Solution: 

Add the run_game function to the else statement in the play_game function.


## Validation:


![Skärmbild (31)](https://user-images.githubusercontent.com/102023928/180496360-6c5ba1d9-24dd-46a2-907d-df0053ee01a2.png)


The python code was run through Pep8 Online to check to make sure there are no errors in the code.


## Credits

I done my upmost to deviate from code as much as possible they maybe similarities within the code. 
The ispiration visuals was used from (https://www.youtube.com/watch?v=m4nEnsavl6w&t=3s).
The random words was generated from (https://wordcounter.net/random-word-generator).

GRATITUDE

Thank you Harry for the pep talk,not to over think 
and for reminding me keep it simple!!
