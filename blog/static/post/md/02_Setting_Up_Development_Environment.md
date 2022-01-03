# Cent OS 8에 pyenv + venv + Django 환경설정

## pyenv 설치

패키지 업데이트

```bash
[centos@ip-172-31-45-178 ~]$ sudo yum update
```

의존성 패키지 설치

```bash
[centos@ip-172-31-45-178 ~]$ sudo yum install -y zlib-devel bzip2 bzip2-devel readline-devel sqlite sqlite-devel openssl-devel xz xz-devel curl git
```

pyenv 설치 [**참조 페이지**](https://github.com/pyenv/pyenv-installer#installation--update--uninstallation)

```bash
[centos@ip-172-31-45-178 ~]$ curl https://pyenv.run | bash
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   270  100   270    0     0    246      0  0:00:01  0:00:01 --:--:--   246
Cloning into '/home/centos/.pyenv'...
remote: Enumerating objects: 876, done.
remote: Counting objects: 100% (876/876), done.
remote: Compressing objects: 100% (432/432), done.
remote: Total 876 (delta 501), reused 560 (delta 338), pack-reused 0
Receiving objects: 100% (876/876), 453.53 KiB | 17.44 MiB/s, done.
Resolving deltas: 100% (501/501), done.
Cloning into '/home/centos/.pyenv/plugins/pyenv-doctor'...
remote: Enumerating objects: 11, done.
remote: Counting objects: 100% (11/11), done.
remote: Compressing objects: 100% (9/9), done.
remote: Total 11 (delta 1), reused 2 (delta 0), pack-reused 0
Unpacking objects: 100% (11/11), 38.70 KiB | 5.53 MiB/s, done.
Cloning into '/home/centos/.pyenv/plugins/pyenv-installer'...
remote: Enumerating objects: 16, done.
remote: Counting objects: 100% (16/16), done.
remote: Compressing objects: 100% (13/13), done.
remote: Total 16 (delta 1), reused 10 (delta 0), pack-reused 0
Unpacking objects: 100% (16/16), 5.76 KiB | 1.92 MiB/s, done.
Cloning into '/home/centos/.pyenv/plugins/pyenv-update'...
remote: Enumerating objects: 10, done.
remote: Counting objects: 100% (10/10), done.
remote: Compressing objects: 100% (6/6), done.
remote: Total 10 (delta 1), reused 5 (delta 0), pack-reused 0
Unpacking objects: 100% (10/10), 2.83 KiB | 1.41 MiB/s, done.
Cloning into '/home/centos/.pyenv/plugins/pyenv-virtualenv'...
remote: Enumerating objects: 61, done.
remote: Counting objects: 100% (61/61), done.
remote: Compressing objects: 100% (55/55), done.
remote: Total 61 (delta 11), reused 26 (delta 0), pack-reused 0
Unpacking objects: 100% (61/61), 38.21 KiB | 2.12 MiB/s, done.
Cloning into '/home/centos/.pyenv/plugins/pyenv-which-ext'...
remote: Enumerating objects: 10, done.
remote: Counting objects: 100% (10/10), done.
remote: Compressing objects: 100% (6/6), done.
remote: Total 10 (delta 1), reused 6 (delta 0), pack-reused 0
Unpacking objects: 100% (10/10), 2.92 KiB | 1.46 MiB/s, done.

WARNING: seems you still have not added 'pyenv' to the load path.


# See the README for instructions on how to set up
# your shell environment for Pyenv.

# Load pyenv-virtualenv automatically by adding
# the following to ~/.bashrc:

eval "$(pyenv virtualenv-init -)"
```

bash_profile 추가

```bash
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
echo 'eval "$(pyenv init -)"' >> ~/.bash_profile
echo 'eval "$(pyenv init --path)"' >> ~/.bash_profile
source ~/.bash_profile
```

pyenv가 잘 실행되는 지 확인 겸 pyenv 업데이트 후 각종 커맨드 실행

```bash
[centos@ip-172-31-45-178 ~]$ pyenv update
```

```bash
[centos@ip-172-31-45-178 ~]$ pyenv --version
pyenv 2.2.3
```

```bash
[centos@ip-172-31-45-178 ~]$ pyenv install --list | wc -l
532
```

## pyenv를 이용한 python 설치

우선 python 설치에 필요한 의존성 패키지들을 설치 [**참조 페이지: Install Python build dependencies**](https://github.com/pyenv/pyenv/wiki#suggested-build-environment) 

```bash
[centos@ip-172-31-45-178 ~]$ sudo yum install gcc zlib-devel bzip2 bzip2-devel readline-devel sqlite sqlite-devel openssl-devel tk-devel libffi-devel xz-devel
-----
Installed:
  binutils-2.30-108.el8_5.1.x86_64     cpp-8.5.0-4.el8_5.x86_64                 expat-devel-2.2.5-4.el8.x86_64    fontconfig-devel-2.13.1-4.el8.x86_64 freetype-devel-2.9.1-4.el8_3.1.x86_64
  gcc-8.5.0-4.el8_5.x86_64             glibc-devel-2.28-164.el8.x86_64          glibc-headers-2.28-164.el8.x86_64 isl-0.16.1-6.el8.x86_64              kernel-headers-4.18.0-348.7.1.el8_5.x86_64
  libX11-devel-1.6.8-5.el8.x86_64      libX11-xcb-1.6.8-5.el8.x86_64            libXau-devel-1.0.9-3.el8.x86_64   libXft-2.3.3-1.el8.x86_64            libXft-devel-2.3.3-1.el8.x86_64
  libXrender-devel-0.9.10-7.el8.x86_64 libffi-devel-3.1-22.el8.x86_64           libmpc-1.1.0-9.1.el8.x86_64       libpng-devel-2:1.6.34-5.el8.x86_64   libuuid-devel-2.32.1-28.el8.x86_64
  libxcb-devel-1.13.1-1.el8.x86_64     libxcrypt-devel-4.1.1-6.el8.x86_64       tcl-1:8.6.8-2.el8.x86_64          tcl-devel-1:8.6.8-2.el8.x86_64       tk-1:8.6.8-1.el8.x86_64
  tk-devel-1:8.6.8-1.el8.x86_64        xorg-x11-proto-devel-2020.1-3.el8.noarch

Complete!
```

리스트에서 확인한 가장 최신 버전인 3.10.1을 설치

```bash
[centos@ip-172-31-45-178 ~]$ pyenv install 3.10.1
Downloading Python-3.10.1.tar.xz...
-> https://www.python.org/ftp/python/3.10.1/Python-3.10.1.tar.xz
Installing Python-3.10.1...

BUILD FAILED (CentOS Linux 8 using python-build 20180424)

Inspect or clean up the working tree at /tmp/python-build.20220102182735.90387
Results logged to /tmp/python-build.20220102182735.90387.log
```

fail 원인 확인

```bash
[centos@ip-172-31-45-178 ~]$ cat /tmp/python-build.20220102182735.90387.log
-----
/home/centos/.pyenv/plugins/python-build/bin/python-build: line 796: make: command not found
```

make 커맨드가 없다고 하므로 설치해 준다.
그러고보니 centos 8부터는 yum이 아니라 dnf를 써야 했는데 습관적으로 여태 yum을 쓰고 있었다...

```bash
[centos@ip-172-31-45-178 ~]$ sudo dnf install make
```

설치했으니 다시 시도

```bash
[centos@ip-172-31-45-178 ~]$ pyenv install 3.10.1
Downloading Python-3.10.1.tar.xz...
-> https://www.python.org/ftp/python/3.10.1/Python-3.10.1.tar.xz
Installing Python-3.10.1...
Installed Python-3.10.1 to /home/centos/.pyenv/versions/3.10.1
```

완료. 3.10.1을 글로벌 버전으로 설정하고 rehash

```bash
[centos@ip-172-31-45-178 ~]$ pyenv global 3.10.1
[centos@ip-172-31-45-178 ~]$ pyenv rehash
```

python3, pip3 버전을 각각 확인

```bash
[centos@ip-172-31-45-178 ~]$ python3 -V
Python 3.10.1
[centos@ip-172-31-45-178 ~]$ pip3 -V
pip 21.2.4 from /home/centos/.pyenv/versions/3.10.1/lib/python3.10/site-packages/pip (python 3.10)
```

3이 붙지 않은 python, pip로 사용하기 위해 alias 설정

```bash
echo 'alias python3=python' >> ~/.bash_profile
echo 'alias pip3=pip' >> ~/.bash_profile
source ~/.bash_profile
```

python, pip로 사용되는지 확인

```bash
[centos@ip-172-31-45-178 ~]$ python -V
Python 3.10.1
[centos@ip-172-31-45-178 ~]$ pip -V
pip 21.2.4 from /home/centos/.pyenv/versions/3.10.1/lib/python3.10/site-packages/pip (python 3.10)
```

완료.

## venv 기동

블로그 외에도 복수의 프로젝트를 운용할지는 모르겠으나, 
차후 프로젝트 패키지 간의 충돌을 막기 위해 일단 가상환경을 사용하기로 한다.
우선 pip 버전 21.3.1이 이용 가능하다고 하여 업데이트.

```bash
[centos@ip-172-31-45-178 ~]$ pip install
ERROR: You must give at least one requirement to install (see "pip help install")
WARNING: You are using pip version 21.2.4; however, version 21.3.1 is available.
You should consider upgrading via the '/home/centos/.pyenv/versions/3.10.1/bin/python3.10 -m pip install --upgrade pip' command.
[centos@ip-172-31-45-178 ~]$ /home/centos/.pyenv/versions/3.10.1/bin/python3.10 -m pip install --upgrade pip
Requirement already satisfied: pip in ./.pyenv/versions/3.10.1/lib/python3.10/site-packages (21.2.4)
Collecting pip
  Downloading pip-21.3.1-py3-none-any.whl (1.7 MB)
     |████████████████████████████████| 1.7 MB 1.7 MB/s
Installing collected packages: pip
  Attempting uninstall: pip
    Found existing installation: pip 21.2.4
    Uninstalling pip-21.2.4:
      Successfully uninstalled pip-21.2.4
Successfully installed pip-21.3.1
```

```bash
[centos@ip-172-31-45-178 ~]$ pip -V
pip 21.3.1 from /home/centos/.pyenv/versions/3.10.1/lib/python3.10/site-packages/pip (python 3.10)
```

조사해보니 원래는 pip로 virtualenv 패키지를 설치해서 이용했던 것 같은데,
python 3.3부터는 별도의 패키지를 설치하지 않고도 [**python 커맨드로도 이용 가능**](https://docs.python.org/3/library/venv.html#creating-virtual-environments)한 모양.



우선 python virtual env용으로 만들 디렉토리를 생성한다.
현재 모든 디렉토리가 root 권한이어서 디렉토리 하나 만드는 데에도 sudo가 필요하다.
그렇지만 우선은 혼자 사용할 서버이니 유저 권한에 대해서는 따로 신경쓰지 않고 일단 계속 sudo로 실행하도록 한다.

```bash
[centos@ip-172-31-45-178 local]$ sudo mkdir pythonvenv
```

minahblog라는 이름으로 가상환경을 시작한다.

```bash
[centos@ip-172-31-45-178 pythonvenv]$ python -m venv minahblog
Error: [Errno 13] Permission denied: '/usr/local/pythonvenv/minahblog'
[centos@ip-172-31-45-178 pythonvenv]$ sudo python -m venv minahblog
sudo: python: command not found
```

centos 유저로 하자니 permission denied가 나오고, sudo를 붙여 실행하자니 python 커맨드를 읽지 못한다.
bash_profile에 추가한 것 만으로는, root user에서 해당 내용을 읽지 못하기 때문.
root user가 현재의 PATH를 읽어들일 수 있도록 수정해줄 필요가 있다. [**참조 페이지**](https://genchan.net/it/programming/python/7469/)

```bash
sudo sudovi
```

변경 전

```bash
Defaults    secure_path = /sbin:/bin:/usr/sbin:/usr/bin
```

변경 후

```bash
#Defaults    secure_path = /sbin:/bin:/usr/sbin:/usr/bin
Defaults    env_keep +="PATH" # Make root user executable 'python'. Minah Kim Added at 21/01/03
```

변경사항 반영을 위해 쉘 실행

```bash
exec $SHELL
```

다시 venv 시작

```bash
[centos@ip-172-31-45-178 pythonvenv]$ sudo python -m venv minahblog
```

```bash
[centos@ip-172-31-45-178 pythonvenv]$ ll minahblog/
total 4
drwxr-xr-x. 2 root root 168 Jan  2 19:21 bin
drwxr-xr-x. 2 root root   6 Jan  2 19:21 include
drwxr-xr-x. 3 root root  24 Jan  2 19:21 lib
lrwxrwxrwx. 1 root root   3 Jan  2 19:21 lib64 -> lib
-rw-r--r--. 1 root root 101 Jan  2 19:21 pyvenv.cfg
```

가상 환경에 접속 시에는 source activate를 실행한다.

```bash
[centos@ip-172-31-45-178 pythonvenv]$ cd minahblog/bin
[centos@ip-172-31-45-178 bin]$ source activate
(minahblog) [centos@ip-172-31-45-178 bin]$
```

빠져나올 시에는 deactivate를 실행한다.

```bash
(minahblog) [centos@ip-172-31-45-178 bin]$ deactivate
[centos@ip-172-31-45-178 bin]$
```

## Django 설치

```bash
(minahblog) [centos@ip-172-31-45-178 bin]$ pip install django
Collecting django
  Downloading Django-4.0-py3-none-any.whl (8.0 MB)
     |████████████████████████████████| 8.0 MB 2.2 MB/s
Collecting sqlparse>=0.2.2
  Downloading sqlparse-0.4.2-py3-none-any.whl (42 kB)
     |████████████████████████████████| 42 kB 2.6 MB/s
Collecting asgiref<4,>=3.4.1
  Downloading asgiref-3.4.1-py3-none-any.whl (25 kB)
Installing collected packages: sqlparse, asgiref, django
ERROR: Could not install packages due to an OSError: [Errno 13] Permission denied: '/usr/local/pythonvenv/minahblog/lib/python3.10/site-packages/sqlparse'
Check the permissions.

WARNING: You are using pip version 21.2.4; however, version 21.3.1 is available.
You should consider upgrading via the '/usr/local/pythonvenv/minahblog/bin/python -m pip install --upgrade pip' command.
```

우선 가상환경 내에 pip는 여전히 21.2.4인것 같다.
왠지 거슬리니 가상환경 내 pip를 업데이트 해주기로 한다.

```bash
(minahblog) [centos@ip-172-31-45-178 bin]$ ll
total 36
-rw-r--r--. 1 root root 9033 Jan  2 19:21 Activate.ps1
-rw-r--r--. 1 root root 2008 Jan  2 19:21 activate
-rw-r--r--. 1 root root  934 Jan  2 19:21 activate.csh
-rw-r--r--. 1 root root 2076 Jan  2 19:21 activate.fish
-rwxr-xr-x. 1 root root  247 Jan  2 19:26 pip
-rwxr-xr-x. 1 root root  247 Jan  2 19:26 pip3
-rwxr-xr-x. 1 root root  247 Jan  2 19:26 pip3.10
lrwxrwxrwx. 1 root root   46 Jan  2 19:21 python -> /home/centos/.pyenv/versions/3.10.1/bin/python
lrwxrwxrwx. 1 root root    6 Jan  2 19:21 python3 -> python
lrwxrwxrwx. 1 root root    6 Jan  2 19:21 python3.10 -> python

(minahblog) [centos@ip-172-31-45-178 bin]$ sudo ./python -m pip install --upgrade pip

(minahblog) [centos@ip-172-31-45-178 bin]$ pip -V
pip 21.3.1 from /usr/local/pythonvenv/minahblog/lib/python3.10/site-packages/pip (python 3.10)
```

django install

```bash
(minahblog) [centos@ip-172-31-45-178 bin]$ sudo pip install django
Collecting django
  Downloading Django-4.0-py3-none-any.whl (8.0 MB)
     |████████████████████████████████| 8.0 MB 1.7 MB/s
Collecting asgiref<4,>=3.4.1
  Downloading asgiref-3.4.1-py3-none-any.whl (25 kB)
Collecting sqlparse>=0.2.2
  Downloading sqlparse-0.4.2-py3-none-any.whl (42 kB)
     |████████████████████████████████| 42 kB 2.3 MB/s
Installing collected packages: sqlparse, asgiref, django
Successfully installed asgiref-3.4.1 django-4.0 sqlparse-0.4.2
```

```bash
(minahblog) [centos@ip-172-31-45-178 bin]$ python -m django --version
4.0
```

4.0으로 설치 완료.



Django 프로젝트는 로컬 PC에서 개발 중인 것이 있으므로, 여기서는 Django의 startproject 및 startapp은 생략한다.