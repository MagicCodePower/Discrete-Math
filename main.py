from PyQt5 import QtWidgets
import sys
import textwrap
import lab1
import window_a, window_b, window_c, window_d, window_f

class lab_one(QtWidgets.QMainWindow, lab1.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.variant()
        self.A = self.lineEdit.text()
        self.B = self.lineEdit_2.text()
        self.pushButton.clicked.connect(lambda: self.read_array(self.lineEdit))
        self.pushButton_2.clicked.connect(lambda: self.read_array(self.lineEdit_2))
        self.pushButton_8.clicked.connect(lambda: self.dubl_array(self.lineEdit,self.a,50))
        self.pushButton_9.clicked.connect(lambda: self.dubl_array(self.lineEdit_2,self.b,50))


        self.pushButton_3.clicked.connect(self.A_wind)
        self.pushButton_4.clicked.connect(self.B_wind)
        self.pushButton_5.clicked.connect(self.C_wind)
        self.pushButton_6.clicked.connect(self.D_wind)
        self.pushButton_7.clicked.connect(self.F_wind)

    def variant(self):
        varr = str(list(filter(lambda i: i % 3 == 0,range(0,1025))))

        wrapper = textwrap.TextWrapper(width=155)
        word_list = wrapper.wrap(text=varr)
        res = '\n'.join(word_list)
        self.y = '{' + res.strip('[]') + '}'
        self.label_6.setText(self.y)

    def read_array(self, where):
        f_name = QtWidgets.QFileDialog.getOpenFileName(self, "Open file", '/home')[0]
        f = open(f_name,'r')
        with f:
            data = f.read()
            where.setText(data)

    def dubl_array(self,fromm,where, width):
        wrapper = textwrap.TextWrapper(width=width)
        word_list = wrapper.wrap(text=fromm.text())
        res = '\n'.join(word_list)
        copyy = res
        # self.A = self.lineEdit.text

        if where == self.a:
            if len(fromm.text().split()) == len(set(fromm.text().split())):
                where.setStyleSheet('color: black;')
                where.setText('A: {{{}}}'.format(copyy))
                self.A = fromm.text()
            else:

                where.setStyleSheet('color: red;')
                where.setText("Enter set without duplicate!")


        else:
            if len(fromm.text().split()) == len(set(fromm.text().split())):
                where.setStyleSheet('color: black;')
                where.setText('B: {{{}}}'.format(copyy))
                self.B = fromm.text()
            else:
                where.setStyleSheet('color: red;')
                where.setText("Enter set without duplicate!")

    def A_wind(self):
        self.windowA = A_window(self.y,self.A)
        self.windowA.show()
    def B_wind(self):
        self.windowB = B_window(self.A, self.B)
        self.windowB.show()
    def C_wind(self):
        self.windowC = C_window(self.A, self.B)
        self.windowC.show()
    def D_wind(self):
        self.windowD = D_window(self.A, self.B)
        self.windowD.show()
    def F_wind(self):
        self.windowF = F_window(self.A, self.B)
        self.windowF.show()

class A_window(QtWidgets.QMainWindow, window_a.Ui_MainWindow):
    def __init__(self,y, A):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.close)

        self.A = A
        self.y = y
        self.label_3.setText('Y: {}'.format(self.y))
        cc = ''.join(self.c_res())

        if (len(A.split()) != 0):
            self.label_4.setStyleSheet('color: black;')
            self.label_4.setText('R: {{{}}}'.format(cc))
        else:
            self.label_4.setStyleSheet('color: red;')
            self.label_4.setText('Enter at least something into the set a')


    def c_res(self):
        self.c = []
        for elem in self.y.strip('{}').split(','):
            if elem not in self.A:
                self.c.append(elem)
        return self.c

class B_window(QtWidgets.QMainWindow, window_b.Ui_MainWindow):
    def __init__(self,A,B):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.close)
        if (len(A.split()) != 0) and (len(B.split()) != 0):
            self.label_6.setText('')
            self.label_3.setText('C: {{{}}}'.format(self.c_res(A,B)))
        else:
            self.label_6.setStyleSheet('color: red;')
            self.label_6.setText('Enter at least something into the set a and b')

    def c_res(self,A,B):
        C =[]
        for elem in A.split():
            if elem not in B.split():
                C.append(elem)
        C =  B.split() + C
        return ' '.join(C)

class C_window(QtWidgets.QMainWindow, window_c.Ui_MainWindow):
    def __init__(self,A,B):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.close)
        if (len(A.split()) != 0) and (len(B.split()) != 0):
            self.label_6.setText('')
            self.label_3.setText('C: {{{}}}'.format(self.c_res(A, B)))
        else:
            self.label_6.setStyleSheet('color: red;')
            self.label_6.setText('Enter at least something into the set a and b')


    def c_res(self,A,B):
        C = []
        for elem in A.split():
            if elem in B.split():
                C.append(elem)
        return ' '.join(C)

class D_window(QtWidgets.QMainWindow, window_d.Ui_MainWindow):
    def __init__(self,A,B):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.close)
        if (len(A.split()) != 0) and (len(B.split()) != 0):
            self.label_6.setText('')
            self.label_3.setText('C: {{{}}}'.format(self.c_res(A, B)))
        else:
            self.label_6.setStyleSheet('color: red;')
            self.label_6.setText('Enter at least something into the set a and b')

    def c_res(self,A,B):
        C = []
        for elem in A.split():
            if elem not in B.split():
                C.append(elem)
        return ' '.join(C)

class F_window(QtWidgets.QMainWindow, window_f.Ui_MainWindow):
    def __init__(self,A,B):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.close)
        if (len(A.split()) != 0) and (len(B.split()) != 0):
            self.label_6.setText('')
            self.label_3.setText('C: {{{}}}'.format(self.c_res(A, B)))
        else:
            self.label_6.setStyleSheet('color: red;')
            self.label_6.setText('Enter at least something into the set a and b')

    def c_res(self,A,B):
        C = []
        for elem in A.split():
            if elem not in B.split():
                C.append(elem)
        for elem in B.split():
            if elem not in A.split():
                C.append(elem)
        return ' '.join(C)

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = lab_one()
    window.show()
    app.exec_()



if __name__ == '__main__':
    main()