import os
import zipfile
def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.py'):
                ziph.write(os.path.join(root, file))
  
  
if __name__ == "__main__": 
    zipf = zipfile.ZipFile('../Submissions/exam03.zip', 'w', zipfile.ZIP_DEFLATED)
    zipdir('./exam03/', zipf)
    zipf.close()   