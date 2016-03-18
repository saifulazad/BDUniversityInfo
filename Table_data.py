"""
Module doc string
"""


def gettabledata(table):
    """

    :param table: A HTML table data <tr></tr>
    :type table: HTML
    :return general_info: dict
    """
    general_info = {}
    for row in table.findAll("tr"):
        cells = row.findAll("td")
        if len(cells) > 0:
            general_info[' '.join(cells[0].text.split())] =\
                                                        ' '.join(cells[2].text.split())

    return general_info