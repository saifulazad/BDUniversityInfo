"""
This class Mainpulate data from HTML
"""
class BasicInfo(object):
    """
    This class Mainpulate data from HTML
    """
    def __init__(self):
        self.basic_info = None
        self.eduiconURL = None
        self.universityURL = None
        self.imageURL = None

    def getBasicInfo(self, row):
        """

        :param row: Take HTML row content
        :type row: HTML content
        :return None:

        """
        head = row.text

        try:
            self.imageURL = row.findAll('img')[0].attrs['src']

        except:
            self.imageURL = None
            return

        allURl = row.findAll('a')

        if len(allURl) > 2:

            self.eduiconURL = allURl[0].attrs['href']
            self.universityURL = allURl[2].attrs['href']

        elif len(allURl) == 2:
            self.eduiconURL = allURl[0].attrs['href']
            self.universityURL = allURl[1].attrs['href']

        self.basic_info = ' '.join(head.split()).split("Phone")[0]

