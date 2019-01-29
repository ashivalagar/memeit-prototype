# Meme Generator 

The program is a python chatbot, which takes in an image and makes it into a meme. The project was made for the Hackathon conducted in NUS, Hack&Roll 2018. 


## Brownie Memes

* Abhinav Narayana Balasubramaniam - 226
* Rajgopal Iyer - 246
* Vivek Adrakatti - 247
* Shiv Alagar TGH Ashok Kumar - 772


## Contesting for prize
Most useless but innovative hack


## Behind the scenes

### Making a database
* We used google vision API to get descriptions, emotions and text off of images.
* We created a database of descriptions, emotions and text by writing the data into an XLS file.
* We ran the above code on a dataset of 3000 memes.

### Selecting the most appropriate text required for each meme
* Our selection algorithm filtered out our text for the memes based on the following priority: 1. emotion 2. number of matching description tags 3. length of meme text .
* After our meme text got selected we wrote our text onto our photo.

### Front-end
* Our front end was made using a telegram bot api, based on picture input the code would output a meme.


## Prerequisites needed
Install the following python libraries using pip3
```
google-cloud
pillow
xlwt
wget
requests
pyTelegramBotAPI
```


## To run the code
* Create a project on google console.
* Enable google cloud vision API.
* Download the API key json file.
* Open the terminal/bash and run the following command
```
export GOOGLE_APPLICATION_CREDENTIALS="path/to/API/key.json"
```
* Create a telegram bot using bot father and replace the link used in the Bot_Trial.py with the one obtained by you.
* Open the command line and run the following to run the telegram bot.
* Send pictures and get the meme-ified.

```
python3 Bot_Trial.py
```


<!-- ## Memefied images

### Input
Pictures here
### Output
Memefied output -->
