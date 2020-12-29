import pyttsx3
import PyPDF2

book = open('short_story.pdf', 'rb')    #the name of the pdf file (must be in the same directory)
pdf_reader = PyPDF2.PdfFileReader(book)

num_of_pages = pdf_reader.numPages      #extract the number of pages in the PDF file

speaker = pyttsx3.init()                #initialize the speaker

speaker.setProperty('rate', 221)        #set the speaker's rate of speaking

voices = speaker.getProperty('voices')
speaker.setProperty('voice', voices[1].id)      #can choose from a variety of speaker voices available

for page_num in range(num_of_pages):
    page = pdf_reader.getPage(page_num) #extract a particular page
    text = page.extractText()           #extract the text through it
    speaker.say(text)                   #the speaker says the text that has been extracted
    speaker.runAndWait()
