def formatCCs(CCtocheck):

    today = date.today()
    today = int(today.strftime("%Y"))

    CCFormated = CCtocheck.replace('\n','')
    CCFormated = CCFormated.split('|')

    try:
        [int(CCFormated[0]),int(CCFormated[1]),int(CCFormated[2]),int(CCFormated[3])]
    except ValueError:
        return None
    else:
        if len(CCFormated[0]) < 15 or len(CCFormated[0]) >= 17:
            return None
        elif int(CCFormated[1]) < 1 or int(CCFormated[1]) > 12:
            return None
        elif int(CCFormated[2]) < today or int(CCFormated[2]) > today + 7:
            return None
        elif len(CCFormated[3]) != 3 and len(CCFormated[0]) == 16 or len(CCFormated[3]) != 4 and len(CCFormated[0]) == 15:
            return None
        else:
            return CCFormated

def cleanNone(CCtocheck):
    if CCtocheck == None:
        return False
    else:
        return True

def generateMail():
    limit = [7,8,9,10,11,12]
    mails = ['@gmail.com','@hotmail.com','@outlook.com']
    letters = string.ascii_lowercase
    email = ''.join(random.choice(letters) for i in range(random.choice(limit)))
    email = email+random.choice(mails)
    return email

def file(nombre):
		if ".txt" in nombre:
			file = open(nombre).readlines()
			file = [archivo.rstrip() for archivo in file]
			for lines in file:
				datos.append(lines)
			name.append(nombre)
		else:
			raise TypeError