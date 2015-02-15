"""
Document Reader/Writer
By Ian Kruper

"""

from docx import Document

def reader(doc): #Accepts document name, return string of text from document
    try:
        if doc[-3:] == "txt":
            doc = open(doc, 'r')
            text = doc.read()
            doc.close()
            return text
        if doc[-4:] == "docx":
            word_doc = Document(doc)
            text = ""
            for p in word_doc.paragraphs:
                text += p.text
                text += '\n'
            return text[0:-1]
    except IOError:
        raise IOError
        

def writer(doc, text): #Accepts document name and text to write, returns nothing
    try:
        if doc[-3:] == "txt":
            open(doc, 'w')
            doc.write(text)
            doc.close()
        if doc[-4:] == "docx":
            dest_doc = Document()
            dest_doc.add_paragraph(text)
            dest_doc.save(doc)
    except IOError:
        raise IOError