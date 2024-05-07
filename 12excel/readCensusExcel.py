import openpyxl, pprint

print('opening workbook...')
wb = openpyxl.load('censuspopdata.xlsx')
sheet = wb['Population by Census Tract']
