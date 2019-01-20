Python 3.6.7 (default, Oct 22 2018, 11:32:17) 
[GCC 8.2.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> spam ={}
>>> spam.setdefault('color', 'black')
'black'
>>> spam
{'color': 'black'}
>>> spam['color'] = 'green'
>>> spam
{'color': 'green'}
>>> spam.update('color':'purple')
SyntaxError: invalid syntax
>>> spam.update('color': 'purple')
SyntaxError: invalid syntax
>>> spam.update({'color': 'purple'})
>>> spam
{'color': 'purple'}
>>> spam.update({'name': 'kal'})
>>> spam
{'color': 'purple', 'name': 'kal'}
>>> spam.update({'name': 'Jame', 'color':'pink'})
>>> spam
{'color': 'pink', 'name': 'Jame'}
>>> spam.pop('name')
'Jame'
>>> spam
{'color': 'pink'}
>>> spam.pop(0)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    spam.pop(0)
KeyError: 0
>>> spam.pop[0]
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    spam.pop[0]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> spam
{'color': 'pink'}
>>>  spam.update({'name': 'Jame', 'color':'pink'})
SyntaxError: unexpected indent
>>> spam.update({'name': 'Jame', 'color':'pink'})
>>> spam
{'color': 'pink', 'name': 'Jame'}
>>> spam.update('color':'purple')
SyntaxError: invalid syntax
>>> 
>>> 
>>> 
=============================== RESTART: Shell ===============================
>>> 
 RESTART: /home/kalibur/kal-labs/python/automate_python/fantasyGameInventory.py 
dict_items([('rope', 1), ('torch', 6), ('gold coin', 42), ('dagger', 1), ('arrow', 12)])
>>> 
 RESTART: /home/kalibur/kal-labs/python/automate_python/fantasyGameInventory.py 
Traceback (most recent call last):
  File "/home/kalibur/kal-labs/python/automate_python/fantasyGameInventory.py", line 11, in <module>
    pprint(inventory.items())
NameError: name 'pprint' is not defined
>>> 
 RESTART: /home/kalibur/kal-labs/python/automate_python/fantasyGameInventory.py 
dict_items([('rope', 1), ('torch', 6), ('gold coin', 42), ('dagger', 1), ('arrow', 12)])
Traceback (most recent call last):
  File "/home/kalibur/kal-labs/python/automate_python/fantasyGameInventory.py", line 19, in <module>
    displayInventory()
  File "/home/kalibur/kal-labs/python/automate_python/fantasyGameInventory.py", line 15, in displayInventory
    print(value + item)
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> 
 RESTART: /home/kalibur/kal-labs/python/automate_python/fantasyGameInventory.py 
dict_items([('rope', 1), ('torch', 6), ('gold coin', 42), ('dagger', 1), ('arrow', 12)])
Traceback (most recent call last):
  File "/home/kalibur/kal-labs/python/automate_python/fantasyGameInventory.py", line 19, in <module>
    displayInventory()
  File "/home/kalibur/kal-labs/python/automate_python/fantasyGameInventory.py", line 15, in displayInventory
    print(value + ' ' + item)
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> 
 RESTART: /home/kalibur/kal-labs/python/automate_python/fantasyGameInventory.py 
dict_items([('rope', 1), ('torch', 6), ('gold coin', 42), ('dagger', 1), ('arrow', 12)])
1 rope
6 torch
42 gold coin
1 dagger
12 arrow
>>> 
 RESTART: /home/kalibur/kal-labs/python/automate_python/fantasyGameInventory.py 
1 rope
6 torch
42 gold coin
1 dagger
12 arrow
>>> 
 RESTART: /home/kalibur/kal-labs/python/automate_python/fantasyGameInventory.py 
1 rope
Traceback (most recent call last):
  File "/home/kalibur/kal-labs/python/automate_python/fantasyGameInventory.py", line 21, in <module>
    displayInventory()
  File "/home/kalibur/kal-labs/python/automate_python/fantasyGameInventory.py", line 16, in displayInventory
    totalItems = totalItems + value
UnboundLocalError: local variable 'totalItems' referenced before assignment
>>> 
 RESTART: /home/kalibur/kal-labs/python/automate_python/fantasyGameInventory.py 
1 rope
>>> 
 RESTART: /home/kalibur/kal-labs/python/automate_python/fantasyGameInventory.py 
1 rope
>>> 
 RESTART: /home/kalibur/kal-labs/python/automate_python/fantasyGameInventory.py 
1 rope
6 torch
42 gold coin
1 dagger
12 arrow
>>> 
 RESTART: /home/kalibur/kal-labs/python/automate_python/fantasyGameInventory.py 
1 rope
6 torch
42 gold coin
1 dagger
12 arrow
Traceback (most recent call last):
  File "/home/kalibur/kal-labs/python/automate_python/fantasyGameInventory.py", line 23, in <module>
    print('Total number of items: ' + totalItems)
NameError: name 'totalItems' is not defined
>>> 
 RESTART: /home/kalibur/kal-labs/python/automate_python/fantasyGameInventory.py 
1 rope
Traceback (most recent call last):
  File "/home/kalibur/kal-labs/python/automate_python/fantasyGameInventory.py", line 22, in <module>
    displayInventory()
  File "/home/kalibur/kal-labs/python/automate_python/fantasyGameInventory.py", line 17, in displayInventory
    totalItems = totalItems + value
UnboundLocalError: local variable 'totalItems' referenced before assignment
>>> 
 RESTART: /home/kalibur/kal-labs/python/automate_python/fantasyGameInventory.py 
1 rope
Traceback (most recent call last):
  File "/home/kalibur/kal-labs/python/automate_python/fantasyGameInventory.py", line 22, in <module>
    print(displayInventory())
  File "/home/kalibur/kal-labs/python/automate_python/fantasyGameInventory.py", line 17, in displayInventory
    totalItems = totalItems + value
UnboundLocalError: local variable 'totalItems' referenced before assignment
>>> 
 RESTART: /home/kalibur/kal-labs/python/automate_python/fantasyGameInventory.py 
1 rope
6 torch
42 gold coin
1 dagger
12 arrow
62
Total number of items: 
>>> 
 RESTART: /home/kalibur/kal-labs/python/automate_python/fantasyGameInventory.py 
1 rope
6 torch
42 gold coin
1 dagger
12 arrow
62
1 rope
6 torch
42 gold coin
1 dagger
12 arrow
Traceback (most recent call last):
  File "/home/kalibur/kal-labs/python/automate_python/fantasyGameInventory.py", line 25, in <module>
    print('Total number of items: ' + (displayInventory()))
TypeError: must be str, not int
>>> 
 RESTART: /home/kalibur/kal-labs/python/automate_python/fantasyGameInventory.py 
1 rope
6 torch
42 gold coin
1 dagger
12 arrow
62
1 rope
6 torch
42 gold coin
1 dagger
12 arrow
Total number of items: 62
>>> 
 RESTART: /home/kalibur/kal-labs/python/automate_python/fantasyGameInventory.py 
111 rope
6 torch
42 gold coin
1 dagger
12 arrow
Total number of items: 172
>>> import system
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    import system
ModuleNotFoundError: No module named 'system'
>>> import os
>>> help(os)

>>> dir(os)

>>> dir(os)
['CLD_CONTINUED', 'CLD_DUMPED', 'CLD_EXITED', 'CLD_TRAPPED', 'DirEntry', 'EX_CANTCREAT', 'EX_CONFIG', 'EX_DATAERR', 'EX_IOERR', 'EX_NOHOST', 'EX_NOINPUT', 'EX_NOPERM', 'EX_NOUSER', 'EX_OK', 'EX_OSERR', 'EX_OSFILE', 'EX_PROTOCOL', 'EX_SOFTWARE', 'EX_TEMPFAIL', 'EX_UNAVAILABLE', 'EX_USAGE', 'F_LOCK', 'F_OK', 'F_TEST', 'F_TLOCK', 'F_ULOCK', 'GRND_NONBLOCK', 'GRND_RANDOM', 'MutableMapping', 'NGROUPS_MAX', 'O_ACCMODE', 'O_APPEND', 'O_ASYNC', 'O_CLOEXEC', 'O_CREAT', 'O_DIRECT', 'O_DIRECTORY', 'O_DSYNC', 'O_EXCL', 'O_LARGEFILE', 'O_NDELAY', 'O_NOATIME', 'O_NOCTTY', 'O_NOFOLLOW', 'O_NONBLOCK', 'O_PATH', 'O_RDONLY', 'O_RDWR', 'O_RSYNC', 'O_SYNC', 'O_TMPFILE', 'O_TRUNC', 'O_WRONLY', 'POSIX_FADV_DONTNEED', 'POSIX_FADV_NOREUSE', 'POSIX_FADV_NORMAL', 'POSIX_FADV_RANDOM', 'POSIX_FADV_SEQUENTIAL', 'POSIX_FADV_WILLNEED', 'PRIO_PGRP', 'PRIO_PROCESS', 'PRIO_USER', 'P_ALL', 'P_NOWAIT', 'P_NOWAITO', 'P_PGID', 'P_PID', 'P_WAIT', 'PathLike', 'RTLD_DEEPBIND', 'RTLD_GLOBAL', 'RTLD_LAZY', 'RTLD_LOCAL', 'RTLD_NODELETE', 'RTLD_NOLOAD', 'RTLD_NOW', 'R_OK', 'SCHED_BATCH', 'SCHED_FIFO', 'SCHED_IDLE', 'SCHED_OTHER', 'SCHED_RESET_ON_FORK', 'SCHED_RR', 'SEEK_CUR', 'SEEK_DATA', 'SEEK_END', 'SEEK_HOLE', 'SEEK_SET', 'ST_APPEND', 'ST_MANDLOCK', 'ST_NOATIME', 'ST_NODEV', 'ST_NODIRATIME', 'ST_NOEXEC', 'ST_NOSUID', 'ST_RDONLY', 'ST_RELATIME', 'ST_SYNCHRONOUS', 'ST_WRITE', 'TMP_MAX', 'WCONTINUED', 'WCOREDUMP', 'WEXITED', 'WEXITSTATUS', 'WIFCONTINUED', 'WIFEXITED', 'WIFSIGNALED', 'WIFSTOPPED', 'WNOHANG', 'WNOWAIT', 'WSTOPPED', 'WSTOPSIG', 'WTERMSIG', 'WUNTRACED', 'W_OK', 'XATTR_CREATE', 'XATTR_REPLACE', 'XATTR_SIZE_MAX', 'X_OK', '_Environ', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_execvpe', '_exists', '_exit', '_fspath', '_fwalk', '_get_exports_list', '_putenv', '_spawnvef', '_unsetenv', '_wrap_close', 'abc', 'abort', 'access', 'altsep', 'chdir', 'chmod', 'chown', 'chroot', 'close', 'closerange', 'confstr', 'confstr_names', 'cpu_count', 'ctermid', 'curdir', 'defpath', 'device_encoding', 'devnull', 'dup', 'dup2', 'environ', 'environb', 'errno', 'error', 'execl', 'execle', 'execlp', 'execlpe', 'execv', 'execve', 'execvp', 'execvpe', 'extsep', 'fchdir', 'fchmod', 'fchown', 'fdatasync', 'fdopen', 'fork', 'forkpty', 'fpathconf', 'fsdecode', 'fsencode', 'fspath', 'fstat', 'fstatvfs', 'fsync', 'ftruncate', 'fwalk', 'get_blocking', 'get_exec_path', 'get_inheritable', 'get_terminal_size', 'getcwd', 'getcwdb', 'getegid', 'getenv', 'getenvb', 'geteuid', 'getgid', 'getgrouplist', 'getgroups', 'getloadavg', 'getlogin', 'getpgid', 'getpgrp', 'getpid', 'getppid', 'getpriority', 'getrandom', 'getresgid', 'getresuid', 'getsid', 'getuid', 'getxattr', 'initgroups', 'isatty', 'kill', 'killpg', 'lchown', 'linesep', 'link', 'listdir', 'listxattr', 'lockf', 'lseek', 'lstat', 'major', 'makedev', 'makedirs', 'minor', 'mkdir', 'mkfifo', 'mknod', 'name', 'nice', 'open', 'openpty', 'pardir', 'path', 'pathconf', 'pathconf_names', 'pathsep', 'pipe', 'pipe2', 'popen', 'posix_fadvise', 'posix_fallocate', 'pread', 'putenv', 'pwrite', 'read', 'readlink', 'readv', 'remove', 'removedirs', 'removexattr', 'rename', 'renames', 'replace', 'rmdir', 'scandir', 'sched_get_priority_max', 'sched_get_priority_min', 'sched_getaffinity', 'sched_getparam', 'sched_getscheduler', 'sched_param', 'sched_rr_get_interval', 'sched_setaffinity', 'sched_setparam', 'sched_setscheduler', 'sched_yield', 'sendfile', 'sep', 'set_blocking', 'set_inheritable', 'setegid', 'seteuid', 'setgid', 'setgroups', 'setpgid', 'setpgrp', 'setpriority', 'setregid', 'setresgid', 'setresuid', 'setreuid', 'setsid', 'setuid', 'setxattr', 'spawnl', 'spawnle', 'spawnlp', 'spawnlpe', 'spawnv', 'spawnve', 'spawnvp', 'spawnvpe', 'st', 'stat', 'stat_float_times', 'stat_result', 'statvfs', 'statvfs_result', 'strerror', 'supports_bytes_environ', 'supports_dir_fd', 'supports_effective_ids', 'supports_fd', 'supports_follow_symlinks', 'symlink', 'sync', 'sys', 'sysconf', 'sysconf_names', 'system', 'tcgetpgrp', 'tcsetpgrp', 'terminal_size', 'times', 'times_result', 'truncate', 'ttyname', 'umask', 'uname', 'uname_result', 'unlink', 'unsetenv', 'urandom', 'utime', 'wait', 'wait3', 'wait4', 'waitid', 'waitid_result', 'waitpid', 'walk', 'write', 'writev']
>>> os.fstat
<built-in function fstat>
>>> os.fstat('/')
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    os.fstat('/')
TypeError: an integer is required (got type str)
>>> os.fstat()
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    os.fstat()
TypeError: Required argument 'fd' (pos 1) not found
>>> os.uptime()
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    os.uptime()
AttributeError: module 'os' has no attribute 'uptime'
>>> os.uname()
posix.uname_result(sysname='Linux', nodename='kal-XT3', release='4.15.0-39-generic', version='#42-Ubuntu SMP Tue Oct 23 15:48:01 UTC 2018', machine='x86_64')
>>> os.utime()
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    os.utime()
TypeError: Required argument 'path' (pos 1) not found
>>> os.utime('/')
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    os.utime('/')
PermissionError: [Errno 13] Permission denied
>>> os.utime('/)
	     
SyntaxError: EOL while scanning string literal
>>> os.utime(/)
	     
SyntaxError: invalid syntax
>>> 
 RESTART: /home/kalibur/kal-labs/python/automate_python/fantasyGameInventory.py 
111 rope
6 torch
42 gold coin
1 dagger
12 arrow
Total number of items: 172
>>> 
 RESTART: /home/kalibur/kal-labs/python/automate_python/fantasyGameInventory.py 
{'rope': 111, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
>>> 
 RESTART: /home/kalibur/kal-labs/python/automate_python/fantasyGameInventory.py 
{'rope': 111, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
>>> 
 RESTART: /home/kalibur/kal-labs/python/automate_python/fantasyGameInventory.py 
{'rope': 111, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
Traceback (most recent call last):
  File "/home/kalibur/kal-labs/python/automate_python/fantasyGameInventory.py", line 20, in <module>
    addToInventory()
TypeError: addToInventory() missing 2 required positional arguments: 'inventory' and 'addItems'
>>> 
 RESTART: /home/kalibur/kal-labs/python/automate_python/fantasyGameInventory.py 
{'rope': 111, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
What item would you like to add? 
>>> hello
	     
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    hello
NameError: name 'hello' is not defined
>>> 
 RESTART: /home/kalibur/kal-labs/python/automate_python/fantasyGameInventory.py 
{'rope': 111, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
['gold coin', 'rope', 'dagger', 'gold coin', 'ruby']
What item would you like to add? 
>>> 
[DEBUG ON]
>>> 
 RESTART: /home/kalibur/kal-labs/python/automate_python/fantasyGameInventory.py 

 RESTART: /home/kalibur/kal-labs/python/automate_python/fantasyGameInventory.py 

 RESTART: /home/kalibur/kal-labs/python/automate_python/fantasyGameInventory.py 
[DEBUG ON]
>>> 
 RESTART: /home/kalibur/kal-labs/python/automate_python/fantasyGameInventory.py 
{'rope': 111, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
Traceback (most recent call last):
  File "/home/kalibur/kal-labs/python/automate_python/fantasyGameInventory.py", line 26, in <module>
    print(countLoot())
  File "/home/kalibur/kal-labs/python/automate_python/fantasyGameInventory.py", line 16, in countLoot
    z == z + i
NameError: name 'z' is not defined
[DEBUG ON]
>>> 
[DEBUG OFF]
>>> 
 RESTART: /home/kalibur/kal-labs/python/automate_python/fantasyGameInventory.py 
{'rope': 111, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
Traceback (most recent call last):
  File "/home/kalibur/kal-labs/python/automate_python/fantasyGameInventory.py", line 26, in <module>
    print(countLoot())
  File "/home/kalibur/kal-labs/python/automate_python/fantasyGameInventory.py", line 16, in countLoot
    z == z + i
NameError: name 'z' is not defined
>>> 
 RESTART: /home/kalibur/kal-labs/python/automate_python/fantasyGameInventory.py 
{'rope': 111, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
Traceback (most recent call last):
  File "/home/kalibur/kal-labs/python/automate_python/fantasyGameInventory.py", line 27, in <module>
    print(countLoot())
  File "/home/kalibur/kal-labs/python/automate_python/fantasyGameInventory.py", line 17, in countLoot
    z == z + i
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> 
 RESTART: /home/kalibur/kal-labs/python/automate_python/fantasyGameInventory.py 
{'rope': 111, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
Traceback (most recent call last):
  File "/home/kalibur/kal-labs/python/automate_python/fantasyGameInventory.py", line 27, in <module>
    print(countLoot())
  File "/home/kalibur/kal-labs/python/automate_python/fantasyGameInventory.py", line 15, in countLoot
    for i in dragonLoot():
TypeError: 'list' object is not callable
>>> 
 RESTART: /home/kalibur/kal-labs/python/automate_python/fantasyGameInventory.py 
{'rope': 111, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
['gold coin', 'rope', 'dagger', 'gold coin', 'ruby']
Traceback (most recent call last):
  File "/home/kalibur/kal-labs/python/automate_python/fantasyGameInventory.py", line 28, in <module>
    print(countLoot())
  File "/home/kalibur/kal-labs/python/automate_python/fantasyGameInventory.py", line 16, in countLoot
    for i in dragonLoot():
TypeError: 'list' object is not callable
>>> 
 RESTART: /home/kalibur/kal-labs/python/automate_python/fantasyGameInventory.py 
{'rope': 111, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
['gold coin', 'rope', 'dagger', 'gold coin', 'ruby']
Traceback (most recent call last):
  File "/home/kalibur/kal-labs/python/automate_python/fantasyGameInventory.py", line 27, in <module>
    print(countLoot())
  File "/home/kalibur/kal-labs/python/automate_python/fantasyGameInventory.py", line 16, in countLoot
    for i in dragonLoot():
TypeError: 'list' object is not callable
>>> 
 RESTART: /home/kalibur/kal-labs/python/automate_python/fantasyGameInventory.py 
{'rope': 111, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
['gold coin', 'rope', 'dagger', 'gold coin', 'ruby']
Traceback (most recent call last):
  File "/home/kalibur/kal-labs/python/automate_python/fantasyGameInventory.py", line 27, in <module>
    print(countLoot())
  File "/home/kalibur/kal-labs/python/automate_python/fantasyGameInventory.py", line 16, in countLoot
    for i in (len.dragonLoot()):
AttributeError: 'builtin_function_or_method' object has no attribute 'dragonLoot'
>>> 
 RESTART: /home/kalibur/kal-labs/python/automate_python/fantasyGameInventory.py 
{'rope': 111, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
Traceback (most recent call last):
  File "/home/kalibur/kal-labs/python/automate_python/fantasyGameInventory.py", line 26, in <module>
    print(countLoot())
  File "/home/kalibur/kal-labs/python/automate_python/fantasyGameInventory.py", line 15, in countLoot
    for i in len.dragonLoot():
AttributeError: 'builtin_function_or_method' object has no attribute 'dragonLoot'
>>> 
 RESTART: /home/kalibur/kal-labs/python/automate_python/fantasyGameInventory.py 
Traceback (most recent call last):
  File "/home/kalibur/kal-labs/python/automate_python/fantasyGameInventory.py", line 24, in <module>
    print(len.dragonLoot())
AttributeError: 'builtin_function_or_method' object has no attribute 'dragonLoot'
>>> 
 RESTART: /home/kalibur/kal-labs/python/automate_python/fantasyGameInventory.py 
Traceback (most recent call last):
  File "/home/kalibur/kal-labs/python/automate_python/fantasyGameInventory.py", line 24, in <module>
    print(str(len.dragonLoot()))
AttributeError: 'builtin_function_or_method' object has no attribute 'dragonLoot'
>>> dragonLoot = ['gold coin', 'rope' , 'dagger', 'gold coin', 'ruby' ]

>>> dragonLoot
	     
['gold coin', 'rope', 'dagger', 'gold coin', 'ruby']
>>> len.dragonLoot
	     
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    len.dragonLoot
AttributeError: 'builtin_function_or_method' object has no attribute 'dragonLoot'
>>> len.dragonLoot()
	     
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    len.dragonLoot()
AttributeError: 'builtin_function_or_method' object has no attribute 'dragonLoot'
>>> len(dragonLoot)
	     
5
>>> 
 RESTART: /home/kalibur/kal-labs/python/automate_python/fantasyGameInventory.py 
5
{'rope': 111, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
Traceback (most recent call last):
  File "/home/kalibur/kal-labs/python/automate_python/fantasyGameInventory.py", line 26, in <module>
    print(countLoot())
  File "/home/kalibur/kal-labs/python/automate_python/fantasyGameInventory.py", line 15, in countLoot
    for i in len(dragonLoot):
TypeError: 'int' object is not iterable
>>> 
 RESTART: /home/kalibur/kal-labs/python/automate_python/fantasyGameInventory.py 
5
{'rope': 111, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
Traceback (most recent call last):
  File "/home/kalibur/kal-labs/python/automate_python/fantasyGameInventory.py", line 27, in <module>
    print(countLoot())
  File "/home/kalibur/kal-labs/python/automate_python/fantasyGameInventory.py", line 15, in countLoot
    for i in len(dragonLoot):
TypeError: 'int' object is not iterable
>>> 
 RESTART: /home/kalibur/kal-labs/python/automate_python/fantasyGameInventory.py 
5
{'rope': 111, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
Traceback (most recent call last):
  File "/home/kalibur/kal-labs/python/automate_python/fantasyGameInventory.py", line 27, in <module>
    print(countLoot())
  File "/home/kalibur/kal-labs/python/automate_python/fantasyGameInventory.py", line 15, in countLoot
    for i in len(dragonLoot):
TypeError: 'int' object is not iterable
>>> dragonLoot
	     
['gold coin', 'rope', 'dagger', 'gold coin', 'ruby']
>>> dragonLoot[0]
	     
'gold coin'
>>> 
 RESTART: /home/kalibur/kal-labs/python/automate_python/fantasyGameInventory.py 
5
{'rope': 111, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
Traceback (most recent call last):
  File "/home/kalibur/kal-labs/python/automate_python/fantasyGameInventory.py", line 27, in <module>
    print(countLoot())
  File "/home/kalibur/kal-labs/python/automate_python/fantasyGameInventory.py", line 16, in countLoot
    print(dragonLoot[i])
TypeError: list indices must be integers or slices, not str
>>> 
 RESTART: /home/kalibur/kal-labs/python/automate_python/fantasyGameInventory.py 
5
{'rope': 111, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
Traceback (most recent call last):
  File "/home/kalibur/kal-labs/python/automate_python/fantasyGameInventory.py", line 27, in <module>
    print(countLoot())
  File "/home/kalibur/kal-labs/python/automate_python/fantasyGameInventory.py", line 15, in countLoot
    for i in len(dragonLoot):
TypeError: 'int' object is not iterable
>>> 
[DEBUG ON]
>>> 
 RESTART: /home/kalibur/kal-labs/python/automate_python/fantasyGameInventory.py 

 RESTART: /home/kalibur/kal-labs/python/automate_python/fantasyGameInventory.py 
[DEBUG ON]
>>> 
 RESTART: /home/kalibur/kal-labs/python/automate_python/fantasyGameInventory.py 
[DEBUG OFF]
>>> 
>>> 
 RESTART: /home/kalibur/kal-labs/python/automate_python/fantasyGameInventory.py 
{'rope': 111, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
Traceback (most recent call last):
  File "/home/kalibur/kal-labs/python/automate_python/fantasyGameInventory.py", line 27, in <module>
    print(countLoot())
  File "/home/kalibur/kal-labs/python/automate_python/fantasyGameInventory.py", line 15, in countLoot
    for i in len(dragonLoot):
TypeError: 'int' object is not iterable
>>> 
 RESTART: /home/kalibur/kal-labs/python/automate_python/fantasyGameInventory.py 
{'rope': 111, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
0
['gold coin', 'rope', 'dagger', 'gold coin', 'ruby']
What item would you like to add? 
>>> 
 RESTART: /home/kalibur/kal-labs/python/automate_python/fantasyGameInventory.py 
0
What item would you like to add? 
>>> 
 RESTART: /home/kalibur/kal-labs/python/automate_python/fantasyGameInventory.py 
Traceback (most recent call last):
  File "/home/kalibur/kal-labs/python/automate_python/fantasyGameInventory.py", line 27, in <module>
    print(countLoot())
  File "/home/kalibur/kal-labs/python/automate_python/fantasyGameInventory.py", line 16, in countLoot
    print(dragonLoot[i])
NameError: name 'i' is not defined
>>> 
 RESTART: /home/kalibur/kal-labs/python/automate_python/fantasyGameInventory.py 
gold coin
rope
dagger
gold coin
ruby
5
What item would you like to add? 
>>> 
 RESTART: /home/kalibur/kal-labs/python/automate_python/fantasyGameInventory.py 
gold coin
rope
dagger
gold coin
ruby
5
What item would you like to add? 
>>> 
 RESTART: /home/kalibur/kal-labs/python/automate_python/fantasyGameInventory.py 
Traceback (most recent call last):
  File "/home/kalibur/kal-labs/python/automate_python/fantasyGameInventory.py", line 28, in <module>
    print(countLoot())
  File "/home/kalibur/kal-labs/python/automate_python/fantasyGameInventory.py", line 16, in countLoot
    print(dragonLoot[z])
NameError: name 'z' is not defined
>>> 
 RESTART: /home/kalibur/kal-labs/python/automate_python/fantasyGameInventory.py 
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
Traceback (most recent call last):
  File "/home/kalibur/kal-labs/python/automate_python/fantasyGameInventory.py", line 28, in <module>
    print(countLoot())
  File "/home/kalibur/kal-labs/python/automate_python/fantasyGameInventory.py", line 16, in countLoot
    print(dragonLoot[count])
KeyboardInterrupt
>>> 
 RESTART: /home/kalibur/kal-labs/python/automate_python/fantasyGameInventory.py 
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
Traceback (most recent call last):
  File "/home/kalibur/kal-labs/python/automate_python/fantasyGameInventory.py", line 28, in <module>
    print(countLoot())
  File "/home/kalibur/kal-labs/python/automate_python/fantasyGameInventory.py", line 16, in countLoot
    print(dragonLoot[count])
KeyboardInterrupt
>>> 
 RESTART: /home/kalibur/kal-labs/python/automate_python/fantasyGameInventory.py 
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coin
gold coinTraceback (most recent call last):
  File "/home/kalibur/kal-labs/python/automate_python/fantasyGameInventory.py", line 28, in <module>
    print(countLoot())
  File "/home/kalibur/kal-labs/python/automate_python/fantasyGameInventory.py", line 16, in countLoot
    print(dragonLoot[count])
KeyboardInterrupt
>>> 
 RESTART: /home/kalibur/kal-labs/python/automate_python/fantasyGameInventory.py 
gold coin
rope
dagger
gold coin
ruby
Traceback (most recent call last):
  File "/home/kalibur/kal-labs/python/automate_python/fantasyGameInventory.py", line 28, in <module>
    print(countLoot())
  File "/home/kalibur/kal-labs/python/automate_python/fantasyGameInventory.py", line 18, in countLoot
    return lootStuff
NameError: name 'lootStuff' is not defined
>>> 
 RESTART: /home/kalibur/kal-labs/python/automate_python/fantasyGameInventory.py 
gold coin
rope
dagger
gold coin
ruby
None
What item would you like to add? 
>>> 
 RESTART: /home/kalibur/kal-labs/python/automate_python/fantasyGameInventory.py 
gold coin
rope
dagger
gold coin
ruby
Traceback (most recent call last):
  File "/home/kalibur/kal-labs/python/automate_python/fantasyGameInventory.py", line 28, in <module>
    print(countLoot())
  File "/home/kalibur/kal-labs/python/automate_python/fantasyGameInventory.py", line 18, in countLoot
    return totLoot
NameError: name 'totLoot' is not defined
>>> 
 RESTART: /home/kalibur/kal-labs/python/automate_python/fantasyGameInventory.py 
gold coin
rope
dagger
gold coin
ruby
{'rope': 111, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
What item would you like to add? 
>>> 
 RESTART: /home/kalibur/kal-labs/python/automate_python/fantasyGameInventory.py 
Traceback (most recent call last):
  File "/home/kalibur/kal-labs/python/automate_python/fantasyGameInventory.py", line 31, in <module>
    print(countLoot())
  File "/home/kalibur/kal-labs/python/automate_python/fantasyGameInventory.py", line 16, in countLoot
    for item in dragonLoot():
TypeError: 'list' object is not callable
>>> 
 RESTART: /home/kalibur/kal-labs/python/automate_python/fantasyGameInventory.py 
Traceback (most recent call last):
  File "/home/kalibur/kal-labs/python/automate_python/fantasyGameInventory.py", line 30, in <module>
    print(countLoot())
  File "/home/kalibur/kal-labs/python/automate_python/fantasyGameInventory.py", line 17, in countLoot
    print(dragonLoot[count] + count)
TypeError: must be str, not int
>>> 
 RESTART: /home/kalibur/kal-labs/python/automate_python/fantasyGameInventory.py 
gold coin0
rope1
dagger2
gold coin3
ruby4
{'rope': 111, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
What item would you like to add? 
>>> 
 RESTART: /home/kalibur/kal-labs/python/automate_python/fantasyGameInventory.py 
gold coin 0
rope 1
dagger 2
gold coin 3
ruby 4
{'rope': 111, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
What item would you like to add? 
>>> 
 RESTART: /home/kalibur/kal-labs/python/automate_python/fantasyGameInventory.py 
gold coin => 0
rope => 1
dagger => 2
gold coin => 3
ruby => 4
{'rope': 111, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
What item would you like to add? 
>>> dragonLoot
	     
['gold coin', 'rope', 'dagger', 'gold coin', 'ruby']
>>> inv
	     
{'rope': 111, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
>>> inv.values['rope']
	     
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    inv.values['rope']
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> inv.values['rope':]
	     
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    inv.values['rope':]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> inv['rope':]
	     
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    inv['rope':]
TypeError: unhashable type: 'slice'
>>> inv
	     
{'rope': 111, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
>>> inv.items
	     
<built-in method items of dict object at 0x7fa559e49870>
>>> inv.items()
	     
dict_items([('rope', 111), ('torch', 6), ('gold coin', 42), ('dagger', 1), ('arrow', 12)])
>>> inv.items('rope')
	     
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    inv.items('rope')
TypeError: items() takes no arguments (1 given)
>>> inv.items()
	     
dict_items([('rope', 111), ('torch', 6), ('gold coin', 42), ('dagger', 1), ('arrow', 12)])
>>> inv.key()
	     
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    inv.key()
AttributeError: 'dict' object has no attribute 'key'
>>> inv.keys()
	     
dict_keys(['rope', 'torch', 'gold coin', 'dagger', 'arrow'])
>>> update.inv('rope': 20)
	     
SyntaxError: invalid syntax
>>> update.inv('rope', 20)
	     
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    update.inv('rope', 20)
NameError: name 'update' is not defined
>>> update.inv'rope', 20}
SyntaxError: invalid syntax
>>> update.inv{'rope', 20}
SyntaxError: invalid syntax
>>> update.inv['rope', 20]
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    update.inv['rope', 20]
NameError: name 'update' is not defined
>>> update.inv{'rope', 20}
SyntaxError: invalid syntax
>>> inv.update{'rope', 20 }
SyntaxError: invalid syntax
>>> inv.update['rope', 20 ]
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    inv.update['rope', 20 ]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> inv['rope'] = 20
>>> inv['rope']
20
>>> inv['rope'] = 20 + 1
>>> inv['rope']
21
>>> for i in inv():
	print(i)

	
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    for i in inv():
TypeError: 'dict' object is not callable
>>> for i in len(inv)():
	print(inv[i])

	
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    for i in len(inv)():
TypeError: 'int' object is not callable
>>> len(inv)
5
>>> print(inv[2])
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    print(inv[2])
KeyError: 2
>>> for i,z in inv():
	print(i + z )

	
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    for i,z in inv():
TypeError: 'dict' object is not callable
>>> for i,z in inv():
	print( i + str(z) )

	
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    for i,z in inv():
TypeError: 'dict' object is not callable
>>> 
 RESTART: /home/kalibur/kal-labs/python/automate_python/fantasyGameInventory.py 
gold coin => 0
rope => 1
dagger => 2
gold coin => 3
ruby => 4
{'rope': 111, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
What item would you like to add? 
>>> 
 RESTART: /home/kalibur/kal-labs/python/automate_python/fantasyGameInventory.py 
gold coin => 0
<built-in method values of dict object at 0x7f36e1973990>
rope => 1
<built-in method values of dict object at 0x7f36e1973990>
dagger => 2
<built-in method values of dict object at 0x7f36e1973990>
gold coin => 3
<built-in method values of dict object at 0x7f36e1973990>
ruby => 4
<built-in method values of dict object at 0x7f36e1973990>
{'rope': 111, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
What item would you like to add? 
>>> 
 RESTART: /home/kalibur/kal-labs/python/automate_python/fantasyGameInventory.py 
gold coin => 0
dict_values([111, 6, 42, 1, 12])
rope => 1
dict_values([111, 6, 42, 1, 12])
dagger => 2
dict_values([111, 6, 42, 1, 12])
gold coin => 3
dict_values([111, 6, 42, 1, 12])
ruby => 4
dict_values([111, 6, 42, 1, 12])
{'rope': 111, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
What item would you like to add? 
>>> inv
{'rope': 111, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
>>> for x, y in inv.items():
	print( x y)
	
SyntaxError: invalid syntax
>>> for x, y in inv.items():
	print( x + y)
