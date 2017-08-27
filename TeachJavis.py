# Referenced 1 : http://meonggae.blogspot.kr/2016/08/nodejs-python-shell-python.html
# Referenced 2 : http://ngee.tistory.com/335
'''
This module is about teaching Word2Tag, Sentence2Tag, Tag2Tag, Tag2Word, Tag2Sentence... etc.
DB Schema is like below.
    wordSchemaCollection = Client[id]["wordSchema"]
    sentenceSchemaCollection = Client[id]["sentenceSchema"]
    ...
    signInSchemaCollection = client[masterID]["SignIn"]
'''

import pymongo as mogdb

def teachConversation(inputSentence, outputSentence, id):
    '''
    ARGS:

    RETURNS:

    RAISES:

    '''

def teachWord2Tag(word, wtag, id):
    '''
    ARGS:

    RETURNS:
    
    RAISES:

    '''

def teachTag2Word(wtag, word, id):
    '''
    ARGS:

    RETURNS:
    
    RAISES:
    
    '''

def teachSentence2Tag(sentence, stag, id):
    '''
    ARGS:

    RETURNS:
    
    RAISES:
    
    '''

def teachTag2Sentence(stag, sentence, id):
    '''
    ARGS:

    RETURNS:
    
    RAISES:
    
    '''

def teachTag2Tag(stag1, stag2, id):
    '''
    ARGS:

    RETURNS:
    
    RAISES:
    
    '''

def forgetConversation(inputSentence, outputSentence, id):
    '''
    ARGS:

    RETURNS:
    
    RAISES:
    
    '''

def forgetWord2Tag(word, wtag, id):
    '''
    ARGS:

    RETURNS:
    
    RAISES:
    
    '''

def forgetTag2Word(wtag, word, id):
    '''
    ARGS:

    RETURNS:
    
    RAISES:
    
    '''

def forgetSentence2Tag(sentence, stag, id):
    '''
    ARGS:

    RETURNS:
    
    RAISES:
    
    '''
def forgetTag2Sentence(stag, sentence, id):
    '''
    ARGS:

    RETURNS:
    
    RAISES:
    
    '''
def forgetTag2Tag(stag1, stag2, id):
    '''
    ARGS:

    RETURNS:
    
    RAISES:
    
    '''


def connectToMasterDB(to='localhost',port=27017):
    '''
    ARGS :
        to = where the db is located ip. Default is localhos, 127.0.0.1.
        port = where the db is located port. Default is 27017.
    RETURNS :
        databasePlace = where can find data.
    '''
    connection = mogdb.MongoClient(to, port)
    databasePlace = connection["master"]

    return databasePlace

def connectToNonMasterDB(id, to='localhost',port=27017):
    '''
    ARGS :
        to = where the db is located ip. Default is localhos, 127.0.0.1.
        port = where the db is located port. Default is 27017.
    RETURNS :
        databasePlace = where can find data.
    '''
    connection = mogdb.MongoClient(to, port)
    databasePlace = connection[id]

    return databasePlace
