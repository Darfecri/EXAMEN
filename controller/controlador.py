import xlwings as xw
import numpy as np

from EXAMEN.model.funciones import caudal

def main():
    wb = xw.Book.caller()
    sheet = wb.sheets[0]
    col1= "colum1"
    col2= "colum2"
    col3= "colum3"
    col4= "colum4"
    col5= "colum5"
    res1= "capa1"
    res2= "capa2"
    res3= "capa3"
    res4= "capa4"
    res5= "capa5"

    params= sheet(col1).options(np.array, transpose=True).value
    sheet(res1).value= caudal(*params)
    params2 = sheet(col2).options(np.array, transpose=True).value
    sheet(res2).value = caudal(*params2)
    params3 = sheet(col3).options(np.array, transpose=True).value
    sheet(res3).value = caudal(*params3)
    params4 = sheet(col4).options(np.array, transpose=True).value
    sheet(res4).value = caudal(*params4)
    params5 = sheet(col5).options(np.array, transpose=True).value
    sheet(res5).value = caudal(*params5)


@xw.func
def hello(name):
    return f"Hello {name}!"


if __name__ == "__main__":
    xw.Book("examen.xlsm").set_mock_caller()
    main()
