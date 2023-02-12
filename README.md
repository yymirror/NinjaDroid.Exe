NinjaDroid-Exe (64-bit)
==========

NinjaDroid is a simple tool to reverse engineering Android APK packages.
##### This is a Windows 64-bit ONLY build-spec for 'Nuitka' (Python3).
##### Releases were packed as one-file executable with "BoxedApp Packer".


[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
![NinjaDroid](docs/images/ninjadroid.gif "Screencast of NinjaDroid")

## Overview

NinjaDroid uses [AXMLParser](https://github.com/appknox/pyaxmlparser) together with a series of Python scripts based on `aapt`, `keytool`, `string` and such to extract a series of information from a given APK package, such as:

- List of files of the APK: file name, size, MD5, SHA-1, SHA-256 and SHA-512
- `AndroidManifest.xml` info: app name, package name, version, sdks, permissions, activities, services, broadcast-receivers, ...
- `CERT.RSA/DSA` digital certificate info: serial number, validity, fingerprint, issuer and owner
- List of URLs, shell commands and other generic strings hard-coded into the `classes.dex` files

Furthermore, NinjaDroid uses [apktool](https://github.com/iBotPeaches/Apktool) and [dex2jar](https://github.com/pxb1988/dex2jar) to extract and store:

- JSON report file, which contains all the extracted APK info
- `AndroidManifest.xml` file (thanks to `apktool`)
- `CERT.RSA/DSA` digital certificate file
- `classes.dex` files
- translated _.jar_ file (thanks to `dex2jar`)
- disassembled smali files (thanks to `apktool`)
- `assets/` and `res/` folders together with their content (thanks to `apktool`)

## Usage

The following are examples of running NinjaDroid against the sample APK package.

### Show APK summary
```shell
$ ninjadroid regression/data/Example.apk
```
```shell
file:    regression/data/Example.apk
size:    70058
md5:     c9504f487c8b51412ba4980bfe3cc15d
sha1:    482a28812495b996a92191fbb3be1376193ca59b
sha256:  8773441a656b60c5e18481fd5ba9c1bf350d98789b975987cb3b2b57ee44ee51
sha512:  559eab9840ff2f8507842605e60bb0730442ddf9ee7ca4ab4f386f715c1a4707766065d6f0b977816886692bf88b400643979e2fd13e6999358a21cabdfb3071
name:    Example
cert:
	file:   META-INF/CERT.RSA
	size:   906
	md5:    860e19fa47d37d9510f1245c511a8578
	sha1:   59a04084c0d5ef23fd05f0f429dab6267ccb3d0b
	sha256: 0efa622919417adfa6eb77770fd33d3bcd93265ac7343695e246dab1a7b6bfee
	sha512: 2a5befcc0bcb14e44d7b7cb4322a76933ad3e90e5e1ffbb87ba31ee7cc0172725dcc98e9d414fb3a207bc107b2a7ca7563b5f954cac6bd41d77e4726c70a95a3
manifest:
	file:   AndroidManifest.xml
	size:   6544
	md5:    1f97f7e7ca62f39f8f81d79b1b540c37
	sha1:   011316a011e5b8738c12c662cb0b0a6ffe04ca74
	sha256: 7c8011a46191ecb368bf2e0104049abeb98bae8a7b1fa3328ff050aed85b1347
	sha512: 8c7c1ede610f9c6613418b46a52a196ad6d5e8cc067c2f26b931738ad8087f998d9ea95e80ec4352c95fbdbb93a4f29c646973535068a3a3d584da95480ab45f
	package: com.example.app
	version:
		code:  1
		name:  1.0
	sdk:
		min:   10
		target: 20
		max:   20
	permissions:
		- android.permission.INTERNET
		- android.permission.READ_EXTERNAL_STORAGE
		- android.permission.RECEIVE_BOOT_COMPLETED
		- android.permission.WRITE_EXTERNAL_STORAGE
dex:
	file:   classes.dex
	size:   2132
	md5:    7bc52ece5249ccd2d72c4360f9be2ca5
	sha1:   89476799bf92798047ca026c922a5bc33983b008
	sha256: 3f543c68c4c059548cec619a68f329010d797e5e4c00aa46cd34c0d19cabe056
	sha512: 0725f961bc1bac47eb8dd045c2f0a0cf5475fd77089af7ddc3098e341a95d8b5624969b6fa47606a05d5a6adf9d74d0c52562ea41a376bd3d7d0aa3695ca2e22
```

### Show APK extended information in JSON format
```shell
$ ninjadroid regression/data/Example.apk --all --json
```
```json
{
    "cert": {
        "file": "META-INF/CERT.RSA",
        "fingerprint": {
            "md5": "",
            "sha1": "5A:C0:6C:32:63:7F:5D:BE:CA:F9:38:38:4C:FA:FF:ED:20:52:43:B6",
            "sha256": "E5:15:CC:BC:5E:BF:B2:9D:A6:13:03:63:CF:19:33:FA:CE:AF:DC:ED:5D:2F:F5:98:7C:CE:37:13:64:4A:CF:77",
            "signature": "SHA1withRSA",
            "version": "3"
        },
        "issuer": {
            "city": "City",
            "country": "XX",
            "domain": "",
            "email": "",
            "name": "Name",
            "organization": "Organization",
            "state": "State",
            "unit": "Unit"
        },
        "md5": "860e19fa47d37d9510f1245c511a8578",
        "owner": {
            "city": "City",
            "country": "XX",
            "domain": "",
            "email": "",
            "name": "Name",
            "organization": "Organization",
            "state": "State",
            "unit": "Unit"
        },
        "serial_number": "558e7595",
        "sha1": "59a04084c0d5ef23fd05f0f429dab6267ccb3d0b",
        "sha256": "0efa622919417adfa6eb77770fd33d3bcd93265ac7343695e246dab1a7b6bfee",
        "sha512": "2a5befcc0bcb14e44d7b7cb4322a76933ad3e90e5e1ffbb87ba31ee7cc0172725dcc98e9d414fb3a207bc107b2a7ca7563b5f954cac6bd41d77e4726c70a95a3",
        "size": 906,
        "validity": {
            "from": "2015-06-27 10:06:13Z",
            "until": "2515-02-26 10:06:13Z"
        }
    },
    "dex": [
        {
            "file": "classes.dex",
            "md5": "7bc52ece5249ccd2d72c4360f9be2ca5",
            "sha1": "89476799bf92798047ca026c922a5bc33983b008",
            "sha256": "3f543c68c4c059548cec619a68f329010d797e5e4c00aa46cd34c0d19cabe056",
            "sha512": "0725f961bc1bac47eb8dd045c2f0a0cf5475fd77089af7ddc3098e341a95d8b5624969b6fa47606a05d5a6adf9d74d0c52562ea41a376bd3d7d0aa3695ca2e22",
            "shell_commands": [
                "set"
            ],
            "size": 2132,
            "strings": [
                "!Lcom/example/app/ExampleService2;",
                "!Lcom/example/app/ExampleService3;",
                "#Landroid/content/BroadcastReceiver;",
                ")Lcom/example/app/ExampleBrodcastReceiver;",
                "*Lcom/example/app/ExampleBrodcastReceiver2;",
                "*Lcom/example/app/ExampleBrodcastReceiver3;",
                "*Lcom/example/app/ExampleBrodcastReceiver4;",
                "<init>",
                "Landroid/app/Activity;",
                "Landroid/app/Service;",
                "Landroid/content/Context;",
                "Landroid/content/Intent;",
                "Landroid/os/Bundle;",
                "Landroid/os/IBinder;",
                "Lcom/example/app/ExampleService;",
                "Lcom/example/app/HomeActivity;",
                "Lcom/example/app/OtherActivity;",
                "onBind",
                "onCreate",
                "onReceive",
                "setContentView"
            ],
            "urls": []
        }
    ],
    "file": "regression/data/Example.apk",
    "manifest": {
        "activities": [
            {
                "intent-filter": [
                    {
                        "action": [
                            "android.intent.action.MAIN"
                        ],
                        "category": [
                            "android.intent.category.LAUNCHER"
                        ]
                    }
                ],
                "launchMode": "1",
                "name": "com.example.app.HomeActivity"
            },
            {
                "intent-filter": [
                    {
                        "action": [
                            "android.intent.action.VIEW"
                        ],
                        "category": [
                            "android.intent.category.DEFAULT"
                        ],
                        "data": [
                            {
                                "scheme": "content"
                            },
                            {
                                "scheme": "file"
                            },
                            {
                                "mimeType": "application/vnd.android.package-archive"
                            }
                        ]
                    }
                ],
                "launchMode": "1",
                "meta-data": [
                    {
                        "name": "android.support.PARENT_ACTIVITY",
                        "value": "com.example.app.HomeActivity"
                    }
                ],
                "name": "com.example.app.OtherActivity",
                "noHistory": "true",
                "parentActivityName": "com.example.app.HomeActivity"
            }
        ],
        "file": "AndroidManifest.xml",
        "md5": "1f97f7e7ca62f39f8f81d79b1b540c37",
        "package": "com.example.app",
        "permissions": [
            "android.permission.INTERNET",
            "android.permission.READ_EXTERNAL_STORAGE",
            "android.permission.RECEIVE_BOOT_COMPLETED",
            "android.permission.WRITE_EXTERNAL_STORAGE"
        ],
        "receivers": [
            {
                "name": "com.example.app.ExampleBrodcastReceiver"
            },
            {
                "exported": false,
                "intent-filter": [
                    {
                        "action": [
                            "android.intent.action.BOOT_COMPLETED",
                            "android.intent.action.MY_PACKAGE_REPLACED"
                        ],
                        "priority": "1000"
                    }
                ],
                "name": "com.example.app.ExampleBrodcastReceiver2"
            },
            {
                "enabled": true,
                "exported": false,
                "intent-filter": [
                    {
                        "action": [
                            "android.intent.action.BROADCAST_PACKAGE_REMOVED",
                            "android.intent.action.PACKAGE_ADDED",
                            "android.intent.action.PACKAGE_REPLACED"
                        ],
                        "data": [
                            {
                                "scheme": "package"
                            }
                        ],
                        "priority": "800"
                    }
                ],
                "name": "com.example.app.ExampleBrodcastReceiver3"
            },
            {
                "enabled": false,
                "exported": true,
                "name": "com.example.app.ExampleBrodcastReceiver4"
            }
        ],
        "sdk": {
            "max": "20",
            "min": "10",
            "target": "20"
        },
        "services": [
            {
                "name": "com.example.app.ExampleService"
            },
            {
                "enabled": false,
                "exported": true,
                "isolatedProcess": true,
                "name": "com.example.app.ExampleService2"
            },
            {
                "enabled": true,
                "exported": false,
                "isolatedProcess": false,
                "name": "com.example.app.ExampleService3"
            }
        ],
        "sha1": "011316a011e5b8738c12c662cb0b0a6ffe04ca74",
        "sha256": "7c8011a46191ecb368bf2e0104049abeb98bae8a7b1fa3328ff050aed85b1347",
        "sha512": "8c7c1ede610f9c6613418b46a52a196ad6d5e8cc067c2f26b931738ad8087f998d9ea95e80ec4352c95fbdbb93a4f29c646973535068a3a3d584da95480ab45f",
        "size": 6544,
        "version": {
            "code": 1,
            "name": "1.0"
        }
    },
    [...]
```

### Extract and store APK entries and information
```shell
$ ninjadroid regression/data/Example.apk --all --extract output/
```
```shell
  >> NinjaDroid: [INFO] Executing apktool...
  >> NinjaDroid: [INFO] Creating output/smali/...
  >> NinjaDroid: [INFO] Creating output/AndroidManifest.xml...
  >> NinjaDroid: [INFO] Creating output/res/...
  >> NinjaDroid: [INFO] Creating output/assets/...
  >> NinjaDroid: [INFO] Executing dex2jar...
  >> NinjaDroid: [INFO] Creating output/Example.jar...
dex2jar regression/data/Example.apk -> output/Example.jar
  >> NinjaDroid: [INFO] Extracting certificate file...
  >> NinjaDroid: [INFO] Creating output/META-INF/CERT.RSA...
  >> NinjaDroid: [INFO] Extracting DEX files...
  >> NinjaDroid: [INFO] Creating output/classes.dex...
  >> NinjaDroid: [INFO] Generating JSON report file...
  >> NinjaDroid: [INFO] Creating output/report-Example.json...
```
**NOTE:** without specifying an output directory, one with the APK package name will be created inside the current working directory.



## Licence

NinjaDroid is licensed under the GNU General Public License v3.0 (http://www.gnu.org/licenses/gpl-3.0.html).
