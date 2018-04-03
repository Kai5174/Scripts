import csv
import pyperclip

rfile = open('../table.csv', 'r')
reader = csv.reader(rfile)

col_row = input('input row and col info (e.g. an 3x4 table, input 3 4): ')
col_row = col_row.split(' ')

if len(col_row) != 2:
    print("invalid input")
    exit()

row = int(col_row[0])
col = int(col_row[1])

template = ''
template += '\\begin{table}[!ht]\n' \
            '\\centering\n' \
            '\\rowcolors{2}{lightgray}{white}\n' \
            '\\resizebox{\columnwidth}{!}{%\n'

template += '\\begin{tabular}{'+col*'c'+'}\n'
col_counter = 0
for reader_row in reader:
    col_counter += 1
    if col_counter == 1:
        template += '\\toprule\n'
    if col_counter == 2:
        template += '\\midrule\n'
    if col_counter == row+1:
        template += '\\bottomrule\n'
    if col_counter > row:
        break
    for ii in range(col):
        if ii == col - 1:
            template += reader_row[ii]+'\\\\ \n'
        else:
            template += reader_row[ii]+'&'

template += '\\end{tabular}\n' \
            '}\n' \
            '\\end{table}'
print(template)
pyperclip.copy(template)

rfile.close()
