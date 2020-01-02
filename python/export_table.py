import ezodf
from VAR import filepath

ezodf.config.set_table_expand_strategy('all')

# doc = ezodf.opendoc('/home/pi/Desktop/Associations.ods')
doc = ezodf.opendoc(filepath)

associations = doc.sheets['Feuille1']
semis = doc.sheets['Feuille2']

a_row_count = associations.nrows()
a_col_count = associations.ncols()

names = [associations[i,0].value for i in range(1, a_row_count)]

s_row_count = semis.nrows()
s_col_count = semis.ncols()

vegetables = {}
for row in range(1, a_row_count):
    name = ""
    for col in range(a_col_count):
        if col == 0:
            name = associations[row, col].value
            t = {'good': [], 'bad': []}
            vegetables[name] = t
            continue
        val = associations[row, col].value

        if val == 1.0:
            vegetables[name]['good'].append(associations[0,col].value)
        if val == 0.0:
            vegetables[name]['bad'].append(associations[0,col].value)


for row in range(1, s_row_count):
    name = ""
    for col in range(s_col_count):
        if col == 0:
            name = semis[row, col].value
            t = {'pleine terre': [], 'sous abris': []}
            vegetables[name]['semis'] = t
            continue
        val = semis[row, col].value

        if val is not None and 'SA' in val:
            vegetables[name]['semis']['sous abris'].append(semis[0, col].value)
        if val is not None and 'PT' in val:
            vegetables[name]['semis']['pleine terre'].append(semis[0,col].value)





print(vegetables)

#print(content[1,4].value)




ezodf.config.reset_table_expand_strategy()
