import re

def get_immigrant(tweet):
    regex = re.compile(r'immigr[a-zA-Z]*')
    regex_two = re.compile(r'illegals[a-zA-Z]*')
    regex_three=re.compile(r'foreignors[a-zA-Z]*')
    regex_four=re.compile(r'illegal border crosser[a-zA-Z]*')
    
    if regex.search(tweet) or regex_two.search(tweet) or regex_three.search(tweet) or regex_four.search(tweet):
        return True
    else:
        return False
def get_vet(tweet):
    regex = re.compile(r'vet[a-zA-Z]*')
    if regex.search(tweet):
        return True
    else:
        return False
    
def get_ukraine(tweet):
    regex = re.compile(r'ukrain[a-zA-Z]*')
    if regex.search(tweet):
        return True
    else:
        return False
    
    
def get_refugee(tweet):
    regex = re.compile(r'refug[a-zA-Z]*')
    if regex.search(tweet):
        return True
    else:
        return False
def get_asylum(tweet):
    regex = re.compile(r'asyl[a-zA-Z]*')
    if regex.search(tweet):
        return True
    else:
        return False

    
def get_homeless_vet(tweet):
    regex = re.compile(r'homeless vet[a-zA-Z]*')
    if regex.search(tweet):
        return True
    else:
        return False
    
# def get_homeless_people(tweet):
#     regex = re.compile(r'homeless people*')
#     if regex.search(tweet):
#         return True
#     else:
#         return False
    
def get_homeless_people(tweet):
    regex = re.compile(r'homeless people*')
    regex1 = re.compile(r'homeless person*')
    regex2 = re.compile(r'homeless ppl*')
    if regex.search(tweet) or regex1.search(tweet) or regex2.search(tweet):
        return True
    else:
        return False
    
def get_homeless_americans(tweet):
    regex = re.compile(r'homeless americans*')
    if regex.search(tweet):
        return True
    else:
        return False

def get_american_citizens(tweet):
    regex = re.compile(r'american citizens*')
    if regex.search(tweet):
        return True
    else:
        return False
    
    
def get_illegal_alien(tweet):
    regex = re.compile(r'illegal alien*')
    if regex.search(tweet):
        return True
    else:
        return False