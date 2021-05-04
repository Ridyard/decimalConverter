Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from pathlib import Path
>>> Path(alex/yo)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    Path(alex/yo)
NameError: name 'alex' is not defined
>>> Path('alex'/'yo')
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    Path('alex'/'yo')
TypeError: unsupported operand type(s) for /: 'str' and 'str'
>>> Path('alex','yo')
WindowsPath('alex/yo')
>>> lst = ['alex', 'abby','millie']
>>> for i in lst:
	print(Path(i))

	
alex
abby
millie
>>> import os
>>> print(os.cwd)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    print(os.cwd)
AttributeError: module 'os' has no attribute 'cwd'
>>> Path('millie')/'dog'
WindowsPath('millie/dog')
>>> print(os.cwd())
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    print(os.cwd())
AttributeError: module 'os' has no attribute 'cwd'
>>> cwd()
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    cwd()
NameError: name 'cwd' is not defined
>>> print(Path(cwd()))
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    print(Path(cwd()))
NameError: name 'cwd' is not defined
>>> Path.cwd()
WindowsPath('C:/Users/Alex/AppData/Local/Programs/Python/Python39')
>>> Path('alex', 'test.txt')
WindowsPath('alex/test.txt')
>>> Path.cwd()
WindowsPath('C:/Users/Alex/AppData/Local/Programs/Python/Python39')
>>> os.chdir(Path.cwd()/..)
SyntaxError: invalid syntax
>>> p = path.cwd()
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    p = path.cwd()
NameError: name 'path' is not defined
>>> p = Path.cwd()
>>> p
WindowsPath('C:/Users/Alex/AppData/Local/Programs/Python/Python39')
>>> os.chdir('C:\\Windows')
>>> Path.cwd()
WindowsPath('C:/Windows')
>>> os.chdir(p)
>>> Path.cwd()
WindowsPath('C:/Users/Alex/AppData/Local/Programs/Python/Python39')
>>> Path.home()
WindowsPath('C:/Users/Alex')
>>> Path(Path.cwd(), 'test1')
WindowsPath('C:/Users/Alex/AppData/Local/Programs/Python/Python39/test1')
>>> os.mkdirs(Path(Path.cwd(), 'test1'))
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    os.mkdirs(Path(Path.cwd(), 'test1'))
AttributeError: module 'os' has no attribute 'mkdirs'
>>> os.makedirs(Path(Path.cwd(), 'test1'))
>>> '..'.is_absolute()
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    '..'.is_absolute()
AttributeError: 'str' object has no attribute 'is_absolute'
>>> Path('..')
WindowsPath('..')
>>> Path('..').is_absolute()
False
>>> Path('.').is_absolute()
False
>>> Path(Path.cwd()).is_absolute()
True
>>> Path.cwd().is_absolute()
True
>>> Path(Path.cwd()/'muffins').is_absolute()
True
>>> Path(Path.cwd()/'muffins.txt').is_absolute()
True
>>> val = ('a','b','c','d')
>>> (e,f,*g) = val
>>> val
('a', 'b', 'c', 'd')
>>> g
['c', 'd']
>>> os.path.abspath('.')
'C:\\Users\\Alex\\AppData\\Local\\Programs\\Python\\Python39'
>>> os.path.relpath('.', '..\\..\\..')
'Programs\\Python\\Python39'
>>> os.path.abspayh('.\\scripts')
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    os.path.abspayh('.\\scripts')
AttributeError: module 'ntpath' has no attribute 'abspayh'
>>> os.path.abspath('.\\scripts')
'C:\\Users\\Alex\\AppData\\Local\\Programs\\Python\\Python39\\scripts'
>>> os.listdir('.')
['DLLs', 'Doc', 'include', 'Lib', 'libs', 'LICENSE.txt', 'NEWS.txt', 'python.exe', 'python3.dll', 'python39.dll', 'pythonw.exe', 'Scripts', 'tcl', 'Tools', 'vcruntime140.dll', 'vcruntime140_1.dll', 'Workspace']
>>> os.listdir('.\\Workspace')
['ATBS', 'Git test files', 'Small Projects']
>>> os.path.getsize('\\Workspace')
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    os.path.getsize('\\Workspace')
  File "C:\Users\Alex\AppData\Local\Programs\Python\Python39\lib\genericpath.py", line 50, in getsize
    return os.stat(filename).st_size
FileNotFoundError: [WinError 2] The system cannot find the file specified: '\\Workspace'
>>> os.path.getsize('.\\Workspace')
0
>>> os.path.getsize('.\\workspace')
0
>>> os.path.getsize('.')
4096
>>> os.path.getsize('.\\workspace\\atbs')
16384
>>> p = Path.home()
>>> p
WindowsPath('C:/Users/Alex')
>>> list(p.glob('*'))
[WindowsPath('C:/Users/Alex/.bash_history'), WindowsPath('C:/Users/Alex/.gconf'), WindowsPath('C:/Users/Alex/.gconfd'), WindowsPath('C:/Users/Alex/.gitconfig'), WindowsPath('C:/Users/Alex/.idlerc'), WindowsPath('C:/Users/Alex/.minttyrc'), WindowsPath('C:/Users/Alex/.oracle_jre_usage'), WindowsPath('C:/Users/Alex/.recently-used.xbel'), WindowsPath('C:/Users/Alex/.recently-used.xbel.4WVUDX'), WindowsPath('C:/Users/Alex/.ssh'), WindowsPath('C:/Users/Alex/.swt'), WindowsPath('C:/Users/Alex/AppData'), WindowsPath('C:/Users/Alex/Contacts'), WindowsPath('C:/Users/Alex/Desktop'), WindowsPath('C:/Users/Alex/Documents'), WindowsPath('C:/Users/Alex/Downloads'), WindowsPath('C:/Users/Alex/Favorites'), WindowsPath('C:/Users/Alex/Links'), WindowsPath('C:/Users/Alex/Music'), WindowsPath('C:/Users/Alex/ntuser.dat'), WindowsPath('C:/Users/Alex/ntuser.dat.LOG1'), WindowsPath('C:/Users/Alex/ntuser.dat.LOG2'), WindowsPath('C:/Users/Alex/ntuser.dat{8d59b30e-78ee-11ea-bf4f-d850e63812f0}.TxR.0.regtrans-ms'), WindowsPath('C:/Users/Alex/ntuser.dat{8d59b30e-78ee-11ea-bf4f-d850e63812f0}.TxR.1.regtrans-ms'), WindowsPath('C:/Users/Alex/ntuser.dat{8d59b30e-78ee-11ea-bf4f-d850e63812f0}.TxR.2.regtrans-ms'), WindowsPath('C:/Users/Alex/ntuser.dat{8d59b30e-78ee-11ea-bf4f-d850e63812f0}.TxR.blf'), WindowsPath('C:/Users/Alex/ntuser.dat{8d59b30f-78ee-11ea-bf4f-d850e63812f0}.TM.blf'), WindowsPath('C:/Users/Alex/ntuser.dat{8d59b30f-78ee-11ea-bf4f-d850e63812f0}.TMContainer00000000000000000001.regtrans-ms'), WindowsPath('C:/Users/Alex/ntuser.dat{8d59b30f-78ee-11ea-bf4f-d850e63812f0}.TMContainer00000000000000000002.regtrans-ms'), WindowsPath('C:/Users/Alex/NTUSER.DAT{bbed3e3b-0b41-11e3-8249-d6927d06400b}.TM.blf'), WindowsPath('C:/Users/Alex/NTUSER.DAT{bbed3e3b-0b41-11e3-8249-d6927d06400b}.TMContainer00000000000000000001.regtrans-ms'), WindowsPath('C:/Users/Alex/NTUSER.DAT{bbed3e3b-0b41-11e3-8249-d6927d06400b}.TMContainer00000000000000000002.regtrans-ms'), WindowsPath('C:/Users/Alex/ntuser.ini'), WindowsPath('C:/Users/Alex/Pictures'), WindowsPath('C:/Users/Alex/README.md'), WindowsPath('C:/Users/Alex/Saved Games'), WindowsPath('C:/Users/Alex/Searches'), WindowsPath('C:/Users/Alex/SkyDrive'), WindowsPath('C:/Users/Alex/Tracing'), WindowsPath('C:/Users/Alex/Videos'), WindowsPath('C:/Users/Alex/workspace')]
>>> lst = list(p.glob('*'))
>>> for i in lst:
	print(i)

	
C:\Users\Alex\.bash_history
C:\Users\Alex\.gconf
C:\Users\Alex\.gconfd
C:\Users\Alex\.gitconfig
C:\Users\Alex\.idlerc
C:\Users\Alex\.minttyrc
C:\Users\Alex\.oracle_jre_usage
C:\Users\Alex\.recently-used.xbel
C:\Users\Alex\.recently-used.xbel.4WVUDX
C:\Users\Alex\.ssh
C:\Users\Alex\.swt
C:\Users\Alex\AppData
C:\Users\Alex\Contacts
C:\Users\Alex\Desktop
C:\Users\Alex\Documents
C:\Users\Alex\Downloads
C:\Users\Alex\Favorites
C:\Users\Alex\Links
C:\Users\Alex\Music
C:\Users\Alex\ntuser.dat
C:\Users\Alex\ntuser.dat.LOG1
C:\Users\Alex\ntuser.dat.LOG2
C:\Users\Alex\ntuser.dat{8d59b30e-78ee-11ea-bf4f-d850e63812f0}.TxR.0.regtrans-ms
C:\Users\Alex\ntuser.dat{8d59b30e-78ee-11ea-bf4f-d850e63812f0}.TxR.1.regtrans-ms
C:\Users\Alex\ntuser.dat{8d59b30e-78ee-11ea-bf4f-d850e63812f0}.TxR.2.regtrans-ms
C:\Users\Alex\ntuser.dat{8d59b30e-78ee-11ea-bf4f-d850e63812f0}.TxR.blf
C:\Users\Alex\ntuser.dat{8d59b30f-78ee-11ea-bf4f-d850e63812f0}.TM.blf
C:\Users\Alex\ntuser.dat{8d59b30f-78ee-11ea-bf4f-d850e63812f0}.TMContainer00000000000000000001.regtrans-ms
C:\Users\Alex\ntuser.dat{8d59b30f-78ee-11ea-bf4f-d850e63812f0}.TMContainer00000000000000000002.regtrans-ms
C:\Users\Alex\NTUSER.DAT{bbed3e3b-0b41-11e3-8249-d6927d06400b}.TM.blf
C:\Users\Alex\NTUSER.DAT{bbed3e3b-0b41-11e3-8249-d6927d06400b}.TMContainer00000000000000000001.regtrans-ms
C:\Users\Alex\NTUSER.DAT{bbed3e3b-0b41-11e3-8249-d6927d06400b}.TMContainer00000000000000000002.regtrans-ms
C:\Users\Alex\ntuser.ini
C:\Users\Alex\Pictures
C:\Users\Alex\README.md
C:\Users\Alex\Saved Games
C:\Users\Alex\Searches
C:\Users\Alex\SkyDrive
C:\Users\Alex\Tracing
C:\Users\Alex\Videos
C:\Users\Alex\workspace
>>> for i in lst:
	print(i.stem)

	
.bash_history
.gconf
.gconfd
.gitconfig
.idlerc
.minttyrc
.oracle_jre_usage
.recently-used
.recently-used.xbel
.ssh
.swt
AppData
Contacts
Desktop
Documents
Downloads
Favorites
Links
Music
ntuser
ntuser.dat
ntuser.dat
ntuser.dat{8d59b30e-78ee-11ea-bf4f-d850e63812f0}.TxR.0
ntuser.dat{8d59b30e-78ee-11ea-bf4f-d850e63812f0}.TxR.1
ntuser.dat{8d59b30e-78ee-11ea-bf4f-d850e63812f0}.TxR.2
ntuser.dat{8d59b30e-78ee-11ea-bf4f-d850e63812f0}.TxR
ntuser.dat{8d59b30f-78ee-11ea-bf4f-d850e63812f0}.TM
ntuser.dat{8d59b30f-78ee-11ea-bf4f-d850e63812f0}.TMContainer00000000000000000001
ntuser.dat{8d59b30f-78ee-11ea-bf4f-d850e63812f0}.TMContainer00000000000000000002
NTUSER.DAT{bbed3e3b-0b41-11e3-8249-d6927d06400b}.TM
NTUSER.DAT{bbed3e3b-0b41-11e3-8249-d6927d06400b}.TMContainer00000000000000000001
NTUSER.DAT{bbed3e3b-0b41-11e3-8249-d6927d06400b}.TMContainer00000000000000000002
ntuser
Pictures
README
Saved Games
Searches
SkyDrive
Tracing
Videos
workspace
>>> for i in lst:
	print(i.stem + '.' + i.suffix)

	
.bash_history.
.gconf.
.gconfd.
.gitconfig.
.idlerc.
.minttyrc.
.oracle_jre_usage.
.recently-used..xbel
.recently-used.xbel..4WVUDX
.ssh.
.swt.
AppData.
Contacts.
Desktop.
Documents.
Downloads.
Favorites.
Links.
Music.
ntuser..dat
ntuser.dat..LOG1
ntuser.dat..LOG2
ntuser.dat{8d59b30e-78ee-11ea-bf4f-d850e63812f0}.TxR.0..regtrans-ms
ntuser.dat{8d59b30e-78ee-11ea-bf4f-d850e63812f0}.TxR.1..regtrans-ms
ntuser.dat{8d59b30e-78ee-11ea-bf4f-d850e63812f0}.TxR.2..regtrans-ms
ntuser.dat{8d59b30e-78ee-11ea-bf4f-d850e63812f0}.TxR..blf
ntuser.dat{8d59b30f-78ee-11ea-bf4f-d850e63812f0}.TM..blf
ntuser.dat{8d59b30f-78ee-11ea-bf4f-d850e63812f0}.TMContainer00000000000000000001..regtrans-ms
ntuser.dat{8d59b30f-78ee-11ea-bf4f-d850e63812f0}.TMContainer00000000000000000002..regtrans-ms
NTUSER.DAT{bbed3e3b-0b41-11e3-8249-d6927d06400b}.TM..blf
NTUSER.DAT{bbed3e3b-0b41-11e3-8249-d6927d06400b}.TMContainer00000000000000000001..regtrans-ms
NTUSER.DAT{bbed3e3b-0b41-11e3-8249-d6927d06400b}.TMContainer00000000000000000002..regtrans-ms
ntuser..ini
Pictures.
README..md
Saved Games.
Searches.
SkyDrive.
Tracing.
Videos.
workspace.
>>> p = Path.cwd()
>>> p
WindowsPath('C:/Users/Alex/AppData/Local/Programs/Python/Python39')
>>> p = Path.cwd()/'workspace/atbs'
>>> p
WindowsPath('C:/Users/Alex/AppData/Local/Programs/Python/Python39/workspace/atbs')
>>> list(p.glob('*.py'))
[WindowsPath('C:/Users/Alex/AppData/Local/Programs/Python/Python39/workspace/atbs/001.001 - name length.py'), WindowsPath('C:/Users/Alex/AppData/Local/Programs/Python/Python39/workspace/atbs/001.002 - guess the number.py'), WindowsPath('C:/Users/Alex/AppData/Local/Programs/Python/Python39/workspace/atbs/002.001 - total 0-100.py'), WindowsPath('C:/Users/Alex/AppData/Local/Programs/Python/Python39/workspace/atbs/002.002 - logical operator test.py'), WindowsPath('C:/Users/Alex/AppData/Local/Programs/Python/Python39/workspace/atbs/003.001 - magic8.py'), WindowsPath('C:/Users/Alex/AppData/Local/Programs/Python/Python39/workspace/atbs/003.001 - magic82.py'), WindowsPath('C:/Users/Alex/AppData/Local/Programs/Python/Python39/workspace/atbs/003.002 - abcd call stack.py'), WindowsPath('C:/Users/Alex/AppData/Local/Programs/Python/Python39/workspace/atbs/003.003 - zigzag.py'), WindowsPath('C:/Users/Alex/AppData/Local/Programs/Python/Python39/workspace/atbs/003.003 - zigzag2.py'), WindowsPath('C:/Users/Alex/AppData/Local/Programs/Python/Python39/workspace/atbs/003.004 - collatz sequence.py'), WindowsPath('C:/Users/Alex/AppData/Local/Programs/Python/Python39/workspace/atbs/004.001 - cats.py'), WindowsPath('C:/Users/Alex/AppData/Local/Programs/Python/Python39/workspace/atbs/004.002 - conway.py'), WindowsPath('C:/Users/Alex/AppData/Local/Programs/Python/Python39/workspace/atbs/004.003 - comma code.py'), WindowsPath('C:/Users/Alex/AppData/Local/Programs/Python/Python39/workspace/atbs/004.004 - coin flip streaks.py'), WindowsPath('C:/Users/Alex/AppData/Local/Programs/Python/Python39/workspace/atbs/004.004 - coin flip streaks2.py'), WindowsPath('C:/Users/Alex/AppData/Local/Programs/Python/Python39/workspace/atbs/005.001 - character counter.py'), WindowsPath('C:/Users/Alex/AppData/Local/Programs/Python/Python39/workspace/atbs/005.002 - tictactoe.py'), WindowsPath('C:/Users/Alex/AppData/Local/Programs/Python/Python39/workspace/atbs/005.003 - picnic list.py'), WindowsPath('C:/Users/Alex/AppData/Local/Programs/Python/Python39/workspace/atbs/005.004 - fantasy game inventory.py'), WindowsPath('C:/Users/Alex/AppData/Local/Programs/Python/Python39/workspace/atbs/006.001 - multi-clipboard.py'), WindowsPath('C:/Users/Alex/AppData/Local/Programs/Python/Python39/workspace/atbs/006.002 - bulletPointAdder.py'), WindowsPath('C:/Users/Alex/AppData/Local/Programs/Python/Python39/workspace/atbs/006.003 - tablePrinter.py'), WindowsPath('C:/Users/Alex/AppData/Local/Programs/Python/Python39/workspace/atbs/007.001 - regex intro.py'), WindowsPath('C:/Users/Alex/AppData/Local/Programs/Python/Python39/workspace/atbs/007.002 - regex findall.py'), WindowsPath('C:/Users/Alex/AppData/Local/Programs/Python/Python39/workspace/atbs/007.003 - regex email-phone finder.py'), WindowsPath('C:/Users/Alex/AppData/Local/Programs/Python/Python39/workspace/atbs/007.004 - date detection.py'), WindowsPath('C:/Users/Alex/AppData/Local/Programs/Python/Python39/workspace/atbs/008.001 - PyInputPlus basics.py'), WindowsPath('C:/Users/Alex/AppData/Local/Programs/Python/Python39/workspace/atbs/008.002 - custom validation function.py'), WindowsPath('C:/Users/Alex/AppData/Local/Programs/Python/Python39/workspace/atbs/008.003 - yesNo input.py'), WindowsPath('C:/Users/Alex/AppData/Local/Programs/Python/Python39/workspace/atbs/008.004 - multiplicationQuiz.py'), WindowsPath('C:/Users/Alex/AppData/Local/Programs/Python/Python39/workspace/atbs/008.005 - sandwhich menu.py'), WindowsPath('C:/Users/Alex/AppData/Local/Programs/Python/Python39/workspace/atbs/009.001 - path library intro.py'), WindowsPath('C:/Users/Alex/AppData/Local/Programs/Python/Python39/workspace/atbs/009.002 - path library intro.py'), WindowsPath('C:/Users/Alex/AppData/Local/Programs/Python/Python39/workspace/atbs/009.003 - read,write files.py'), WindowsPath('C:/Users/Alex/AppData/Local/Programs/Python/Python39/workspace/atbs/009.004 - read,write files.py'), WindowsPath('C:/Users/Alex/AppData/Local/Programs/Python/Python39/workspace/atbs/009.005 - glob.py'), WindowsPath('C:/Users/Alex/AppData/Local/Programs/Python/Python39/workspace/atbs/009.006 - random quiz generator.py'), WindowsPath('C:/Users/Alex/AppData/Local/Programs/Python/Python39/workspace/atbs/009.008 - general module tests.py')]
>>> for i in list(p.glob('*.py')):
	print(i)

	
C:\Users\Alex\AppData\Local\Programs\Python\Python39\workspace\atbs\001.001 - name length.py
C:\Users\Alex\AppData\Local\Programs\Python\Python39\workspace\atbs\001.002 - guess the number.py
C:\Users\Alex\AppData\Local\Programs\Python\Python39\workspace\atbs\002.001 - total 0-100.py
C:\Users\Alex\AppData\Local\Programs\Python\Python39\workspace\atbs\002.002 - logical operator test.py
C:\Users\Alex\AppData\Local\Programs\Python\Python39\workspace\atbs\003.001 - magic8.py
C:\Users\Alex\AppData\Local\Programs\Python\Python39\workspace\atbs\003.001 - magic82.py
C:\Users\Alex\AppData\Local\Programs\Python\Python39\workspace\atbs\003.002 - abcd call stack.py
C:\Users\Alex\AppData\Local\Programs\Python\Python39\workspace\atbs\003.003 - zigzag.py
C:\Users\Alex\AppData\Local\Programs\Python\Python39\workspace\atbs\003.003 - zigzag2.py
C:\Users\Alex\AppData\Local\Programs\Python\Python39\workspace\atbs\003.004 - collatz sequence.py
C:\Users\Alex\AppData\Local\Programs\Python\Python39\workspace\atbs\004.001 - cats.py
C:\Users\Alex\AppData\Local\Programs\Python\Python39\workspace\atbs\004.002 - conway.py
C:\Users\Alex\AppData\Local\Programs\Python\Python39\workspace\atbs\004.003 - comma code.py
C:\Users\Alex\AppData\Local\Programs\Python\Python39\workspace\atbs\004.004 - coin flip streaks.py
C:\Users\Alex\AppData\Local\Programs\Python\Python39\workspace\atbs\004.004 - coin flip streaks2.py
C:\Users\Alex\AppData\Local\Programs\Python\Python39\workspace\atbs\005.001 - character counter.py
C:\Users\Alex\AppData\Local\Programs\Python\Python39\workspace\atbs\005.002 - tictactoe.py
C:\Users\Alex\AppData\Local\Programs\Python\Python39\workspace\atbs\005.003 - picnic list.py
C:\Users\Alex\AppData\Local\Programs\Python\Python39\workspace\atbs\005.004 - fantasy game inventory.py
C:\Users\Alex\AppData\Local\Programs\Python\Python39\workspace\atbs\006.001 - multi-clipboard.py
C:\Users\Alex\AppData\Local\Programs\Python\Python39\workspace\atbs\006.002 - bulletPointAdder.py
C:\Users\Alex\AppData\Local\Programs\Python\Python39\workspace\atbs\006.003 - tablePrinter.py
C:\Users\Alex\AppData\Local\Programs\Python\Python39\workspace\atbs\007.001 - regex intro.py
C:\Users\Alex\AppData\Local\Programs\Python\Python39\workspace\atbs\007.002 - regex findall.py
C:\Users\Alex\AppData\Local\Programs\Python\Python39\workspace\atbs\007.003 - regex email-phone finder.py
C:\Users\Alex\AppData\Local\Programs\Python\Python39\workspace\atbs\007.004 - date detection.py
C:\Users\Alex\AppData\Local\Programs\Python\Python39\workspace\atbs\008.001 - PyInputPlus basics.py
C:\Users\Alex\AppData\Local\Programs\Python\Python39\workspace\atbs\008.002 - custom validation function.py
C:\Users\Alex\AppData\Local\Programs\Python\Python39\workspace\atbs\008.003 - yesNo input.py
C:\Users\Alex\AppData\Local\Programs\Python\Python39\workspace\atbs\008.004 - multiplicationQuiz.py
C:\Users\Alex\AppData\Local\Programs\Python\Python39\workspace\atbs\008.005 - sandwhich menu.py
C:\Users\Alex\AppData\Local\Programs\Python\Python39\workspace\atbs\009.001 - path library intro.py
C:\Users\Alex\AppData\Local\Programs\Python\Python39\workspace\atbs\009.002 - path library intro.py
C:\Users\Alex\AppData\Local\Programs\Python\Python39\workspace\atbs\009.003 - read,write files.py
C:\Users\Alex\AppData\Local\Programs\Python\Python39\workspace\atbs\009.004 - read,write files.py
C:\Users\Alex\AppData\Local\Programs\Python\Python39\workspace\atbs\009.005 - glob.py
C:\Users\Alex\AppData\Local\Programs\Python\Python39\workspace\atbs\009.006 - random quiz generator.py
C:\Users\Alex\AppData\Local\Programs\Python\Python39\workspace\atbs\009.008 - general module tests.py
>>> for i in list(p.glob('*.py'):
	      
SyntaxError: invalid syntax
>>> for i in list(p.glob('*.py')):
	print(i.name)

	
001.001 - name length.py
001.002 - guess the number.py
002.001 - total 0-100.py
002.002 - logical operator test.py
003.001 - magic8.py
003.001 - magic82.py
003.002 - abcd call stack.py
003.003 - zigzag.py
003.003 - zigzag2.py
003.004 - collatz sequence.py
004.001 - cats.py
004.002 - conway.py
004.003 - comma code.py
004.004 - coin flip streaks.py
004.004 - coin flip streaks2.py
005.001 - character counter.py
005.002 - tictactoe.py
005.003 - picnic list.py
005.004 - fantasy game inventory.py
006.001 - multi-clipboard.py
006.002 - bulletPointAdder.py
006.003 - tablePrinter.py
007.001 - regex intro.py
007.002 - regex findall.py
007.003 - regex email-phone finder.py
007.004 - date detection.py
008.001 - PyInputPlus basics.py
008.002 - custom validation function.py
008.003 - yesNo input.py
008.004 - multiplicationQuiz.py
008.005 - sandwhich menu.py
009.001 - path library intro.py
009.002 - path library intro.py
009.003 - read,write files.py
009.004 - read,write files.py
009.005 - glob.py
009.006 - random quiz generator.py
009.008 - general module tests.py
>>> 
= RESTART: C:/Users/Alex/AppData/Local/Programs/Python/Python39/Workspace/ATBS/009.005 - glob2.py
cwd is C:\Users\Alex\AppData\Local\Programs\Python\Python39\Workspace\ATBS
>>> 
= RESTART: C:/Users/Alex/AppData/Local/Programs/Python/Python39/Workspace/ATBS/009.005 - glob2.py
cwd is C:\Users\Alex\AppData\Local\Programs\Python\Python39\Workspace\ATBS
files in cwd:
001.001 - name length.py
001.002 - guess the number.py
002.001 - total 0-100.py
002.002 - logical operator test.py
003.001 - magic8.py
003.001 - magic82.py
003.002 - abcd call stack.py
003.003 - zigzag.py
003.003 - zigzag2.py
003.004 - collatz sequence.py
004.001 - cats.py
004.002 - conway.py
004.003 - comma code.py
004.004 - coin flip streaks.py
004.004 - coin flip streaks2.py
005.001 - character counter.py
005.002 - tictactoe.py
005.003 - picnic list.py
005.004 - fantasy game inventory.py
006.001 - multi-clipboard.py
006.002 - bulletPointAdder.py
006.003 - tablePrinter.py
007.001 - regex intro.py
007.002 - regex findall.py
007.003 - regex email-phone finder.py
007.004 - date detection.py
008.001 - PyInputPlus basics.py
008.002 - custom validation function.py
008.003 - yesNo input.py
008.004 - multiplicationQuiz.py
008.005 - sandwhich menu.py
009.001 - path library intro.py
009.002 - path library intro.py
009.003 - read,write files.py
009.004 - read,write files.py
009.005 - glob.py
009.005 - glob2.py
009.006 - random quiz generator.py
009.008 - general module tests.py
>>> 
= RESTART: C:/Users/Alex/AppData/Local/Programs/Python/Python39/Workspace/ATBS/009.005 - glob2.py
cwd is C:\Users\Alex\AppData\Local\Programs\Python\Python39\Workspace\ATBS
files in cwd:
001.001 - name length.py
001.002 - guess the number.py
002.001 - total 0-100.py
002.002 - logical operator test.py
003.001 - magic8.py
003.001 - magic82.py
003.002 - abcd call stack.py
003.003 - zigzag.py
003.003 - zigzag2.py
003.004 - collatz sequence.py
004.001 - cats.py
004.002 - conway.py
004.003 - comma code.py
004.004 - coin flip streaks.py
004.004 - coin flip streaks2.py
005.001 - character counter.py
005.002 - tictactoe.py
005.003 - picnic list.py
005.004 - fantasy game inventory.py
006.001 - multi-clipboard.py
006.002 - bulletPointAdder.py
006.003 - tablePrinter.py
007.001 - regex intro.py
007.002 - regex findall.py
007.003 - regex email-phone finder.py
007.004 - date detection.py
008.001 - PyInputPlus basics.py
008.002 - custom validation function.py
008.003 - yesNo input.py
008.004 - multiplicationQuiz.py
008.005 - sandwhich menu.py
009.001 - path library intro.py
009.002 - path library intro.py
009.003 - read,write files.py
009.004 - read,write files.py
009.005 - glob.py
009.005 - glob2.py
009.006 - random quiz generator.py
009.008 - general module tests.py
>>> 
= RESTART: C:/Users/Alex/AppData/Local/Programs/Python/Python39/Workspace/ATBS/009.005 - glob2.py
cwd is C:\Users\Alex\AppData\Local\Programs\Python\Python39\Workspace\ATBS
files in cwd:
001.001 - name length.py
001.002 - guess the number.py
002.001 - total 0-100.py
002.002 - logical operator test.py
003.001 - magic8.py
003.001 - magic82.py
003.002 - abcd call stack.py
003.003 - zigzag.py
003.003 - zigzag2.py
003.004 - collatz sequence.py
004.001 - cats.py
004.002 - conway.py
004.003 - comma code.py
004.004 - coin flip streaks.py
004.004 - coin flip streaks2.py
005.001 - character counter.py
005.002 - tictactoe.py
005.003 - picnic list.py
005.004 - fantasy game inventory.py
006.001 - multi-clipboard.py
006.002 - bulletPointAdder.py
006.003 - tablePrinter.py
007.001 - regex intro.py
007.002 - regex findall.py
007.003 - regex email-phone finder.py
007.004 - date detection.py
008.001 - PyInputPlus basics.py
008.002 - custom validation function.py
008.003 - yesNo input.py
008.004 - multiplicationQuiz.py
008.005 - sandwhich menu.py
009.001 - path library intro.py
009.002 - path library intro.py
009.003 - read,write files.py
009.004 - read,write files.py
009.005 - glob.py
009.005 - glob2.py
009.006 - random quiz generator.py
009.008 - general module tests.py

enter a file extension to list the contents in cwd...
py
enter a valid file extension (including the preceding '.' character
>>> 
= RESTART: C:/Users/Alex/AppData/Local/Programs/Python/Python39/Workspace/ATBS/009.005 - glob2.py
cwd is C:\Users\Alex\AppData\Local\Programs\Python\Python39\Workspace\ATBS
files in cwd:
001.001 - name length.py
001.002 - guess the number.py
002.001 - total 0-100.py
002.002 - logical operator test.py
003.001 - magic8.py
003.001 - magic82.py
003.002 - abcd call stack.py
003.003 - zigzag.py
003.003 - zigzag2.py
003.004 - collatz sequence.py
004.001 - cats.py
004.002 - conway.py
004.003 - comma code.py
004.004 - coin flip streaks.py
004.004 - coin flip streaks2.py
005.001 - character counter.py
005.002 - tictactoe.py
005.003 - picnic list.py
005.004 - fantasy game inventory.py
006.001 - multi-clipboard.py
006.002 - bulletPointAdder.py
006.003 - tablePrinter.py
007.001 - regex intro.py
007.002 - regex findall.py
007.003 - regex email-phone finder.py
007.004 - date detection.py
008.001 - PyInputPlus basics.py
008.002 - custom validation function.py
008.003 - yesNo input.py
008.004 - multiplicationQuiz.py
008.005 - sandwhich menu.py
009.001 - path library intro.py
009.002 - path library intro.py
009.003 - read,write files.py
009.004 - read,write files.py
009.005 - glob.py
009.005 - glob2.py
009.006 - random quiz generator.py
009.008 - general module tests.py

enter a file extension to list the contents in cwd...
.py
001.001 - name length.py
001.002 - guess the number.py
002.001 - total 0-100.py
002.002 - logical operator test.py
003.001 - magic8.py
003.001 - magic82.py
003.002 - abcd call stack.py
003.003 - zigzag.py
003.003 - zigzag2.py
003.004 - collatz sequence.py
004.001 - cats.py
004.002 - conway.py
004.003 - comma code.py
004.004 - coin flip streaks.py
004.004 - coin flip streaks2.py
005.001 - character counter.py
005.002 - tictactoe.py
005.003 - picnic list.py
005.004 - fantasy game inventory.py
006.001 - multi-clipboard.py
006.002 - bulletPointAdder.py
006.003 - tablePrinter.py
007.001 - regex intro.py
007.002 - regex findall.py
007.003 - regex email-phone finder.py
007.004 - date detection.py
008.001 - PyInputPlus basics.py
008.002 - custom validation function.py
008.003 - yesNo input.py
008.004 - multiplicationQuiz.py
008.005 - sandwhich menu.py
009.001 - path library intro.py
009.002 - path library intro.py
009.003 - read,write files.py
009.004 - read,write files.py
009.005 - glob.py
009.005 - glob2.py
009.006 - random quiz generator.py
009.008 - general module tests.py
>>> 
= RESTART: C:/Users/Alex/AppData/Local/Programs/Python/Python39/Workspace/ATBS/009.005 - glob2.py
cwd is C:\Users\Alex\AppData\Local\Programs\Python\Python39\Workspace\ATBS
files in cwd:
001.001 - name length.py
001.002 - guess the number.py
002.001 - total 0-100.py
002.002 - logical operator test.py
003.001 - magic8.py
003.001 - magic82.py
003.002 - abcd call stack.py
003.003 - zigzag.py
003.003 - zigzag2.py
003.004 - collatz sequence.py
004.001 - cats.py
004.002 - conway.py
004.003 - comma code.py
004.004 - coin flip streaks.py
004.004 - coin flip streaks2.py
005.001 - character counter.py
005.002 - tictactoe.py
005.003 - picnic list.py
005.004 - fantasy game inventory.py
006.001 - multi-clipboard.py
006.002 - bulletPointAdder.py
006.003 - tablePrinter.py
007.001 - regex intro.py
007.002 - regex findall.py
007.003 - regex email-phone finder.py
007.004 - date detection.py
008.001 - PyInputPlus basics.py
008.002 - custom validation function.py
008.003 - yesNo input.py
008.004 - multiplicationQuiz.py
008.005 - sandwhich menu.py
009.001 - path library intro.py
009.002 - path library intro.py
009.003 - read,write files.py
009.004 - read,write files.py
009.005 - glob.py
009.005 - glob2.py
009.006 - random quiz generator.py
009.008 - general module tests.py

enter a file extension to list the contents in cwd...
.pyw
009.007 - mcb2.pyw
>>> 
= RESTART: C:/Users/Alex/AppData/Local/Programs/Python/Python39/Workspace/ATBS/009.005 - glob2.py
cwd is C:\Users\Alex\AppData\Local\Programs\Python\Python39\Workspace\ATBS
files in cwd:
001.001 - name length.py
001.002 - guess the number.py
002.001 - total 0-100.py
002.002 - logical operator test.py
003.001 - magic8.py
003.001 - magic82.py
003.002 - abcd call stack.py
003.003 - zigzag.py
003.003 - zigzag2.py
003.004 - collatz sequence.py
004.001 - cats.py
004.002 - conway.py
004.003 - comma code.py
004.004 - coin flip streaks.py
004.004 - coin flip streaks2.py
005.001 - character counter.py
005.002 - tictactoe.py
005.003 - picnic list.py
005.004 - fantasy game inventory.py
006.001 - multi-clipboard.py
006.002 - bulletPointAdder.py
006.003 - tablePrinter.py
007.001 - regex intro.py
007.002 - regex findall.py
007.003 - regex email-phone finder.py
007.004 - date detection.py
008.001 - PyInputPlus basics.py
008.002 - custom validation function.py
008.003 - yesNo input.py
008.004 - multiplicationQuiz.py
008.005 - sandwhich menu.py
009.001 - path library intro.py
009.002 - path library intro.py
009.003 - read,write files.py
009.004 - read,write files.py
009.005 - glob.py
009.005 - glob2.py
009.006 - random quiz generator.py
009.008 - general module tests.py

enter a file extension to list the contents in cwd...
.bat
>>> 
= RESTART: C:/Users/Alex/AppData/Local/Programs/Python/Python39/Workspace/ATBS/009.005 - glob2.py
cwd is C:\Users\Alex\AppData\Local\Programs\Python\Python39\Workspace\ATBS
files in cwd:
001.001 - name length.py
001.002 - guess the number.py
002.001 - total 0-100.py
002.002 - logical operator test.py
003.001 - magic8.py
003.001 - magic82.py
003.002 - abcd call stack.py
003.003 - zigzag.py
003.003 - zigzag2.py
003.004 - collatz sequence.py
004.001 - cats.py
004.002 - conway.py
004.003 - comma code.py
004.004 - coin flip streaks.py
004.004 - coin flip streaks2.py
005.001 - character counter.py
005.002 - tictactoe.py
005.003 - picnic list.py
005.004 - fantasy game inventory.py
006.001 - multi-clipboard.py
006.002 - bulletPointAdder.py
006.003 - tablePrinter.py
007.001 - regex intro.py
007.002 - regex findall.py
007.003 - regex email-phone finder.py
007.004 - date detection.py
008.001 - PyInputPlus basics.py
008.002 - custom validation function.py
008.003 - yesNo input.py
008.004 - multiplicationQuiz.py
008.005 - sandwhich menu.py
009.001 - path library intro.py
009.002 - path library intro.py
009.003 - read,write files.py
009.004 - read,write files.py
009.005 - glob.py
009.005 - glob2.py
009.006 - random quiz generator.py
009.008 - general module tests.py

enter a file extension to list the contents in cwd...
.bak
mcb.bak
>>> 
= RESTART: C:/Users/Alex/AppData/Local/Programs/Python/Python39/Workspace/ATBS/009.005 - glob2.py
cwd is C:\Users\Alex\AppData\Local\Programs\Python\Python39\Workspace\ATBS
files in cwd:
001.001 - name length.py
001.002 - guess the number.py
002.001 - total 0-100.py
002.002 - logical operator test.py
003.001 - magic8.py
003.001 - magic82.py
003.002 - abcd call stack.py
003.003 - zigzag.py
003.003 - zigzag2.py
003.004 - collatz sequence.py
004.001 - cats.py
004.002 - conway.py
004.003 - comma code.py
004.004 - coin flip streaks.py
004.004 - coin flip streaks2.py
005.001 - character counter.py
005.002 - tictactoe.py
005.003 - picnic list.py
005.004 - fantasy game inventory.py
006.001 - multi-clipboard.py
006.002 - bulletPointAdder.py
006.003 - tablePrinter.py
007.001 - regex intro.py
007.002 - regex findall.py
007.003 - regex email-phone finder.py
007.004 - date detection.py
008.001 - PyInputPlus basics.py
008.002 - custom validation function.py
008.003 - yesNo input.py
008.004 - multiplicationQuiz.py
008.005 - sandwhich menu.py
009.001 - path library intro.py
009.002 - path library intro.py
009.003 - read,write files.py
009.004 - read,write files.py
009.005 - glob.py
009.005 - glob2.py
009.006 - random quiz generator.py
009.008 - general module tests.py

enter a file extension to list the contents in cwd...
.py
001.001 - name length.py
001.002 - guess the number.py
002.001 - total 0-100.py
002.002 - logical operator test.py
003.001 - magic8.py
003.001 - magic82.py
003.002 - abcd call stack.py
003.003 - zigzag.py
003.003 - zigzag2.py
003.004 - collatz sequence.py
004.001 - cats.py
004.002 - conway.py
004.003 - comma code.py
004.004 - coin flip streaks.py
004.004 - coin flip streaks2.py
005.001 - character counter.py
005.002 - tictactoe.py
005.003 - picnic list.py
005.004 - fantasy game inventory.py
006.001 - multi-clipboard.py
006.002 - bulletPointAdder.py
006.003 - tablePrinter.py
007.001 - regex intro.py
007.002 - regex findall.py
007.003 - regex email-phone finder.py
007.004 - date detection.py
008.001 - PyInputPlus basics.py
008.002 - custom validation function.py
008.003 - yesNo input.py
008.004 - multiplicationQuiz.py
008.005 - sandwhich menu.py
009.001 - path library intro.py
009.002 - path library intro.py
009.003 - read,write files.py
009.004 - read,write files.py
009.005 - glob.py
009.005 - glob2.py
009.006 - random quiz generator.py
009.008 - general module tests.py
>>> 
= RESTART: C:/Users/Alex/AppData/Local/Programs/Python/Python39/Workspace/ATBS/009.005 - glob2.py
cwd is C:\Users\Alex\AppData\Local\Programs\Python\Python39\Workspace\ATBS
files in cwd:
001.001 - name length.py
001.002 - guess the number.py
002.001 - total 0-100.py
002.002 - logical operator test.py
003.001 - magic8.py
003.001 - magic82.py
003.002 - abcd call stack.py
003.003 - zigzag.py
003.003 - zigzag2.py
003.004 - collatz sequence.py
004.001 - cats.py
004.002 - conway.py
004.003 - comma code.py
004.004 - coin flip streaks.py
004.004 - coin flip streaks2.py
005.001 - character counter.py
005.002 - tictactoe.py
005.003 - picnic list.py
005.004 - fantasy game inventory.py
006.001 - multi-clipboard.py
006.002 - bulletPointAdder.py
006.003 - tablePrinter.py
007.001 - regex intro.py
007.002 - regex findall.py
007.003 - regex email-phone finder.py
007.004 - date detection.py
008.001 - PyInputPlus basics.py
008.002 - custom validation function.py
008.003 - yesNo input.py
008.004 - multiplicationQuiz.py
008.005 - sandwhich menu.py
009.001 - path library intro.py
009.002 - path library intro.py
009.003 - read,write files.py
009.004 - read,write files.py
009.005 - glob.py
009.005 - glob2.py
009.006 - random quiz generator.py
009.008 - general module tests.py

enter a file extension to list the contents in cwd...
.py
001.001 - name length.py
001.002 - guess the number.py
002.001 - total 0-100.py
002.002 - logical operator test.py
003.001 - magic8.py
003.001 - magic82.py
003.002 - abcd call stack.py
003.003 - zigzag.py
003.003 - zigzag2.py
003.004 - collatz sequence.py
004.001 - cats.py
004.002 - conway.py
004.003 - comma code.py
004.004 - coin flip streaks.py
004.004 - coin flip streaks2.py
005.001 - character counter.py
005.002 - tictactoe.py
005.003 - picnic list.py
005.004 - fantasy game inventory.py
006.001 - multi-clipboard.py
006.002 - bulletPointAdder.py
006.003 - tablePrinter.py
007.001 - regex intro.py
007.002 - regex findall.py
007.003 - regex email-phone finder.py
007.004 - date detection.py
008.001 - PyInputPlus basics.py
008.002 - custom validation function.py
008.003 - yesNo input.py
008.004 - multiplicationQuiz.py
008.005 - sandwhich menu.py
009.001 - path library intro.py
009.002 - path library intro.py
009.003 - read,write files.py
009.004 - read,write files.py
009.005 - glob.py
009.005 - glob2.py
009.006 - random quiz generator.py
009.008 - general module tests.py
>>> p
WindowsPath('C:/Users/Alex/AppData/Local/Programs/Python/Python39/Workspace/ATBS')
>>> p.glob('*')
<generator object Path.glob at 0x000000D01BCEB970>
>>> for i in p.glob('*'):
	print(i)

	
C:\Users\Alex\AppData\Local\Programs\Python\Python39\Workspace\ATBS\.git
C:\Users\Alex\AppData\Local\Programs\Python\Python39\Workspace\ATBS\001.001 - name length.py
C:\Users\Alex\AppData\Local\Programs\Python\Python39\Workspace\ATBS\001.002 - guess the number.py
C:\Users\Alex\AppData\Local\Programs\Python\Python39\Workspace\ATBS\002.001 - total 0-100.py
C:\Users\Alex\AppData\Local\Programs\Python\Python39\Workspace\ATBS\002.002 - logical operator test.py
C:\Users\Alex\AppData\Local\Programs\Python\Python39\Workspace\ATBS\003.001 - magic8.py
C:\Users\Alex\AppData\Local\Programs\Python\Python39\Workspace\ATBS\003.001 - magic82.py
C:\Users\Alex\AppData\Local\Programs\Python\Python39\Workspace\ATBS\003.002 - abcd call stack.py
C:\Users\Alex\AppData\Local\Programs\Python\Python39\Workspace\ATBS\003.003 - zigzag.py
C:\Users\Alex\AppData\Local\Programs\Python\Python39\Workspace\ATBS\003.003 - zigzag2.py
C:\Users\Alex\AppData\Local\Programs\Python\Python39\Workspace\ATBS\003.004 - collatz sequence.py
C:\Users\Alex\AppData\Local\Programs\Python\Python39\Workspace\ATBS\004.001 - cats.py
C:\Users\Alex\AppData\Local\Programs\Python\Python39\Workspace\ATBS\004.002 - conway.py
C:\Users\Alex\AppData\Local\Programs\Python\Python39\Workspace\ATBS\004.003 - comma code.py
C:\Users\Alex\AppData\Local\Programs\Python\Python39\Workspace\ATBS\004.004 - coin flip streaks.py
C:\Users\Alex\AppData\Local\Programs\Python\Python39\Workspace\ATBS\004.004 - coin flip streaks2.py
C:\Users\Alex\AppData\Local\Programs\Python\Python39\Workspace\ATBS\005.001 - character counter.py
C:\Users\Alex\AppData\Local\Programs\Python\Python39\Workspace\ATBS\005.002 - tictactoe.py
C:\Users\Alex\AppData\Local\Programs\Python\Python39\Workspace\ATBS\005.003 - picnic list.py
C:\Users\Alex\AppData\Local\Programs\Python\Python39\Workspace\ATBS\005.004 - fantasy game inventory.py
C:\Users\Alex\AppData\Local\Programs\Python\Python39\Workspace\ATBS\006.001 - multi-clipboard.py
C:\Users\Alex\AppData\Local\Programs\Python\Python39\Workspace\ATBS\006.002 - bulletPointAdder.py
C:\Users\Alex\AppData\Local\Programs\Python\Python39\Workspace\ATBS\006.003 - tablePrinter.py
C:\Users\Alex\AppData\Local\Programs\Python\Python39\Workspace\ATBS\007.001 - regex intro.py
C:\Users\Alex\AppData\Local\Programs\Python\Python39\Workspace\ATBS\007.002 - regex findall.py
C:\Users\Alex\AppData\Local\Programs\Python\Python39\Workspace\ATBS\007.003 - regex email-phone finder.py
C:\Users\Alex\AppData\Local\Programs\Python\Python39\Workspace\ATBS\007.004 - date detection.py
C:\Users\Alex\AppData\Local\Programs\Python\Python39\Workspace\ATBS\008.001 - PyInputPlus basics.py
C:\Users\Alex\AppData\Local\Programs\Python\Python39\Workspace\ATBS\008.002 - custom validation function.py
C:\Users\Alex\AppData\Local\Programs\Python\Python39\Workspace\ATBS\008.003 - yesNo input.py
C:\Users\Alex\AppData\Local\Programs\Python\Python39\Workspace\ATBS\008.004 - multiplicationQuiz.py
C:\Users\Alex\AppData\Local\Programs\Python\Python39\Workspace\ATBS\008.005 - sandwhich menu.py
C:\Users\Alex\AppData\Local\Programs\Python\Python39\Workspace\ATBS\009.001 - path library intro.py
C:\Users\Alex\AppData\Local\Programs\Python\Python39\Workspace\ATBS\009.002 - path library intro.py
C:\Users\Alex\AppData\Local\Programs\Python\Python39\Workspace\ATBS\009.003 - read,write files.py
C:\Users\Alex\AppData\Local\Programs\Python\Python39\Workspace\ATBS\009.004 - read,write files.py
C:\Users\Alex\AppData\Local\Programs\Python\Python39\Workspace\ATBS\009.005 - glob.py
C:\Users\Alex\AppData\Local\Programs\Python\Python39\Workspace\ATBS\009.005 - glob2.py
C:\Users\Alex\AppData\Local\Programs\Python\Python39\Workspace\ATBS\009.006 - random quiz generator.py
C:\Users\Alex\AppData\Local\Programs\Python\Python39\Workspace\ATBS\009.007 - mcb2.pyw
C:\Users\Alex\AppData\Local\Programs\Python\Python39\Workspace\ATBS\009.008 - general module tests.py
C:\Users\Alex\AppData\Local\Programs\Python\Python39\Workspace\ATBS\automate_online-materials
C:\Users\Alex\AppData\Local\Programs\Python\Python39\Workspace\ATBS\Batch Files
C:\Users\Alex\AppData\Local\Programs\Python\Python39\Workspace\ATBS\mcb.bak
C:\Users\Alex\AppData\Local\Programs\Python\Python39\Workspace\ATBS\mcb.dat
C:\Users\Alex\AppData\Local\Programs\Python\Python39\Workspace\ATBS\mcb.dir
C:\Users\Alex\AppData\Local\Programs\Python\Python39\Workspace\ATBS\Testing files
>>> for i in p.glob('*'):
	print(i.name)

	
.git
001.001 - name length.py
001.002 - guess the number.py
002.001 - total 0-100.py
002.002 - logical operator test.py
003.001 - magic8.py
003.001 - magic82.py
003.002 - abcd call stack.py
003.003 - zigzag.py
003.003 - zigzag2.py
003.004 - collatz sequence.py
004.001 - cats.py
004.002 - conway.py
004.003 - comma code.py
004.004 - coin flip streaks.py
004.004 - coin flip streaks2.py
005.001 - character counter.py
005.002 - tictactoe.py
005.003 - picnic list.py
005.004 - fantasy game inventory.py
006.001 - multi-clipboard.py
006.002 - bulletPointAdder.py
006.003 - tablePrinter.py
007.001 - regex intro.py
007.002 - regex findall.py
007.003 - regex email-phone finder.py
007.004 - date detection.py
008.001 - PyInputPlus basics.py
008.002 - custom validation function.py
008.003 - yesNo input.py
008.004 - multiplicationQuiz.py
008.005 - sandwhich menu.py
009.001 - path library intro.py
009.002 - path library intro.py
009.003 - read,write files.py
009.004 - read,write files.py
009.005 - glob.py
009.005 - glob2.py
009.006 - random quiz generator.py
009.007 - mcb2.pyw
009.008 - general module tests.py
automate_online-materials
Batch Files
mcb.bak
mcb.dat
mcb.dir
Testing files
>>> ext = py
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    ext = py
NameError: name 'py' is not defined
>>> ext = 'py'
>>> '.'.join ext
SyntaxError: invalid syntax
>>> '.'.join(ext)
'p.y'
>>> ext = 'py'
>>> ext = '.' + ext
>>> ext
'.py'
>>> 
= RESTART: C:/Users/Alex/AppData/Local/Programs/Python/Python39/Workspace/ATBS/009.005 - glob2.py
cwd is C:\Users\Alex\AppData\Local\Programs\Python\Python39\Workspace\ATBS
files in cwd:
001.001 - name length.py
001.002 - guess the number.py
002.001 - total 0-100.py
002.002 - logical operator test.py
003.001 - magic8.py
003.001 - magic82.py
003.002 - abcd call stack.py
003.003 - zigzag.py
003.003 - zigzag2.py
003.004 - collatz sequence.py
004.001 - cats.py
004.002 - conway.py
004.003 - comma code.py
004.004 - coin flip streaks.py
004.004 - coin flip streaks2.py
005.001 - character counter.py
005.002 - tictactoe.py
005.003 - picnic list.py
005.004 - fantasy game inventory.py
006.001 - multi-clipboard.py
006.002 - bulletPointAdder.py
006.003 - tablePrinter.py
007.001 - regex intro.py
007.002 - regex findall.py
007.003 - regex email-phone finder.py
007.004 - date detection.py
008.001 - PyInputPlus basics.py
008.002 - custom validation function.py
008.003 - yesNo input.py
008.004 - multiplicationQuiz.py
008.005 - sandwhich menu.py
009.001 - path library intro.py
009.002 - path library intro.py
009.003 - read,write files.py
009.004 - read,write files.py
009.005 - glob.py
009.005 - glob2.py
009.006 - random quiz generator.py
009.008 - general module tests.py

enter a file extension to list the contents in cwd...
py
001.001 - name length.py
001.002 - guess the number.py
002.001 - total 0-100.py
002.002 - logical operator test.py
003.001 - magic8.py
003.001 - magic82.py
003.002 - abcd call stack.py
003.003 - zigzag.py
003.003 - zigzag2.py
003.004 - collatz sequence.py
004.001 - cats.py
004.002 - conway.py
004.003 - comma code.py
004.004 - coin flip streaks.py
004.004 - coin flip streaks2.py
005.001 - character counter.py
005.002 - tictactoe.py
005.003 - picnic list.py
005.004 - fantasy game inventory.py
006.001 - multi-clipboard.py
006.002 - bulletPointAdder.py
006.003 - tablePrinter.py
007.001 - regex intro.py
007.002 - regex findall.py
007.003 - regex email-phone finder.py
007.004 - date detection.py
008.001 - PyInputPlus basics.py
008.002 - custom validation function.py
008.003 - yesNo input.py
008.004 - multiplicationQuiz.py
008.005 - sandwhich menu.py
009.001 - path library intro.py
009.002 - path library intro.py
009.003 - read,write files.py
009.004 - read,write files.py
009.005 - glob.py
009.005 - glob2.py
009.006 - random quiz generator.py
009.008 - general module tests.py
>>> 
= RESTART: C:/Users/Alex/AppData/Local/Programs/Python/Python39/Workspace/ATBS/009.005 - glob2.py
cwd is C:\Users\Alex\AppData\Local\Programs\Python\Python39\Workspace\ATBS
files in cwd:
001.001 - name length.py
001.002 - guess the number.py
002.001 - total 0-100.py
002.002 - logical operator test.py
003.001 - magic8.py
003.001 - magic82.py
003.002 - abcd call stack.py
003.003 - zigzag.py
003.003 - zigzag2.py
003.004 - collatz sequence.py
004.001 - cats.py
004.002 - conway.py
004.003 - comma code.py
004.004 - coin flip streaks.py
004.004 - coin flip streaks2.py
005.001 - character counter.py
005.002 - tictactoe.py
005.003 - picnic list.py
005.004 - fantasy game inventory.py
006.001 - multi-clipboard.py
006.002 - bulletPointAdder.py
006.003 - tablePrinter.py
007.001 - regex intro.py
007.002 - regex findall.py
007.003 - regex email-phone finder.py
007.004 - date detection.py
008.001 - PyInputPlus basics.py
008.002 - custom validation function.py
008.003 - yesNo input.py
008.004 - multiplicationQuiz.py
008.005 - sandwhich menu.py
009.001 - path library intro.py
009.002 - path library intro.py
009.003 - read,write files.py
009.004 - read,write files.py
009.005 - glob.py
009.005 - glob2.py
009.006 - random quiz generator.py
009.008 - general module tests.py

enter a file extension to list the contents in cwd...
.py
001.001 - name length.py
001.002 - guess the number.py
002.001 - total 0-100.py
002.002 - logical operator test.py
003.001 - magic8.py
003.001 - magic82.py
003.002 - abcd call stack.py
003.003 - zigzag.py
003.003 - zigzag2.py
003.004 - collatz sequence.py
004.001 - cats.py
004.002 - conway.py
004.003 - comma code.py
004.004 - coin flip streaks.py
004.004 - coin flip streaks2.py
005.001 - character counter.py
005.002 - tictactoe.py
005.003 - picnic list.py
005.004 - fantasy game inventory.py
006.001 - multi-clipboard.py
006.002 - bulletPointAdder.py
006.003 - tablePrinter.py
007.001 - regex intro.py
007.002 - regex findall.py
007.003 - regex email-phone finder.py
007.004 - date detection.py
008.001 - PyInputPlus basics.py
008.002 - custom validation function.py
008.003 - yesNo input.py
008.004 - multiplicationQuiz.py
008.005 - sandwhich menu.py
009.001 - path library intro.py
009.002 - path library intro.py
009.003 - read,write files.py
009.004 - read,write files.py
009.005 - glob.py
009.005 - glob2.py
009.006 - random quiz generator.py
009.008 - general module tests.py
>>> Path.cwd()
WindowsPath('C:/Users/Alex/AppData/Local/Programs/Python/Python39/Workspace/ATBS')
>>> import os
>>> x = Path.cwd()
>>> x
WindowsPath('C:/Users/Alex/AppData/Local/Programs/Python/Python39/Workspace/ATBS')
>>> Path(x)/'Testing Files'
WindowsPath('C:/Users/Alex/AppData/Local/Programs/Python/Python39/Workspace/ATBS/Testing Files')
>>> x = Path(x)/'Testing Files'
>>> x
WindowsPath('C:/Users/Alex/AppData/Local/Programs/Python/Python39/Workspace/ATBS/Testing Files')
>>> os.chdir(x)
>>> Path.cwd()
WindowsPath('C:/Users/Alex/AppData/Local/Programs/Python/Python39/Workspace/ATBS/Testing Files')
>>> doc = Path('spam.txt')
>>> doc.write_text('hello world')
11
>>> doc.read_text()
'hello world'
>>> doc1 = Path('spam2.txt')
>>> doc1.write_text('this is a test file for ATBS - files chapter')
44
>>> doc1 = ('spam3.txt')
>>> doc1.write_text('')
Traceback (most recent call last):
  File "<pyshell#106>", line 1, in <module>
    doc1.write_text('')
AttributeError: 'str' object has no attribute 'write_text'
>>> doc1 = Path('spam2.txt')
>>> doc1.write_text('')
0
>>> doc1 = Path('spam2.txt')
>>> doc1.write_text('this is a test file for ATBS chapter on files')
45
>>> doc1.read_text()
'this is a test file for ATBS chapter on files'
>>> testfile = open(doc1)
>>> testfile
<_io.TextIOWrapper name='spam2.txt' mode='r' encoding='cp1252'>
>>> testfile.read()
'this is a test file for ATBS chapter on files'
>>> o = testfile.read()
>>> o
''
>>> testfile
<_io.TextIOWrapper name='spam2.txt' mode='r' encoding='cp1252'>
>>> testfile.read()
''
>>> Path.cwd()
WindowsPath('C:/Users/Alex/AppData/Local/Programs/Python/Python39/Workspace/ATBS/Testing Files')
>>> open('spam2.txt')
<_io.TextIOWrapper name='spam2.txt' mode='r' encoding='cp1252'>
>>> a = open('spam2.txt')
>>> a
<_io.TextIOWrapper name='spam2.txt' mode='r' encoding='cp1252'>
>>> a.reead()
Traceback (most recent call last):
  File "<pyshell#123>", line 1, in <module>
    a.reead()
AttributeError: '_io.TextIOWrapper' object has no attribute 'reead'
>>> a.read()
'this is a test file for ATBS chapter on files'
>>> a = open(./'spam2.txt')
SyntaxError: invalid syntax
>>> a = open(.\'spam2.txt')
	 
SyntaxError: invalid syntax
>>> a = open('.'\'spam2.txt')
	 
SyntaxError: unexpected character after line continuation character
>>> a = open('.'/'spam2.txt')
Traceback (most recent call last):
  File "<pyshell#128>", line 1, in <module>
    a = open('.'/'spam2.txt')
TypeError: unsupported operand type(s) for /: 'str' and 'str'
>>> a = open('.\\spam2.txt')
>>> a
<_io.TextIOWrapper name='.\\spam2.txt' mode='r' encoding='cp1252'>
>>> a.read()
'this is a test file for ATBS chapter on files'
>>> p
WindowsPath('C:/Users/Alex/AppData/Local/Programs/Python/Python39/Workspace/ATBS')
>>> o
''
>>> a
<_io.TextIOWrapper name='.\\spam2.txt' mode='r' encoding='cp1252'>
>>> i
WindowsPath('C:/Users/Alex/AppData/Local/Programs/Python/Python39/Workspace/ATBS/009.008 - general module tests.py')
>>> open('spam1.txt')
Traceback (most recent call last):
  File "<pyshell#136>", line 1, in <module>
    open('spam1.txt')
FileNotFoundError: [Errno 2] No such file or directory: 'spam1.txt'
>>> p
WindowsPath('C:/Users/Alex/AppData/Local/Programs/Python/Python39/Workspace/ATBS')
>>> doc1
WindowsPath('spam2.txt')
>>> x
WindowsPath('C:/Users/Alex/AppData/Local/Programs/Python/Python39/Workspace/ATBS/Testing Files')
>>> open(Path(x)/'spam1.txt')
Traceback (most recent call last):
  File "<pyshell#140>", line 1, in <module>
    open(Path(x)/'spam1.txt')
FileNotFoundError: [Errno 2] No such file or directory: 'C:\\Users\\Alex\\AppData\\Local\\Programs\\Python\\Python39\\Workspace\\ATBS\\Testing Files\\spam1.txt'
>>> open(Path(x)/'spam1.txt','w')
<_io.TextIOWrapper name='C:\\Users\\Alex\\AppData\\Local\\Programs\\Python\\Python39\\Workspace\\ATBS\\Testing Files\\spam1.txt' mode='w' encoding='cp1252'>
>>> d1 = open('spam1.txt')
>>> d1
<_io.TextIOWrapper name='spam1.txt' mode='r' encoding='cp1252'>
>>> d1.read()
''
>>> d1 = open('spam1.txt', w)
Traceback (most recent call last):
  File "<pyshell#145>", line 1, in <module>
    d1 = open('spam1.txt', w)
NameError: name 'w' is not defined
>>> d1 = open('spam1.txt', 'w')
>>> d1.write('hello there\n, this is a test of files\n, using python')
52
>>> d1.readlines()
Traceback (most recent call last):
  File "<pyshell#148>", line 1, in <module>
    d1.readlines()
io.UnsupportedOperation: not readable
>>> d1.readlines()
Traceback (most recent call last):
  File "<pyshell#149>", line 1, in <module>
    d1.readlines()
io.UnsupportedOperation: not readable
>>> d1
<_io.TextIOWrapper name='spam1.txt' mode='w' encoding='cp1252'>
>>> d1.readline()
Traceback (most recent call last):
  File "<pyshell#151>", line 1, in <module>
    d1.readline()
io.UnsupportedOperation: not readable
>>> d1 = 'spam1.txt'
>>> d1
'spam1.txt'
>>> d1 = open('spam1.txt')
>>> d1.read()
'hello there\n, this is a test of files\n, using python'
>>> d1.readlines()
[]
>>> d1.readlines()
[]
>>> d1.read()
''
>>> d1 = open(x/'spam1.txt')
>>> d1.readlines()
['hello there\n', 'this is a test of files\n', 'using python\n', '\n', "When, in disgrace with fortune and men's eyes,\n", 'I all alone beweep my outcast state,\n', 'And trouble deaf heaven with my bootless cries,\n', 'And look upon myself and curse my fate,']
>>> d2 = open(x/'spam0.txt')
Traceback (most recent call last):
  File "<pyshell#161>", line 1, in <module>
    d2 = open(x/'spam0.txt')
FileNotFoundError: [Errno 2] No such file or directory: 'C:\\Users\\Alex\\AppData\\Local\\Programs\\Python\\Python39\\Workspace\\ATBS\\Testing Files\\spam0.txt'
>>> d2 = open(x/'spam0.txt','w')
>>> d2
<_io.TextIOWrapper name='C:\\Users\\Alex\\AppData\\Local\\Programs\\Python\\Python39\\Workspace\\ATBS\\Testing Files\\spam0.txt' mode='w' encoding='cp1252'>
>>> d2.read()
Traceback (most recent call last):
  File "<pyshell#164>", line 1, in <module>
    d2.read()
io.UnsupportedOperation: not readable
>>> d2.open('spam0.txt')
Traceback (most recent call last):
  File "<pyshell#165>", line 1, in <module>
    d2.open('spam0.txt')
AttributeError: '_io.TextIOWrapper' object has no attribute 'open'
>>> d2 =open('spam0.txt')
>>> d2
<_io.TextIOWrapper name='spam0.txt' mode='r' encoding='cp1252'>
>>> d2.read()
''
>>> d2 = open('spam0.txt','w')
>>> d2.writelines('hello there,\nthis is a test using python idle,\nmanipulating files')
>>> d2.open('spam0.txt')
Traceback (most recent call last):
  File "<pyshell#171>", line 1, in <module>
    d2.open('spam0.txt')
AttributeError: '_io.TextIOWrapper' object has no attribute 'open'
>>> d2 =open('spam0.txt')
>>> d2.readlines()
['hello there,\n', 'this is a test using python idle,\n', 'manipulating files']
>>> ## can't use read when in write mode
>>> d2
<_io.TextIOWrapper name='spam0.txt' mode='r' encoding='cp1252'>
>>> x
WindowsPath('C:/Users/Alex/AppData/Local/Programs/Python/Python39/Workspace/ATBS/Testing Files')
>>> Path.cwd()
WindowsPath('C:/Users/Alex/AppData/Local/Programs/Python/Python39/Workspace/ATBS/Testing Files')
>>> import shelve
>>> sf = shelve.open('shelveTest')
>>> ppl = ['alex','abby','millie']
>>> sf['ppl'] = ppl
>>> sf.close()
>>> sf=shelve.open('shelveTest')
>>> type(sf)
<class 'shelve.DbfilenameShelf'>
>>> sf['ppl']
['alex', 'abby', 'millie']
>>> sf['ppl'].append('lulu')
>>> sf
<shelve.DbfilenameShelf object at 0x0000003437970640>
>>> sf['ppl']
['alex', 'abby', 'millie']
>>> ppl = sf['plpl']
Traceback (most recent call last):
  File "C:\Users\Alex\AppData\Local\Programs\Python\Python39\lib\shelve.py", line 111, in __getitem__
    value = self.cache[key]
KeyError: 'plpl'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#189>", line 1, in <module>
    ppl = sf['plpl']
  File "C:\Users\Alex\AppData\Local\Programs\Python\Python39\lib\shelve.py", line 113, in __getitem__
    f = BytesIO(self.dict[key.encode(self.keyencoding)])
  File "C:\Users\Alex\AppData\Local\Programs\Python\Python39\lib\dbm\dumb.py", line 147, in __getitem__
    pos, siz = self._index[key]     # may raise KeyError
KeyError: b'plpl'
>>> ppl = sf['ppl']
>>> ppl
['alex', 'abby', 'millie']
>>> ppl.append('lulu')
>>> ppl
['alex', 'abby', 'millie', 'lulu']
>>> sf['ppl'] = ppl
>>> sf['ppl']
['alex', 'abby', 'millie', 'lulu']
>>> sf.close()
>>> sf
<shelve.DbfilenameShelf object at 0x0000003437970640>
>>> for i in sf:
	print(i)

	
Traceback (most recent call last):
  File "<pyshell#200>", line 1, in <module>
    for i in sf:
  File "C:\Users\Alex\AppData\Local\Programs\Python\Python39\lib\shelve.py", line 95, in __iter__
    for k in self.dict.keys():
  File "C:\Users\Alex\AppData\Local\Programs\Python\Python39\lib\shelve.py", line 70, in closed
    raise ValueError('invalid operation on closed shelf')
ValueError: invalid operation on closed shelf
>>> for i in sf['ppl']:
	print(i)

	
Traceback (most recent call last):
  File "C:\Users\Alex\AppData\Local\Programs\Python\Python39\lib\shelve.py", line 111, in __getitem__
    value = self.cache[key]
KeyError: 'ppl'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#203>", line 1, in <module>
    for i in sf['ppl']:
  File "C:\Users\Alex\AppData\Local\Programs\Python\Python39\lib\shelve.py", line 113, in __getitem__
    f = BytesIO(self.dict[key.encode(self.keyencoding)])
  File "C:\Users\Alex\AppData\Local\Programs\Python\Python39\lib\shelve.py", line 70, in closed
    raise ValueError('invalid operation on closed shelf')
ValueError: invalid operation on closed shelf
>>> sf = shelve.open('shelveTest')
>>> sf
<shelve.DbfilenameShelf object at 0x00000034379708E0>
>>> for i in sf['ppl']:
	print(i)

	
alex
abby
millie
lulu
>>> sf['ppl'].append('frank')
>>> sf['ppl']
['alex', 'abby', 'millie', 'lulu']
>>> sf.close()
>>> print(sf)
<shelve.DbfilenameShelf object at 0x00000034379708E0>
>>> import pyinputplus
>>> import pyinputplus as pyip
>>> pyip.help
Traceback (most recent call last):
  File "<pyshell#214>", line 1, in <module>
    pyip.help
AttributeError: module 'pyinputplus' has no attribute 'help'
>>> pyip.help()
Traceback (most recent call last):
  File "<pyshell#215>", line 1, in <module>
    pyip.help()
AttributeError: module 'pyinputplus' has no attribute 'help'
>>> help(pyip)

>>> 13/2
6.5
>>> 
= RESTART: C:/Users/Alex/AppData/Local/Programs/Python/Python39/Workspace/Small Projects/binaryConverter.py
12
>>> 
= RESTART: C:/Users/Alex/AppData/Local/Programs/Python/Python39/Workspace/Small Projects/binaryConverter.py
12
>>> 
= RESTART: C:/Users/Alex/AppData/Local/Programs/Python/Python39/Workspace/Small Projects/binaryConverter.py
12
Traceback (most recent call last):
  File "C:/Users/Alex/AppData/Local/Programs/Python/Python39/Workspace/Small Projects/binaryConverter.py", line 15, in <module>
    binaryConv(num, 0)
  File "C:/Users/Alex/AppData/Local/Programs/Python/Python39/Workspace/Small Projects/binaryConverter.py", line 9, in binaryConv
    holdingVal.append(str(rem))
AttributeError: 'int' object has no attribute 'append'
>>> 
= RESTART: C:/Users/Alex/AppData/Local/Programs/Python/Python39/Workspace/Small Projects/binaryConverter.py
12
0 6
>>> 
= RESTART: C:/Users/Alex/AppData/Local/Programs/Python/Python39/Workspace/Small Projects/binaryConverter.py
12
6 0
>>> 
= RESTART: C:/Users/Alex/AppData/Local/Programs/Python/Python39/Workspace/Small Projects/binaryConverter.py
13
6 1
1
>>> 
= RESTART: C:/Users/Alex/AppData/Local/Programs/Python/Python39/Workspace/Small Projects/binaryConverter.py
12
6 0

3 0

1 1
1
0 1
11
>>> 
= RESTART: C:/Users/Alex/AppData/Local/Programs/Python/Python39/Workspace/Small Projects/binaryConverter.py
13
6 1
1
3 0
1
1 1
11
0 1
111
>>> 
= RESTART: C:/Users/Alex/AppData/Local/Programs/Python/Python39/Workspace/Small Projects/binaryConverter.py
13
6 1
1
Traceback (most recent call last):
  File "C:/Users/Alex/AppData/Local/Programs/Python/Python39/Workspace/Small Projects/binaryConverter.py", line 23, in <module>
    output = binaryConv(num, runningTotal)
  File "C:/Users/Alex/AppData/Local/Programs/Python/Python39/Workspace/Small Projects/binaryConverter.py", line 18, in binaryConv
    binaryConv(quotient, 0, runningTotal)
TypeError: binaryConv() takes 2 positional arguments but 3 were given
>>> 
= RESTART: C:/Users/Alex/AppData/Local/Programs/Python/Python39/Workspace/Small Projects/binaryConverter.py
13
6 1
1
3 0
1
1 1
11
0 1
111
>>> 
= RESTART: C:/Users/Alex/AppData/Local/Programs/Python/Python39/Workspace/Small Projects/binaryConverter.py
13
6 1
3 0
1 1
0 1
>>> 
= RESTART: C:/Users/Alex/AppData/Local/Programs/Python/Python39/Workspace/Small Projects/binaryConverter.py
13
6 1
1
3 0
1 1
11
0 1
111
>>> 
= RESTART: C:/Users/Alex/AppData/Local/Programs/Python/Python39/Workspace/Small Projects/binaryConverter.py
13
6 1
running total = 1
3 0
1 1
running total = 11
0 1
running total = 111
>>> 
= RESTART: C:/Users/Alex/AppData/Local/Programs/Python/Python39/Workspace/Small Projects/binaryConverter.py
13
6 1
running total = 1
3 0
running total = 10
1 1
running total = 101
0 1
running total = 1011
>>> 
= RESTART: C:/Users/Alex/AppData/Local/Programs/Python/Python39/Workspace/Small Projects/binaryConverter.py
13
6 1
running total = 1
3 0
running total = 01
1 1
running total = 101
0 1
running total = 1101
>>> 
= RESTART: C:/Users/Alex/AppData/Local/Programs/Python/Python39/Workspace/Small Projects/binaryConverter.py
174
87 0
running total = 0
43 1
running total = 10
21 1
running total = 110
10 1
running total = 1110
5 0
running total = 01110
2 1
running total = 101110
1 0
running total = 0101110
0 1
running total = 10101110
>>> 