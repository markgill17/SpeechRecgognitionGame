#  Gesture Based User Interface Project Design Doc
#### By Mark Gill and Aaron Burns

## Original Idea
* Before the Conoravirus drastically altered the course of this project, our original idea was to create a gesture based boxing game in Unity similar to the old Nintendo game, Punchout. The hardware we had decided to use was a kinect. However due to the college being shut down and the ability to meet up and pass the hardware between us, as well as issues surrounding the hardware itself, We had to drop this project idea. We put a lot of thought into this idea but dues to the circumstances unable to create it. 

* The new project specification mentioned using speech recognition as a gesture instead of what we originaly planned and that is what we did. Originally the idea was to create the game in Unity. This would not have been a problem for out team. As one of us is a windows used and the other is a Linux user and Unity is supported by that version of Linux. However because the bases for our project specification changed from visual gestures with the kinect to speech. We were unable to think of a way to utilise our original idea with speech commands.

## A Speech Recognition Brain Training Game
### Introduction
* Due to our original idea for the project (a Kinect boxing game) no longer being compatible with the hardware we are using, we decided to come up with a new idea. We spent some time trying to think of an idea that would work with speech gestures. We contemplated a number of games such as *Snake* or *Pong*. However we could find no way of making these games using speech commands that would be intuitive in the case of *Pong*, or fun in the case of *Snake*. For this reason we racked our brains in order to come up with an idea that would work better for speech gestures. We needed to think of an idea that would be based on speech and not just some game where the gameplay options are adapted into speech gestures.

### Project Overview
* The game we decided to build was a Brain training game using **Word and Colour** association. The player will see the word of a colour in a certain colour, for example: the word green in the colour red. The player will then be prompted to speak either the colour of the word they see or the word itself.
* We decided to code the project using python for a number of reasons one for which is that we have become increasingly familiar with this language over the course of our final two years. Another reason for coding this project in python is because of the compact and easy to implement libraries make the project easy to implement quickly, We needed to consider ease of implementation and quick development because we needed to build a project from scratch and we couldn't salvage any of our original game. Finding these libraries was a god send for getting this project done.

### Purpose of the application
* The purpose of this project is a simple, easy to use brain training game. Brain training help the player exercise their brain by presenting them with quandries that require the player to stop and think for a second before giving an answer

### Gestures identified
* The gestures that are recognized for this game are speech commands. The speech commands are very simple, The user will only have to say either a name or a colour. The player will see a text on the screen. It will be in a certain colour and the test itself will also be the name of a colour. The user will see a prompt below the coloured text that will ask the player to seay the colour they see or the name of the colour the text is. The speech commands that are recognized by the player are colours *red, green and blue*. If the player answers correctly, i.e. they follow the instruction prompt correctly, they will be given an indication that they are correct. If they answer incorrectly they will be given an indication of that as well.

### Hardware used
* The Hardware used was obviously the speech recognition hardware built into a laptop. The software we used to access this hardware was from a built in python module called **SpeechRecognition** as well as some other modules (These are specified in the requirements.txt file). 

### How it was Built
* As mentioned above we used a python module in order to get the speech recognition to work. but how we coded the project can be elaborated upon. We stored the properties of the question text in tuples. This made the values easy to access throughout the program. We were able to access these properties and apply random values to the question text. All we had to do was import the random python module and call a method from it on the tuples with the values. As well as making it easy to generate questions text, storing the values in tulpes makes it easy to access for the conditional statementd in the program, such as checking if the player is correct or not.

* The question text is automatically generated at the start of each round of the game. Once that is done, the player must give an answer for the program to continue. To make sure the player don't speak to quickly and answer before the program is actually listening a time limit and a message telling the player to get ready is there. Once the program is ready, it will listen for the possbile answers, *red, green and blue* or the exit program options *quit, close or leave*. If the program detects anything else it will count as a false answer. It also throws an error if it fails to recognize the users input.

* The player's score will increase for each right answer they get. However if they get three incorrect they will lose them game. This is how the player gets into the fail state of the game. Both the score and the game over are implemented using simple recurring conditional statements and incremental counters.

* If the player gets to the fail state of the game

### Conclusion
* In conclusion we found this project to be extremly stressful due to the nesscessary changes due to the involving circumstances. However we feel that the sudden deadline and complete overhaul of the project encourged us to think carefully about what we were going to build, this made us consider exactly what needed to be done. We did not have time to develop something that may take to much time and result is a broken game. So we went with something simple and easy to deliver. It is regretable that we could not use our original idea as we were looking forward to building something in Unity that used a Kinect. But speech recognition proved to a be a much more realiable and implementable form of hardware. The limitations of speech operated game are made up for with the ease of developing one.

## References
[https://kivy.org/#home](https://kivy.org/#home)  
[https://pypi.org/project/PyAudio/](https://pypi.org/project/PyAudio/)  
[https://realpython.com/pygame-a-primer/](https://realpython.com/pygame-a-primer/)  
[https://pypi.org/project/pyfiglet/0.7/](https://pypi.org/project/pyfiglet/0.7/)  
