import xlwt

# Write data to excel example.
def write_excel(file_name):
    wb = xlwt.Workbook(file_name)
    sheet1 = wb.add_sheet('Sheet1')
    # write to p(0,1) in excel.
    sheet1.row(0).write(1, "test")
    wb.save(file_name)
    
