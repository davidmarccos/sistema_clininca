import sys
from Views import PrimeiraWindow
from Controller.controllerView import *


class MeuApp(QtWidgets.QMainWindow, PrimeiraWindow.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MeuApp, self).__init__(parent)

        # parametros
        self.controler = ControllerView()

        # métodos_Executaveis ao iniciar
        self.setupUi(self)
        self.initEvent()

    def initEvent(self):
        self.btn_cad_cliente.clicked.connect(self.controler.chamar_cadastro_cliente)
        self.btn_reg_consulta.clicked.connect(self.controler.chamar_cadastro_consulta)


def main():
    app = QtWidgets.QApplication(sys.argv)
    form = MeuApp()
    form.show()

    app.exec_()


if __name__ == '__main__':
    main()
