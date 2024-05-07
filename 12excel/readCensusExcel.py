import openpyxl, pprint

print('opening workbook...')
wb = openpyxl.load_workbook('./12excel/censuspopdata.xlsx')
sheet = wb['Population by Census Tract']
county_data = {}

# TODO: county_dataに群の人口と地域数を格納する
print('reading row')
for row in range(2, sheet.max_row + 1):
    # スプレッドシートの1行に、ひとつの人口調査標準地域のデータがある
    state = sheet['B' + str(row)].value # 州の略称
    county = sheet['C' + str(row)].value # 群の名称
    pop = sheet['D' + str(row)].value # 人口
    # print(state, county, pop)

    # この州のキーが確実に存在するようにする
    county_data.setdefault(state, {})
    # この州のこの群のキーが確実に存在するようにする
    county_data[state].setdefault(county, {'tracts': 0, 'pop': 0})
    
    # 各行が人口調査標準地域を表すので、数を一つ増やす
    county_data[state][county]['tracts'] += 1
    # この人口調査標準地域の人口だけ群の人口を増やす
    county_data[state][county]['pop'] += int(pop)
        
# 新しいテキストファイルを開き、county_dataの内容を書き込む
print('writing result...')
result_file = open('./12excel/census2010.py', 'w')
result_file.write('all_data = ' + pprint.pformat(county_data))
result_file.close()
print('finished!')
# pprint.pprint(county_data)