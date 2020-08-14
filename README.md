# Novus Space Python module
Please download the files and put the novusspace directory in the root of your project, then you can import the module.
```python
import novusspace
```
## Install the module
You need pip instance to install novusspace package, you can install it whit the command below
```python
pip install novusspace
```
Now you can totally use the novusspace module

## Module var
```python
from novusspace import var

var.toIntList('Your list here') # Change str list to int list
var.toStrList('Your list here') # Change int list to str list
```

## Module update
```python
from novusspace import update

update.update('old file', 'new file url', 'new file name', 'path where the new file will be added', logs=(False is the default value))
```

## Module infos
```python
from novusspace.credentials import infos

infos.getVersion() # Return version of the module
infos.getAuthor() # Return author of the module
infos.getCompany() # Return company of the module
```

## License
[Novus Space](https://novusspace.inovaperf.me/License.html)
