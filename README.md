PyArmor demonstration
====

<br>

## Overview
- Blog [[Qiita]](https://qiita.com/Takayoshi_Makabe/items/f38380bd1d097ac9d797)

<br>

## Directory
```
./
　├ Single_Module/   # single python module
　├ Single_Module_Obfuscating_pre/   # immediately after encryption
　├ Single_Module/   # Changes from the directory above (file path only)
　├ Whole_Module/   # A module containing .py files in a subdirectory
　├ Whole_Module_Obfuscating_pre/   # immediately after encryption
  └ Whole_Module_Obfuscating/   # Changes from the directory above (file path only) 
```

## Command

```
# single module
$ pyarmor licenses --expired 2022-01-01 r001
$ pyarmor obfuscate --with-license licenses/r001/license.lic main.py


# By default, only the *.py in the same path as the entry script are obfuscated.
# To obfuscate all the *.py in the sub-folder recursively, execute this command.
$ $ pyarmor obfuscate --with-license licenses/r001/license.lic main.py
```
