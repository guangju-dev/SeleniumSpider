import sys
import ui
from PyQt5.QtWidgets import QApplication,QMainWindow
#主程序入口
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = ui.Ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
