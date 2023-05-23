import os,sys,subprocess
import maya.cmds as cmds
import maya.OpenMayaUI as omui
from shiboken2 import wrapInstance
from PySide2 import QtWidgets
from PySide2.QtWidgets import QProgressDialog
from PySide2.QtCore import Qt,QThread,Signal

path=sys.executable
path=os.path.dirname(path)
path=os.path.dirname(path)
fileName=''

class AiThread(QThread):

    def __init__(self,input_path,parent=None):
        super(AiThread,self).__init__(parent)
        self.input_path=input_path

    progess_update=Signal(int)
    
    def run_ai(self):
        python_path=path+'\\AIenv\\python.exe'
        project_path=path+'\\released_v0.1\\facialDetails.py'
        # inputImage_path='C:\\Users\\97919\\Desktop\\released_v0.1\\released_v0.1\\samples\\details\\nic01.jpg'
        # outputResult_path='C:\\Users\\97919\\Desktop\\released_v0.1\\released_v0.1\\results'
        inputImage_path = self.input_path 
        print(inputImage_path)
        outputResult_path = os.path.abspath(path+'\\released_v0.1\\results')

        arg=python_path+" "+project_path+" "+"-i"+" "+inputImage_path+" "+"-o"+" "+outputResult_path
        result=subprocess.run(arg,stdout=subprocess.PIPE,shell=True)
        output=result.stdout.decode('utf-8')
        print(output)

    def showMesh(self):
        fileName=os.path.basename(self.input_path)
        fileName=os.path.splitext(fileName)[0]
        meshPath=path+'\\released_v0.1\\results\\'+fileName+'\\result.obj'
        print(fileName)
        cmds.file(meshPath,i=True,type="OBJ",rnn=True,ns=fileName)
        # find the object name
        mesh_name=fileName+':Mesh'
        mtl_file_path=path+'\\released_v0.1\\results\\'+fileName+'\\result.mtl'
        shading_group_name = cmds.sets(name=mesh_name + "SG", empty=True, renderable=True, noSurfaceShader=True)
        surface_shader_name = cmds.shadingNode("surfaceShader", asShader=True, name=mesh_name + "SS") 
        cmds.connectAttr(surface_shader_name + ".outColor", shading_group_name + ".surfaceShader")


    def update_progress(self,value):
        self.progess_update.emit(value)

def get_mainwindow():
    window=omui.MQtUtil.mainWindow()
    return wrapInstance(int(window),QtWidgets.QDialog)
    
class FaceGenerator(QtWidgets.QDialog):

    def __init__(self,parent=get_mainwindow()):
        super().__init__(parent)
        self.progress_dialog=None
        self.path=' '
        self.name=' '
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
        self.load_image.clicked.connect(self.load_file)
        self.grid_layout.addWidget(self.load_image,1,1,1,1)
        self.generate_image=QtWidgets.QPushButton("generate",self)
        self.generate_image.clicked.connect(self.generate_mesh)
        self.generate_image.setFixedSize(200, 30)
        self.grid_layout.addWidget(self.generate_image,4, 0, 1, 3, Qt.AlignHCenter)
        # self.database_view=QtWidgets.QTableView(self)

    def load_file(self):
        self.ext=' '
        self.path=cmds.fileDialog2(fm=1)[0]
        self.name=os.path.basename(self.path)
        self.name,self.ext=os.path.splitext(self.name)
        print(self.name)

        IMG_EXTENSIONS = [
        '.jpg', '.JPG', '.jpeg', '.JPEG',
        '.png', '.PNG', '.ppm', '.PPM', '.bmp', '.BMP','.tif',
        ]   

        if self.ext not in IMG_EXTENSIONS:
            QtWidgets.QMessageBox.critical(self,"Critial Error","Not valid file type",QtWidgets.QMessageBox.StandardButton.Abort)
            raise ValueError('Invalid file type, please select image file')
        else:
            self.line_edit.setText(self.path)

    def generate_mesh(self):
        input_path=self.path
        ai_thread=AiThread(input_path)
        ai_thread.run_ai()
        ai_thread.showMesh()
        self.close()

    def process_window(self):
        setValue=100000
        self.progress_dialog = QProgressDialog("Generating Mesh...", "Cancel", 0, 100, self)
        self.progress_dialog.setWindowModality(Qt.WindowModal)
        self.progress_dialog.setAutoClose(True)
        self.progress_dialog.setAutoReset(True)
        self.progress_dialog.setValue(0)
        self.progress_dialog.show()

        for i in range(setValue):
            self.progress_dialog.setValue(i/1000)



if __name__=="__main__":
    try:
        face_dialog.close()
        face_dialog.deleteLater()
    except:
        pass
    
    face_dialog=FaceGenerator()
    face_dialog.show()


