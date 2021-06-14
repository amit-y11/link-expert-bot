# <h1 align=center>Link Expert Bot</h1>

<p align=center><img src="images/linkbot.png" alt="logo" width="250px" height="250px"/></p>

<h3 align=center>A telegram bot for shortening and unshortening links</h3>



## About

Bot can short your long url and get bit.ly link or unshort various short url like bit.ly, adf.ly, tinyurl, adfoc.us, sh.st, and many more

Start chat with this bot on [telegram](https://telegram.me/link_expertBot)


## Requirements

* Bot token from [Bot Father](https://t.me/BotFather), If you don't know how to get bot token, read [this](https://core.telegram.org/bots#6-botfather)

* bit.ly api key, get your api key from [here](https://bitly.is/accesstoken/)

---
## Installation 

#### You can fork the repo and deploy it on Heroku :)  

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

OR

* Clone this repository using
```sh
$ git clone https://github.com/amit-y11/link-expert-bot
```
* Enter the directory and install all the requirements using
```sh
$ pip3 install -r requirements.txt
```
* Edit line 14 and paste your plantnet.org api key
```sh
14        Api_key = "Your bit.ly api key"
```
* Edit line 80 and paste your Bot token
```sh
80       token="Your Bot Token"
```
#### Run Your Bot using the following command :
```sh
$  python3 bot.py
```
## License

```
MIT License

Copyright (c) 2020 amit-y11

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

```