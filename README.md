# Overall ([video](https://youtu.be/RNKzpYd654A))
The primary goal of this project is to develop a plugin that is compatible with Maya and import into Unreal Engine5. This plugin is intended to leverage facial images as input data in order to create 3D models that possess rigging capabilities, and can be used in various virtual environments.

The subject can be divided into several subtasks. The first subtask involves the development of a 3D facial reconstruction algorithm, which is capable of creating a 3D model of a face from a 2D image in Maya. The second subtask involves transforming the output model into a mesh that can be further processed. The third subtask is to develop an automatic rigging algorithm that can apply skeletal structures to the model in a way that is suitable for animation. Lastly, the fourth subtask entails developing a key point mapping system that can automatically recognize and associate specific facial landmarks to their corresponding locations on the rig. This process is crucial for ensuring precise and realistic facial animations, as it allows for the mapping of specific areas on the face that should be moved when conveying various emotions or expressions.

# Method
## 3D face reconstruction (pick up the ai model)
### [ESO](https://github.com/patrikhuber/eos)
ESO: The EOS (Eigen-based Object and Scene reconstruction) library is an open-source software library for 3D object and scene reconstruction from 2D images. It provides a set of C++ and Python libraries and tools for developing applications that can perform tasks such as camera calibration, feature detection and matching, and 3D reconstruction. 

### [Facial Detail Synthesis](https://github.com/apchenstu/Facial_Details_Synthesis)
Facial Detail Synthesis: the model is designed to generate high-resolution facial model that contain fine-grained details such as wrinkles, blemishes, and pores from a low-resolution input image. I chose this project as basic 3D face reconstruction algorithm. In addition, I modified the output format and adjusted some of the code related to system paths to a version that is compatible with Maya.

## Mesh modification
The output of Facial Detail Synthesis is a low-resolution proxy mesh. To ensure that all relevant information is retained for future use, the mesh should be checked and modified using 3D modeling software such as Maya. This will involve inspecting the mesh for any missing or incorrect information and making necessary adjustments to ensure that the final model is of high quality and fully optimized for use. Finally, the OBJ file can be imported into the target application, such as Unreal Engine 5, for use in the final 3D modeling or game development project. 

## Automatic rigging
Metahuman plugin in Unreal Engine: The Metahuman plugin features an "identity solve" function that enables the identification of the positioning of the eyes and mouth. This allows for the creation of a Metahuman model with a control rig face. But this way needs default facial features.

I selected the Metahuman plugin for this project due to time constraints. After processing the human face mesh, the plugin can automatically complete the entire human head and rig it.

## Application
Upon completion of the aforementioned processes, a facial model equipped with a control rig can be obtained, which can subsequently be imported into the Unreal Engine and utilized for implementing face motion capture.

# Build（only for Windows）
[Bridge.py](https://github.com/NCCA/pipelineandtd22-Yuqian-He/blob/main/Bridge.py): This is the script runing on maya scripts editor. 

[Facial Detail Synthesis](https://github.com/apchenstu/Facial_Details_Synthesis): This is the AI model I used in this project. You can download [my version](https://drive.google.com/file/d/1wu3N_toknADuCYPHCKeHfS66xjx_66we/view?usp=share_link) as I changed to ensure compatibility with Maya.

[Virtual env](https://github.com/apchenstu/Facial_Details_Synthesis): This virual env was created based on which can run the ai model. You can download my [virtual env](https://drive.google.com/file/d/1BxT_pzV3SyqWvWa2Uec3iWl5_N3f1x6m/view?usp=share_link) as I installed everything already. As for people try to build by themselves, here is the steps:
 ```c
//I use Anaconda Prompt terminal

//create an virtual env, I use python 3.6 version
conda create --name myenv python=3.6
//activate this virtual env
conda activate myenv
//install libraries
conda install pip
pip install numpy h5py Pillow scikit-image scipy
conda install pytorch torchvision torchaudio cudatoolkit=your_cuda_version -c pytorch
pip install --force-reinstall eos-py==0.16.1
 ```

Please ensure that your virtual environment and AI model are placed in the root directory of your Maya installation.(Mine is ..../Maya202)









