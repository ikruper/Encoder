"""
Column Cypher Controller
By Ian Kruper

"""

import column_cypher
import reader_writer

print "Welcome to text encoder/decoder!"
while True:
    source_sel = raw_input("Do you wish to scan document(1) or enter manually(2)? ")
    if source_sel == '2':
        com_sel = '0'
        break
    elif source_sel != '1':
        print "Invalid selection, please choose again."
        continue
    com_sel = raw_input("Do you wish to encode(1) or decode(2)? ")
    if com_sel == '1' or com_sel == '2':
        break
    else:
        print "Invalid selection, please choose again."
        
        
        
        
if com_sel == '0':
    while True:
        text = raw_input("Enter text to encode/decode: ")
        if len(text) < 20:
            print "Text string must be at least 20 characters long. Please try again."
        else:
            break
    if text[-7:] == "xjjquxy":
        result = column_cypher.decrypter(text)
    else:
        result = column_cypher.encrypter(text)
    print result




if com_sel == '1':
    while True:
        try:
            doc = raw_input("Enter name of document: ")
            doc = reader_writer.reader(doc)
            encrypted = column_cypher.encrypter(doc) #Impose 20 character lower limit for size of documents
            break
        except IOError:
            print "No such file exists. Please enter a valid file."
        
    dest_doc = raw_input("Enter a name for destination document: ")
    new_doc = reader_writer.writer(dest_doc, encrypted)
    print "Document encoded successfully!"
    
    
    
    
if com_sel == '2':
    while True:
        try:
            doc = raw_input("Enter name of document: ")
            orig_doc = reader_writer.reader(doc)
            verify = orig_doc[-7:]
            assert verify == "xjjquxy"
            if orig_doc[-7:] == "xjjquxy":
                decrypted = column_cypher.decrypter(orig_doc)
                break
        except IOError:
            print "No such file exists. Please enter a valid file."
        except AssertionError:
            print "Selected file is not encoded. Please select an encoded file."
            
    dest_doc = raw_input("Enter a name for destination document: ")
    reader_writer.writer(dest_doc, decrypted)
    print "Document decoded successfully!"
    
                    
