import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow, QDialog, QVBoxLayout, QLabel, QWidget

class myGame(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("PushButton Widgets(Yes or No)? ")
        self.setGeometry(100, 100, 400,400)
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        yes_button = QPushButton("Bắt đầu game")
        yes_button.clicked.connect(self.show_dialog_choi)
        
        no_button = QPushButton("Thoát Game")
        no_button.clicked.connect(self.show_dialog_thoat)
        
        layout = QVBoxLayout()
        layout.addWidget(yes_button)
        layout.addWidget(no_button)
        
        central_widget.setLayout(layout)
        
    def show_dialog_choi(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Thông báo")
        
        label = QLabel("Chương trình đã bắt đầu")
        
        dialog_layout= QVBoxLayout()
        dialog_layout.addWidget(label)
        
        dialog.setLayout(dialog_layout)
        
        dialog.exec_()
        
        
    def show_dialog_thoat(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Thông báo")
        
        label = QLabel("Bạn đã thoát game")
        
        dialog_layout= QVBoxLayout()
        dialog_layout.addWidget(label)
        
        dialog.setLayout(dialog_layout)
        
        dialog.exec_()
        
def main():
    app = QApplication(sys.argv)
    window = myGame()
    window.show()
    sys.exit(app.exec_())
if __name__ == "__main__":
    main()
        
        
        
        