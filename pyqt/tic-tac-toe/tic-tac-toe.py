import sys
from PyQt6.QtWidgets import QMainWindow,QApplication, QWidget,QPushButton,QLabel,QLCDNumber,QCheckBox,QRadioButton,QButtonGroup
x=100
y=100
a=0
b=0
class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setGeometry(500,250,500,500)
        self.setWindowTitle('Крестики-нолики')
        global x,y,a
        self.radio_btn_x=QRadioButton('X',self)
        self.radio_btn_x.move(200,25)
        self.radio_btn_x.click()
        self.radio_btn_0=QRadioButton('0',self)
        self.radio_btn_0.move(250,25)
        self.radio_group=QButtonGroup()
        self.radio_group.addButton(self.radio_btn_x)
        self.radio_group.addButton(self.radio_btn_0)
        self.btn02=QPushButton('Новая игра',self)
        self.btn02.resize(self.btn02.sizeHint())
        self.btn02.move(125,450)
        self.btn02.clicked.connect(lambda: self.restart())
        self.button_group=QButtonGroup()
        for i in range(9):
            self.btn=QPushButton(self)
            self.btn.resize(90,90)
            self.btn.move(x,y)
            self.button_group.addButton(self.btn)
            x=x+100
            a=a+1
            if a==3:
                x=100
                y=y+100
                a=0
            self.btn.clicked.connect(lambda: self.point()) 
        self.lb01=QLabel('',self)
        self.lb01.move(125,400)
        self.lb01.hide()
    def point(self):
        global b
        b=b+1
        if b==9:
            self.lb01.setText('Ничья!')
            self.lb01.show()
        self.sender().setText(self.radio_group.checkedButton().text())
        self.sender().setEnabled(False)
        if self.radio_btn_0.isChecked():
            self.radio_btn_x.click()
        else:
            self.radio_btn_0.click()
        x=self.button_group.buttons()
        for i in range(0,6,3):
            if x[i].text()==x[i+1].text() and x[i].text()==x[i+2].text() and x[i+1].text()==x[i+2].text() and not x[i].text()=='':
                self.lb01.setText(f'Победили {x[i].text()}!')
                self.lb01.show()
                self.stop()
        for i in range(0,2):
            if x[i].text()==x[i+3].text() and x[i].text()==x[i+6].text() and x[i+3].text()==x[i+6].text() and not x[i].text()=='':
                self.lb01.setText(f'Победили {x[i].text()}!')
                self.lb01.show()
                self.stop()
        if x[0].text()==x[4].text() and x[0].text()==x[8].text() and x[4].text()==x[8].text() and not x[0].text()=='':
            self.lb01.setText(f'Победили {x[0].text()}!')
            self.lb01.show()
            self.stop()
        elif x[2].text()==x[4].text() and x[6].text()==x[2].text() and x[4].text()==x[6].text() and not x[2].text()=='':
            self.lb01.setText(f'Победили {x[2].text()}!')
            self.lb01.show()
            self.stop()

    def stop(self):
        x=self.button_group.buttons()
        for i in range(0,9):
            x[i].setEnabled(False)
            
    def restart(self):
        global b
        b=0
        x=self.button_group.buttons()
        for i in range(0,9):
            x[i].setEnabled(True)
            x[i].setText('')
        self.lb01.hide()
        
        
                
                    
        
        
        
        


            
        
                
            
        




if __name__=='__main__':
    app=QApplication(sys.argv)
    ex=Example()

    ex.show()
    sys.exit(app.exec())
