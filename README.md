# iOS DeviceSupport for Xcode [![Tweet](https://img.shields.io/twitter/url/http/shields.io.svg?style=social)](https://twitter.com/intent/tweet?text=Check%20out%20Xcode-iOS-DeviceSupport%20on%20GitHub&url=https://github.com/isatria/Xcode-iOS-DeviceSupport)

![last commit](https://img.shields.io/github/last-commit/isatria/Xcode-iOS-DeviceSupport.svg)


Will update regularly.

## Usage: ##
Below command is trying to extract all files zip of device support to **/Applications/Xcode.app**.

```pyton
sudo pyton extract.py
```

You can use `--target` if your Xcode is not in **/Applications/**

```pyton
sudo python extract.py --target /Document/Xcode.app
```

```
python extract.py -h
usage: extract.py [-h] [--target XCODEPATH]

Extract DeviceSupport files to Xcode.app

optional arguments:
  -h, --help          show this help message and exit
  --target XCODEPATH  custom Xcode.app path location
```
### Manual ###
1. Close **Xcode**.
2. Open **Finder**.
3. Press **Shift**+**⌘ (Command)**+**G** to open *Go to Folder*
4. Enter: `/Applications/Xcode/Contents/Developer/Platforms/iPhoneOS.platform/DeviceSupport/`.
5. Then extract (unzip) and copy the latest Device Support file do you want to this directory.

**Note :**  
If your **Xcode.app** is not in `/Applications/`, change `/Applications/Xcode` to match the path of the existence of **Xcode.app**.

## Supported Versions ##
#### iOS 13: ####
> * [13.0 (17A5492t)](https://github.com/isatria/Xcode-iOS-DeviceSupport/raw/master/src/13.0.zip) `31 May 2019`

#### iOS 12: ####
> * [12.2 (16E226)](https://github.com/isatria/Xcode-iOS-DeviceSupport/raw/master/src/12.2%20(16E226).zip) `14 March 2019`
> * [12.1 (16B93)](https://github.com/isatria/Xcode-iOS-DeviceSupport/raw/master/src/12.1.zip) `24 October 2018`
> * [12.0 (16A366)](https://github.com/isatria/Xcode-iOS-DeviceSupport/raw/master/src/12.0.zip) `29 August 2018`

#### iOS 11: ####
> * [11.4 (15F79)](https://github.com/isatria/Xcode-iOS-DeviceSupport/raw/master/src/11.4.zip) `12 May 2018`
> * [11.3 (15E216)](https://github.com/isatria/Xcode-iOS-DeviceSupport/raw/master/src/11.3.zip) `14 March 2018`
> * [11.2 (15C114)](https://github.com/isatria/Xcode-iOS-DeviceSupport/raw/master/src/11.2.zip) `30 November 2017`
> * [11.1 (15B87)](https://github.com/isatria/Xcode-iOS-DeviceSupport/raw/master/src/11.1.zip) `13 October 2017`
> * [11.0 (15A372)](https://github.com/isatria/Xcode-iOS-DeviceSupport/raw/master/src/11.0.zip) `2 September 2017`

#### iOS 10: ####
> * [10.3 (14E277)](https://github.com/isatria/Xcode-iOS-DeviceSupport/raw/master/src/10.3.zip) `15 March 2017`
> * [10.2 (14C92)](https://github.com/isatria/Xcode-iOS-DeviceSupport/raw/master/src/10.2.zip) `16 December 2016`
> * [10.1 (14B72c)](https://github.com/isatria/Xcode-iOS-DeviceSupport/raw/master/src/10.1.zip) `22 October 2016`
> * [10.0 (14A345)](https://github.com/isatria/Xcode-iOS-DeviceSupport/raw/master/src/10.0.zip) `13 September 2016`

#### iOS 9: ####
> * [9.3 (13E238)](https://github.com/isatria/Xcode-iOS-DeviceSupport/raw/master/src/9.3.zip) `29 March 2016`
> * [9.2 (13C75)](https://github.com/isatria/Xcode-iOS-DeviceSupport/raw/master/src/9.2.zip) `14 December 2015`
> * [9.1 (13B143)](https://github.com/isatria/Xcode-iOS-DeviceSupport/raw/master/src/9.1.zip) `23 October 2015`
> * [9.0 (13A344)](https://github.com/isatria/Xcode-iOS-DeviceSupport/raw/master/src/9.0.zip) `8 September 2015`

#### iOS 8: ####
> * [8.4](https://github.com/isatria/Xcode-iOS-DeviceSupport/raw/master/src/8.4.zip) `25 June 2015`
> * [8.3](https://github.com/isatria/Xcode-iOS-DeviceSupport/raw/master/src/8.3.zip) `9 April 2015`
> * [8.2](https://github.com/isatria/Xcode-iOS-DeviceSupport/raw/master/src/8.2.zip) `9 April 2015`
> * [8.1](https://github.com/isatria/Xcode-iOS-DeviceSupport/raw/master/src/8.1.zip) `14 October 2014`
> * [8.0](https://github.com/isatria/Xcode-iOS-DeviceSupport/raw/master/src/8.0.zip) `20 August 2014`

## External links ##
* [Official Latest Xcode](https://developer.apple.com/services-account/download?path=/WWDC_2019/Xcode_11_Beta/Xcode_11_Beta.xip)

## Credit ##
[iGhibli/iOS-DeviceSupport](https://github.com/iGhibli/iOS-DeviceSupport)
