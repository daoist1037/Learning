import zipfile, os
def myzip(folder):
    number = 1
    while True:
        zipName = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipName):
            break
        number = number +1
    backup = zipfile.ZipFile(zipName, 'w')
    for folderName,subfolders,  files in os.walk(os.path.abspath(folder)):
        backup.write(folderName, compress_type=zipfile.ZIP_DEFLATED)
        #for subfolder in subfolders:
            #
        for filename in files:
            backup.write(os.path.join(folderName, filename), compress_type=zipfile.ZIP_DEFLATED)


myzip('..\\java')