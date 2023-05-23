import os,sys,subprocess

path=sys.executable
path=os.path.dirname(path)
path=os.path.dirname(path)
fileName=''

def run_ai():
        python_path=path+'\\AIenv\\python.exe'
        project_path=path+'\\released_v0.1\\facialDetails.py'
        # this is the path i used for test on my own computer
        inputImage_path='C:\\Users\\97919\\Desktop\\released_v0.1\\released_v0.1\\samples\\details\\nic01.jpg'
        outputResult_path='C:\\Users\\97919\\Desktop\\released_v0.1\\released_v0.1\\results'
        print(inputImage_path)
        outputResult_path = os.path.abspath(path+'\\released_v0.1\\results')

        arg=python_path+" "+project_path+" "+"-i"+" "+inputImage_path+" "+"-o"+" "+outputResult_path
        result=subprocess.run(arg,stdout=subprocess.PIPE,shell=True)
        output=result.stdout.decode('utf-8')
        print(output)

run_ai()