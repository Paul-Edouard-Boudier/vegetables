"""
Set of functions that are about retrieving the data from the file '.ods'
"""
# ============================================================================
# Import
# ============================================================================
import ezodf


# ============================================================================
# Functions
# ============================================================================
def vegetables(filepath: str) -> dict:
    """
    """
    ezodf.config.set_table_expand_strategy('all')

    doc = ezodf.opendoc(filepath)
    associations_doc = doc.sheets['associations']
    semis_doc = doc.sheets['semis']

    vegetables = {}
    vegetables = associations(associations_doc, vegetables)
    vegetables = semis(semis_doc, vegetables)
    
    ezodf.config.reset_table_expand_strategy()
    
    return vegetables

def semis(sheet, vegetables: dict) -> dict:
    """
    """
    rows = sheet.nrows()
    cols = sheet.ncols()

    for row in range(1, rows):
        name = ""
        for col in range(cols):
            if col == 0:
                name = sheet[row,col].value
                t = {'pt': [], 'sa': []}
                vegetables[name]['semis'] = t
                continue
            val = sheet[row, col].value

            if val is not None and 'SA' in val:
                vegetables[name]['semis']['sa'].append(sheet[0,col].value)
            if val is not None and 'PT' in val:
                vegetables[name]['semis']['pt'].append(sheet[0,col].value)
    return vegetables


def associations(sheet, vegetables: dict) -> dict:
    """
    """
    rows = sheet.nrows()
    cols = sheet.ncols()

    for row in range(1, rows):
        name = ""
        for col in range(cols):
            if col == 0:
                name = sheet[row, col].value
                t = {'good': [], 'bad': []}
                vegetables[name] = t
                continue
            
            val = sheet[row, col].value

            if val == 1.0:
                vegetables[name]['good'].append(sheet[0,col].value)
            if val == 0.0:
                vegetables[name]['bad'].append(sheet[0,col].value)

    return vegetables


def print_carac(v: str, vegetables: dict) -> str:
    """
    """
    msg = "Va bien avec : "
    for good in vegetables[v]['good']:
        msg+= "\n    "+good

    msg += "\n\nVa pas bien avec : "
    for bad in vegetables[v]['bad']:
        msg += "\n    "+bad

    msg += "\n\nSe plante comme suit : "
    msg += "\n    Sous abris lors des mois de => "
    for sa in vegetables[v]['semis']['sa']:
        msg += "\n        "+sa

    msg += "\n    En pleine terre lors des mois de => "
    for pt in vegetables[v]['semis']['pt']:
        msg += "\n        "+pt

    return msg
