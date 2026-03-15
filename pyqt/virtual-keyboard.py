import sys
from PyQt6.QtWidgets import QMainWindow,QApplication, QWidget,QPushButton,QLabel,QLCDNumber,QCheckBox,QLineEdit
x=5
y=55
a=0
b=''
class Keyboard(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        global x,y,a
        self.setGeometry(700,400,500,250)
        self.setWindowTitle('Виртуальная клавиатура')
        self.ln01=QLineEdit(self)
        self.ln01.move(10,10)
        self.ln01.resize(200,30)
        for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            a=a+1
            if a==10:
                y=y+40
                x=5
                a=1
            self.btn=QPushButton(i,self)
            self.btn.resize(40,40)
            self.btn.move(x,y)
            x=x+40
            self.btn.clicked.connect(self.write)
        self.btn01=QPushButton(' ',self)
        self.btn01.move(5,175)
        self.btn01.resize(120,40)
        self.btn01.clicked.connect(self.write)
        self.btn02=QPushButton('<--', self)
        self.btn02.move(365,55)
        self.btn02.resize(100,40)
        self.btn02.clicked.connect(self.delete)
        self.btn03=QPushButton('<',self)
        self.btn03.move(165,175)
        self.btn03.resize(100,40)
        self.btn03.clicked.connect(lambda: self.backward())
        self.btn04=QPushButton('>',self)
        self.btn04.move(265,175)
        self.btn04.resize(100,40)
        self.btn04.clicked.connect(lambda: self.forward())
        
        

    def write(self):
        global b
        b=b+self.sender().text()
        self.ln01.setText(b)

    def delete(self):
        global b
        b=b[:-1]
        self.ln01.setText(b)

    def backward(self):
        self.ln01.setFocus()
        x=self.ln01.cursorPosition()
        self.ln01.setCursorPosition(x-1)

    def forward(self):
        self.ln01.setFocus()
        x=self.ln01.cursorPosition()
        self.ln01.setCursorPosition(x+1)
        

   
        
            
            



if __name__=='__main__':
    app=QApplication(sys.argv)
    ex=Keyboard()
    ex.show()
    sys.exit(app.exec())
