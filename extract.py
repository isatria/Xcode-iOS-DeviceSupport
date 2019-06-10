import argparse
import os
from os import path, listdir
import zipfile

srcPath = path.join(path.dirname(path.abspath(__file__)), 'src')
deviceSupportPath = 'Contents/Developer/Platforms/iPhoneOS.platform/DeviceSupport'

def extractZIP(file, target):
    fileName = file + '.zip'
    filePath = path.join(srcPath, fileName)
    
    zipRef = zipfile.ZipFile(filePath, 'r')
    print('Extracting File:' + fileName)
    zipRef.extractall(target)
    print('Successful extraction ' + target + '/' +  fileName)

def clone(xcodePath):
    targetPath = path.join(xcodePath, deviceSupportPath)
    isExistTargetPath = os.path.isdir(targetPath)

    if os.getuid() != 0:
        print('Permission Denied. This command need administrative access to your computer for extraction file.')
        exit()
    elif isExistTargetPath == False:
        print('Incorrect Target Path')
        exit()
    else:
        deviceSupportFiles = [deviceSupport.replace('.zip', '') for deviceSupport in listdir(srcPath) if deviceSupport.endswith('.zip')]
        existingDeviceSupportFiles = listdir(targetPath)
        
        diffs = set(deviceSupportFiles) - set(existingDeviceSupportFiles)

        if len(diffs) < 1:
            print('Nothing needs to be imported')
            exit()
        
        for fileName in diffs: extractZIP(fileName, targetPath)

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Extract DeviceSupport files to Xcode.app')
    
    parser.add_argument(
        '--target',
        type = str, 
        dest = 'xcodePath',
        default = '/Applications/Xcode.app',
        help = 'custom Xcode.app path location'
        )
        
    args = parser.parse_args()
    clone(args.xcodePath)