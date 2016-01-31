__author__ = 'azad'

def getTableData(table):


    general_info = {}
    for row in table.findAll("tr"):
        cells = row.findAll("td")
        if (len(cells)>0):
           general_info[' '.join(cells[0].text.split())] = ' '.join(cells[2].text.split())

    return general_info