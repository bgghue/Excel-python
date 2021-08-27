import xlwings as xw
#引入函数
#测试
app = xw.App(visible=True,add_book=False)
wb = app.books.add()
sht = xw.sheets["sheet1"]
sht.range("A1").value = "ycb"
wb.save("测试表.xlsx")
wb.close
app.quit