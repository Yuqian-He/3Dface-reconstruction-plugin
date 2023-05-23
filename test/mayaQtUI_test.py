import maya.OpenMayaUI as omui
from shiboken2 import wrapInstance
from PySide2 import QtWidgets
from PySide2.QtCore import Qt

def get_mainwindow():
    window=omui.MQtUtil.mainWindow()
    return wrapInstance(int(window),QtWidgets.QDialog)
    
class FaceGenerator(QtWidgets.QDialog):
    def __init__(self,parent=get_mainwindow()):
        super().__init__(parent)
        self.setWindowTitle("Face Model Generator")
        self.resize(400,100)
        # add grid layout
        self.grid_layout=QtWidgets.QGridLayout(self)
        self.selectImage_text=QtWidgets.QLabel()
        self.selectImage_text.setText("Select Face Image: ")
        self.grid_layout.addWidget(self.selectImage_text,0,0,1,1)
        self.line_edit = QtWidgets.QLineEdit()
        self.line_edit.setReadOnly(True)
        self.grid_layout.addWidget(self.line_edit,1,0,1,1)
        self.load_image=QtWidgets.QPushButton("browse",self)
        self.grid_layout.addWidget(self.load_image,1,1,1,1)
        self.generate_image=QtWidgets.QPushButton("generate",self)
        self.generate_image.setFixedSize(200, 20)
        self.grid_layout.addWidget(self.generate_image,4, 0, 1, 3, Qt.AlignHCenter)
        # self.database_view=QtWidgets.QTableView(self)

if __name__=="__main__":
    try:
        face_dialog.close()
        face_dialog.deleteLater()
    except:
        pass
    
    face_dialog=FaceGenerator()
    face_dialog.show()
        
