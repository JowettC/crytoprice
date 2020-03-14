import json
import xlsxwriter

workbook = xlsxwriter.Workbook('result.xlsx')
worksheet = workbook.add_worksheet()

expenses = (
    ['Rent', 1000],
    ['Gas',   100],
    ['Food',  300],
    ['Gym',    50],
)

row = 1
col = 0

# title
worksheet.write(0, 0, "Name")
worksheet.write(0, 1, "price")
worksheet.write(0, 2, "24hr change")
worksheet.write(0, 3, "volume")

with open('data.json') as json_file:
    data = json.load(json_file)
    for data in data['data']:
        worksheet.write(row, col, data['name'])
        worksheet.write(row, col+1, data['quote']['USD']['price'])
        worksheet.write(row, col+2, data['quote']['USD']['percent_change_24h'])
        worksheet.write(row, col+3, data['quote']['USD']['volume_24h'])
        row += 1
workbook.close()
