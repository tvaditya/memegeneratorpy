# memegenerator.py

This is a random meme generator web app that uses Flask as a framework and covers some intermediate knowledge in Python.
This README file will provide you with all you need to run this in you local python environment.

## Installation
Clone the repo https://github.com/tvaditya/memegeneratorpy , when done enter in the root directory and be sure you have Pyton 3.8 installed.
when in the root directory , you will find the a file called requirements.txt , read the paragrpah below and follow the instructions so you can replicate the environment I used.


The requirements file has been provided with all you need, please be sure you are using Python 3.8.x.

On the root dir you will see a requirements file, execute it as says below.
```bash
pip install -r requirements.txt
```
Also install "pdftotext" you can find it in https://www.xpdfreader.com/download.html

## Running the app

If you have followed the step above correctly you will see a file named app.py, that is our main program and t should be the file you must execute
Just execute your python app on your terminal as says below:

```bash
python app.py
```
(This was developed under Ubuntu 20.04)

Once it is run you will see this:
```bash
* Serving Flask app "app" (lazy loading)
* Environment: production
  WARNING: This is a development server. Do not use it in a production deployment.
  Use a production WSGI server instead.
* Debug mode: off
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```
You can just access the http address above http://127.0.0.1:5000/ on your browser.
Once that is done you will see the meme being generated, if you press RANDOM a new Meme will be generated if you press CREATE 
you can upload your own images.

## A description of the modules

### quote_engine

The quote_engine module is responsible for ingesting many types of files that contain quotes. For our purposes, a quote contains a body and an author:
```bash
"This is a quote body" - Author
```
This module will is composed of many classes and will demonstrate your understanding of complex inheritance, abstract classes, classmethods, strategy objects and other fundamental programming principles.

You can also use the parse method within ingestor to add files via CLI ( Check the main method).

### meme_generator
The Meme Engine Module is responsible for manipulating and drawing text onto images. It will reinforce your understanding of object-oriented thinking while demonstrating your skill using a more advanced third party library for image manipulation.

### quote_models
Just encapsulates the body and the author models.
