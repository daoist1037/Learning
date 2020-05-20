import shutil, os
shelf = open('dir.txt', 'w')
for folderName, subfolders, fileName in os.walk('D:\\study\\Py'):
    #print('The pwd is '+folderName)
    shelf.writelines('The pwd is '+folderName + '\n')
    for i in subfolders:
        #print('The subfolders is' +i)
        shelf.writelines('The subfolders is ' +folderName+'\\'+i+'\n')
    for j in fileName:
        #print('The firlName is' +j)
        shelf.writelines('The firlName is ' +folderName+'\\'+j+'\n')
    print('\n')
    shelf.write('\n')
shelf.close()