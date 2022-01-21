# from re import I
import pyttsx3
import PyPDF2

from tkinter.filedialog import *

book = askopenfilename()
pdfreader = PyPDF2.PdfFileReader(book)
pages = pdfreader.numPages

for num in range(0, pages):
    page = pdfreader.getPage(num)
    text = page.extractText()
    player = pyttsx3.init()
    player.say(text)
    player.runAndWait()


# book = open('sample2.pdf', 'rb')
# pdfReader = PyPDF2.PdfFileReader(book)
# pages = pdfReader.numPages
# print(pages)

# speaker = pyttsx3.init()
# page = pdfReader.getPage(0)
# text = page.extractText()
# speaker.say(text)
# speaker.runAndWait()
 