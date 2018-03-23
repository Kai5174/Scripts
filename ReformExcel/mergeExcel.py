from xlrd import open_workbook
import xlsxwriter
import glob

def decide(sheet):
    dist = {
        'RMA number': '', # done
        'Sub distributor': '',# done
        'Invoice': '',# done
        'Model': '',# done
        'Tel': '',
        'Serial': '',# done
        'Fault describe': '',# done
        'Replaced model': '',
        'Test result': '',# done
        'RMA return date': '', # need manually
        'Return C/N': '', # need manually
    }
    len_row = len(sheet)
    len_col = len(sheet[1])

    # Find RMA
    for row_index in range(len_row):
        if 'Return Authrization Number' in sheet[row_index]:
            col_index = sheet[row_index].index('Return Authrization Number')
            dist['RMA number'] = _get_once_bottom(sheet, row_index, col_index)
            break

    for row_index in range(len_row):
        if 'Customer' in sheet[row_index]:
            col_index = sheet[row_index].index('Customer')
            dist['Sub distributor'] = _find_around(sheet, row_index, col_index)
            break

    for row_index in range(len_row):
        if 'Invoice No.' in sheet[row_index]:
            col_index = sheet[row_index].index('Invoice No.')
            dist['Invoice'] = _find_to_bottom(sheet, row_index, col_index)
            break

    for row_index in range(len_row):
        if 'Description' in sheet[row_index]:
            col_index = sheet[row_index].index('Description')
            dist['Model'] = _find_to_bottom(sheet, row_index, col_index)
            break

    for row_index in range(len_row):
        if 'Serial No.' in sheet[row_index]:
            col_index = sheet[row_index].index('Serial No.')
            dist['Serial'] = _find_to_bottom(sheet, row_index, col_index)
            break

    for row_index in range(len_row):
        if 'Test result' in sheet[row_index]:
            col_index = sheet[row_index].index('Test result')
            dist['Fault describe'] = _find_to_bottom(sheet, row_index, col_index)
            break

    for row_index in range(len_row):
        if 'Replacement S/N' in sheet[row_index]:
            col_index = sheet[row_index].index('Replacement S/N')
            dist['Test result'] = _find_to_bottom(sheet, row_index, col_index)
            break

    for row_index in range(len_row):
        for col_index in range(len_col):
            if sheet[row_index][col_index].find('TEL:') != -1:
                dist['Tel'] = _combine_itself_and_bottom(sheet, row_index, col_index)
                break

    return dist


def _combine_itself_and_bottom(sheet, row_index, col_index):
    data = []
    data.append(sheet[row_index][col_index])
    data.append(sheet[row_index+1][col_index])
    return ''.join(data)


def _get_once_bottom(sheet, row_index, col_index):
    maximum = len(sheet)
    row_index += 1
    data = ''
    while row_index < maximum:
        if sheet[row_index][col_index] != '':
            data = sheet[row_index][col_index]
            break
        row_index += 1
    return data


def _find_around(sheet, row_index, col_index):
    data = ''
    if sheet[row_index][col_index+1] != '':
        data = sheet[row_index][col_index+1]
    elif sheet[row_index+1][col_index] != '':
        data = sheet[row_index+1][col_index]
    elif sheet[row_index+1][col_index+1] != '':
        data = sheet[row_index+1][col_index+1]
    return data


def _find_to_bottom(sheet, row_index, col_index):
    maximum = len(sheet)
    row_index += 1
    data = []
    while row_index < maximum:
        if sheet[row_index][col_index] != '' and sheet[row_index][col_index] != 'Return Date':
            data.append(str(sheet[row_index][col_index]))
        row_index += 1
    return ''.join(data)


def read_and_messsage(wb):

    record = []
    for s in wb.sheets():
        tmp = []
        for row in range(s.nrows):
            values = []
            for col in range(s.ncols):
                values.append(str(s.cell(row, col).value))
            tmp.append(values)
        record.append(tmp)
    return record


if __name__ == '__main__':
    file_lists = glob.glob("input/*.xls")
    row_num = -1
    dec = []

    for name in file_lists:
        row_num += 1
        print(row_num)
        wb = open_workbook(name)
        result = read_and_messsage(wb)
        for tmp in result:
            dec.append(decide(tmp))

    outbook = xlsxwriter.Workbook('output/merged.xlsx')
    outbook_sheet = outbook.add_worksheet()
    row_num = -1
    for data in dec:
        row_num += 1
        output_order = ['RMA number', 'Sub distributor', 'Invoice', 'Model', 'Tel', 'Serial',
                        'Fault describe', 'Replaced model', 'Test result', 'RMA return date', 'Return C/N']

        for values in data:
            col = output_order.index(values)
            outbook_sheet.write_string(row_num, col, str(data[values]))

    outbook.close()


