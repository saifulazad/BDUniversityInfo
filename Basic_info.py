__author__ = 'azad'

class BasicInfo:



    def __init__(self):
        self.basic_info  = None
        self.eduiconURL = None
        self.universityURL = None
        self.imageURL =None


    def getBasicInfo(self ,row):

        head =  row.text

        try :
            self.imageURL=  row.findAll('img')[0].attrs['src']

        except:
            self.imageURL=None
            return

        allURl = row.findAll('a')

        if len(allURl)>2:
            self.eduiconURL = allURl[0].attrs['href']
            self.universityURL = allURl[2].attrs['href']
        elif len(allURl)==2:
            self.eduiconURL = allURl[0].attrs['href']
            self.universityURL = allURl[1].attrs['href']

        print  ' '.join(head.split()).split("Phone")
        self.basic_info = ' '.join(head.split()).split("Phone")[0]

