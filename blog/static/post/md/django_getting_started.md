# Quick Install Guide

https://docs.djangoproject.com/ko/4.0/intro/install/

Python: 3.10.1

```bash
{21-12-29 1:53}P79305:~ minah.kim% python -V
Python 3.10.1
```

Pip: 21.3.1

```bash
{21-12-29 1:53}P79305:~ minah.kim% pip -V
pip 21.3.1 from /Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages/pip (python 3.10)
```

Django: 4.0

```bash
{21-12-29 1:48}P79305:~ minah.kim% python3 -m django --version
4.0
```

# Writing your first Django app, part 1

```bash
{21-12-29 1:51}P79305:~/PycharmProjects minah.kim% django-admin startproject mysite

{21-12-29 1:55}P79305:~/PycharmProjects minah.kim% cd mysite
{21-12-29 1:55}P79305:~/PycharmProjects/mysite minah.kim% python manage.py startapp polls
```

2019년도에 공부할 당시와 달리 대충 이정도면 알겠으므로... 바로 개인 블로그 제작으로 들어가겠다.

# 개인 블로그 제작 시작

```bash
```

# jekyll을 django와 쓰고 싶어 조사 시작

https://jekyllrb.com/docs/

```bash
brew install ruby
echo 'export PATH="/usr/local/opt/ruby/bin:$PATH"' >> ~/.zshrc
export LDFLAGS="-L/usr/local/opt/ruby/lib"
export CPPFLAGS="-I/usr/local/opt/ruby/include"
export PKG_CONFIG_PATH="/usr/local/opt/ruby/lib/pkgconfig"

export SDKROOT=$(xcrun --show-sdk-path)
echo 'export PATH="/usr/local/opt/ruby/bin:/usr/local/lib/ruby/gems/3.0.0/bin:$PATH"' >> ~/.zshrc
source .zshrc

vi .zshrc
-----
# add gem PATH
export PATH="~/.gem/ruby/3.0.0/bin:$PATH"
-----
source .zshrc

gem install --user-install bundler jekyll
```

```bash
{21-12-29 6:06}P79305:~ minah.kim% jekyll new testjekyll
Running bundle install in /Users/minah.kim/testjekyll...
```

모르겠다... 잘 안돼서 때려침.

# markdown 파일을 html로 부르는 방법

```bash
pip install markdown
```

# code를 예쁘게

https://highlightjs.org/

```bash
<link rel="stylesheet" type="text/css" href="{% static 'css/highlightjs/atom-one-light.min.css' %}">
<script type="text/javascript" src="{% static 'js/highlightjs/highlight.min.js' %}"></script>
```

# AWS EC2 인스턴스 생성

![image-20211231131510648](/Users/minah.kim/Library/Application Support/typora-user-images/image-20211231131510648.png)

![image-20211231131524042](/Users/minah.kim/Library/Application Support/typora-user-images/image-20211231131524042.png)

![image-20211231131536742](/Users/minah.kim/Library/Application Support/typora-user-images/image-20211231131536742.png)

![image-20211231131555140](/Users/minah.kim/Library/Application Support/typora-user-images/image-20211231131555140.png)

![image-20211231131656029](/Users/minah.kim/Library/Application Support/typora-user-images/image-20211231131656029.png)

종료 시 삭제 체크 해제

암호화를 alias/aws/ebs로 설정

![image-20211231131722721](/Users/minah.kim/Library/Application Support/typora-user-images/image-20211231131722721.png)

![image-20211231131841397](/Users/minah.kim/Library/Application Support/typora-user-images/image-20211231131841397.png)

새 보안 그룹 생성 대신, 기존 보안 그룹 선택에 체크 (잘 몰라서)

![image-20211231131920644](/Users/minah.kim/Library/Application Support/typora-user-images/image-20211231131920644.png)

![image-20211231132104495](/Users/minah.kim/Library/Application Support/typora-user-images/image-20211231132104495.png)

![image-20211231132153913](/Users/minah.kim/Library/Application Support/typora-user-images/image-20211231132153913.png)

![image-20211231132222406](/Users/minah.kim/Library/Application Support/typora-user-images/image-20211231132222406.png)

```bash
{21-12-31 13:29}P79305:~/Desktop/AWS minah.kim% chmod 400 aws-ec2-keypair-rsa.pem
{21-12-31 13:29}P79305:~/Desktop/AWS minah.kim% ll aws-ec2-keypair-rsa.pem
-r--------@ 1 minah.kim  679754705   1.7K Dec 31 13:21 aws-ec2-keypair-rsa.pem
```

![image-20211231133010725](/Users/minah.kim/Library/Application Support/typora-user-images/image-20211231133010725.png)

```bash
{21-12-31 13:37}P79305:~/Desktop/AWS minah.kim% ssh -i "aws-ec2-keypair-rsa.pem" ec2-user@ec2-13-125-252-157.ap-northeast-2.compute.amazonaws.com
ssh: connect to host ec2-13-125-252-157.ap-northeast-2.compute.amazonaws.com port 22: Operation timed out
```

왜 안돼...



https://qiita.com/yokoto/items/338bd80262d9eefb152e 를 참고해서 보안설정을 변경해보자.

![image-20211231134023406](/Users/minah.kim/Library/Application Support/typora-user-images/image-20211231134023406.png)

![image-20211231134303623](/Users/minah.kim/Library/Application Support/typora-user-images/image-20211231134303623.png)

SSH를 내 IP로 추가

```bash
{22-01-03 2:51}P79305:~/Desktop/AWS minah.kim% ssh -i "aws-ec2-keypair-rsa.pem" centos@ec2-13-125-213-99.ap-northeast-2.compute.amazonaws.com
Activate the web console with: systemctl enable --now cockpit.socket
```

됐다!

```bash
[centos@ip-172-31-45-178 ~]$ df -h
Filesystem      Size  Used Avail Use% Mounted on
devtmpfs        380M     0  380M   0% /dev
tmpfs           408M     0  408M   0% /dev/shm
tmpfs           408M   11M  398M   3% /run
tmpfs           408M     0  408M   0% /sys/fs/cgroup
/dev/xvda2       10G  1.9G  8.2G  19% /
tmpfs            82M     0   82M   0% /run/user/1000
```

centos 버전 확인

```bash
[centos@ip-172-31-45-178 ~]$ cat /etc/redhat-release
CentOS Linux release 8.5.2111
```

# Cent OS 8에 python 환경설정 (pyenv + venv)

## pyenv 설치

우선 sudo yum update

```bash
[centos@ip-172-31-45-178 ~]$ sudo yum update
```

전제가 되는 패키지 설치

```bash
[centos@ip-172-31-45-178 ~]$ sudo yum install -y zlib-devel bzip2 bzip2-devel readline-devel sqlite sqlite-devel openssl-devel xz xz-devel curl git
```

pyenv 설치

참조: https://github.com/pyenv/pyenv-installer#installation--update--uninstallation

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

.bashrc 파일에 다음을 추가

```bash
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
echo 'eval "$(pyenv init -)"' >> ~/.bash_profile
echo 'eval "$(pyenv init --path)"' >> ~/.bash_profile
source ~/.bash_profile
```

pyenv가 잘 실행되는 지 볼 겸 최신으로 업데이트 하고 이것저것 커맨드를 실행해본다.

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

[**Install Python build dependencies**](https://github.com/pyenv/pyenv/wiki#suggested-build-environment) before attempting to install a new Python version.

우선 python 설치에 필요한 의존성 패키지들을 설치해 준다.

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

왜 fail인고 하여 로그를 보니

```bash
[centos@ip-172-31-45-178 ~]$ cat /tmp/python-build.20220102182735.90387.log
-----
/home/centos/.pyenv/plugins/python-build/bin/python-build: line 796: make: command not found
```

make커맨드가 없다고 한다. 설치해주자.

그러고보니 centos 8부터는 yum이 아니라 dnf를 써야 하는데 습관적으로 여태 yum을 썼....;

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

완료! 글로벌 버전으로 설정하고 rehash

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

완료

## virtualenv 설치

블로그 외에도 프로젝트를 여러 개 운용할지는 모르겠으나, 

차후 프로젝트 패키지 간의 충돌을 막기 위해 일단 가상환경을 사용하기로 한다.

그와중에 pip 버전 21.2.4인데 21.3.1이 이용 가능하다고 하여 일단 업데이트.

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

python 3.3부터는 별도의 패키지를 설치하지 않고도 python 커맨드로도 이용 가능한 모양.

참조: https://docs.python.org/3/library/venv.html#creating-virtual-environments



우선 python virtual env용으로 만들 디렉토리를 생성.

현재 모든 디렉토리가 root 권한이어서 디렉토리 하나 만드는 데에도 sudo가 필요하다.

그렇지만 나 혼자만 사용할 서버이니 유저 권한에 대해서는 따로 신경쓰지 않고 일단 계속 sudo로 실행하도록 한다.

```bash
[centos@ip-172-31-45-178 local]$ sudo mkdir pythonvenv
```

minahblog라는 이름으로 가상환경 시작

```bash
[centos@ip-172-31-45-178 pythonvenv]$ python -m venv minahblog
Error: [Errno 13] Permission denied: '/usr/local/pythonvenv/minahblog'
[centos@ip-172-31-45-178 pythonvenv]$ sudo python -m venv minahblog
sudo: python: command not found
```

centos 유저로 하자니 permission denied가 나오고, sudo를 붙여 실행하자니 python 커맨드를 읽지 못한다.

.bash_profile에 추가한 것 만으로는, root user에서 해당 내용을 읽지 못하기 때문.

root user가 현재의 PATH를 읽어들일 수 있도록 수정해줄 필요가 있다.

참조: https://genchan.net/it/programming/python/7469/

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

가상 환경에 접속 시

```bash
[centos@ip-172-31-45-178 pythonvenv]$ cd minahblog/bin
[centos@ip-172-31-45-178 bin]$ source activate
(minahblog) [centos@ip-172-31-45-178 bin]$
```

나올 시

```bash
(minahblog) [centos@ip-172-31-45-178 bin]$ deactivate
[centos@ip-172-31-45-178 bin]$
```

## django 설치

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

우선 가상환경 내에 pip는 여전히 21.2.4인것 같다. 왠지 거슬리니 가상환경 내 pip를 업데이트 해주기로 한다.

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

프로젝트는 이미 로컬 PC에 만들어 둔 것이 있으니 나중에 git에서 가져오면 되고,

이제 브라우저에서 접속할 수 있도록 웹서버를 준비해야 한다.

EC2 인스턴스에 apache를 설치해 보자.

# Cent OS 8에 Apache를 깔아보자

dnf로 설치 가능한 httpd 패키지 정보 확인

```bash
(minahblog) [centos@ip-172-31-45-178 bin]$ dnf info httpd
CentOS Linux 8 - AppStream                                                                                                                                          7.3 MB/s | 8.4 MB     00:01
CentOS Linux 8 - BaseOS                                                                                                                                             9.6 MB/s | 4.6 MB     00:00
Last metadata expiration check: 0:00:01 ago on Sun 02 Jan 2022 07:30:53 PM UTC.
Available Packages
Name         : httpd
Version      : 2.4.37
Release      : 43.module_el8.5.0+1022+b541f3b1
Architecture : x86_64
Size         : 1.4 M
Source       : httpd-2.4.37-43.module_el8.5.0+1022+b541f3b1.src.rpm
Repository   : appstream
Summary      : Apache HTTP Server
URL          : https://httpd.apache.org/
License      : ASL 2.0
Description  : The Apache HTTP Server is a powerful, efficient, and extensible
             : web server.
```

설치

```bash
(minahblog) [centos@ip-172-31-45-178 bin]$ sudo dnf install httpd
```

```bash
Installed:
  apr-1.6.3-12.el8.x86_64                                               apr-util-1.6.1-6.el8.x86_64                                      apr-util-bdb-1.6.1-6.el8.x86_64
  apr-util-openssl-1.6.1-6.el8.x86_64                                   centos-logos-httpd-85.8-2.el8.noarch                             httpd-2.4.37-43.module_el8.5.0+1022+b541f3b1.x86_64
  httpd-filesystem-2.4.37-43.module_el8.5.0+1022+b541f3b1.noarch        httpd-tools-2.4.37-43.module_el8.5.0+1022+b541f3b1.x86_64        mailcap-2.1.48-3.el8.noarch
  mod_http2-1.15.7-3.module_el8.4.0+778+c970deab.x86_64

Complete!
```

httpd 프로세스 정보 확인

```bash
(minahblog) [centos@ip-172-31-45-178 bin]$ systemctl status httpd
● httpd.service - The Apache HTTP Server
   Loaded: loaded (/usr/lib/systemd/system/httpd.service; disabled; vendor preset: disabled)
   Active: inactive (dead)
     Docs: man:httpd.service(8)
```

서버 부팅 시 자동 시작하도록 enable 설정

```bash
(minahblog) [centos@ip-172-31-45-178 bin]$ sudo systemctl enable httpd
Created symlink /etc/systemd/system/multi-user.target.wants/httpd.service → /usr/lib/systemd/system/httpd.service.
```

아파치 프로세스 start, status 확인

```bash
(minahblog) [centos@ip-172-31-45-178 bin]$ sudo systemctl start httpd
(minahblog) [centos@ip-172-31-45-178 bin]$ sudo systemctl status httpd
● httpd.service - The Apache HTTP Server
   Loaded: loaded (/usr/lib/systemd/system/httpd.service; enabled; vendor preset: disabled)
   Active: active (running) since Sun 2022-01-02 19:38:05 UTC; 4s ago
     Docs: man:httpd.service(8)
 Main PID: 115200 (httpd)
   Status: "Started, listening on: port 80"
    Tasks: 213 (limit: 4855)
   Memory: 19.2M
   CGroup: /system.slice/httpd.service
           ├─115200 /usr/sbin/httpd -DFOREGROUND
           ├─115201 /usr/sbin/httpd -DFOREGROUND
           ├─115202 /usr/sbin/httpd -DFOREGROUND
           ├─115203 /usr/sbin/httpd -DFOREGROUND
           └─115204 /usr/sbin/httpd -DFOREGROUND

Jan 02 19:38:05 ip-172-31-45-178.ap-northeast-2.compute.internal systemd[1]: Starting The Apache HTTP Server...
Jan 02 19:38:05 ip-172-31-45-178.ap-northeast-2.compute.internal systemd[1]: Started The Apache HTTP Server.
Jan 02 19:38:05 ip-172-31-45-178.ap-northeast-2.compute.internal httpd[115200]: Server configured, listening on: port 80
```

브라우저에서 접속하기 전에, http와 https 프로토콜을 열어줘야 한다.

현재는 ssh 통신을 위한 22 포트만 열려져 있는 상태.

![image-20220103044026680](/Users/minah.kim/Library/Application Support/typora-user-images/image-20220103044026680.png)

http와 https를 추가해 주도록 하자.

![image-20220103044220586](/Users/minah.kim/Library/Application Support/typora-user-images/image-20220103044220586.png)

이제 EC2 인스턴스의 퍼블릭 IPv4 주소로 브라우저에서 접속해보자.

![image-20220103044334874](/Users/minah.kim/Library/Application Support/typora-user-images/image-20220103044334874.png)

http server test page가 표시되면 아파치 설치도 okay.

참고로 여기서 보여지는 test page는 /usr/share/httpd/noindex/index.html이다.

이제 도메인 등 설정을 해보자.

## 설정

```bash
[centos@ip-172-31-45-178 httpd]$ ll
total 0
drwxr-xr-x. 2 root root  37 Jan  2 19:32 conf
drwxr-xr-x. 2 root root  82 Jan  2 19:32 conf.d
drwxr-xr-x. 2 root root 226 Jan  2 19:32 conf.modules.d
lrwxrwxrwx. 1 root root  19 Nov 12 04:58 logs -> ../../var/log/httpd
lrwxrwxrwx. 1 root root  29 Nov 12 04:58 modules -> ../../usr/lib64/httpd/modules
lrwxrwxrwx. 1 root root  10 Nov 12 04:58 run -> /run/httpd
lrwxrwxrwx. 1 root root  19 Nov 12 04:58 state -> ../../var/lib/httpd
[centos@ip-172-31-45-178 httpd]$ sudo mkdir conf.vhost.d
[centos@ip-172-31-45-178 httpd]$ cd conf.vhost.d
[centos@ip-172-31-45-178 conf.vhost.d]$ sudo touch wonderminah.io.conf
```

```bash
[centos@ip-172-31-45-178 conf.vhost.d]$ sudo vi wonderminah.io.conf
```

```bash
<VirtualHost *:80>
    DocumentRoot    /var/www/html/wonderminah.io
    ServerName      wonderminah.io
    ErrorLog        "/var/log/httpd/wonderminah.io/error_log"
    CustomLog       "/var/log/httpd/wonderminah.io/access_log" combined
    Include         conf.extra.d/wonderminah.io_extra.conf
</VirtualHost>

<VirtualHost *:81>
    DocumentRoot    /var/www/html/wonderminah.io
    SetEnv  HTTPS   on
    ServerName      https://wonderminah.io
    ErrorLog        "/var/log/httpd/wonderminah.io/ssl_error_log"
    CustomLog       "/var/log/httpd/wonderminah.io/ssl_access_log" combined
    Include         conf.extra.d/wonderminah.io_extra.conf
</VirtualHost>


<Directory "/var/www/html/wnikki6.www.nikki.prod.jp.local">
    Order Allow,Deny
    Allow from all
</Directory>
```

그러나 생각을 해보니... wonderminah.io라는 도메인이 필요하다. 휴

구입은 나중에 생각해보기로 하자. 우선 다른 작업부터. 일단 지워놓겠다.

```bash
[centos@ip-172-31-45-178 httpd]$ sudo rm -r conf.vhost.d/
```

# Apache와 django 연결

일단 로컬 PC에서 만든 django 프로젝트를 전송.

배포 절차는 나중에 알아보기로 하고 scp로 단순 전송.

```bash
{22-01-03 5:26}P79305:~/Desktop/AWS minah.kim% scp -r -i aws-ec2-keypair-rsa.pem ~/PycharmProjects/mysite centos@ec2-13-125-213-99.ap-northeast-2.compute.amazonaws.com:/home/centos/
```

```bash
(minahblog) [centos@ip-172-31-45-178 mysite]$ sudo mv /home/centos/mysite /usr/local/pythonvenv/minahblog/
```

```bash
cd /usr/local/pythonvenv/minahblog/mysite
python manage.py runserver
```

ModuleNotFoundError: No module named 'bs4' 등 설치되지 않은 모듈 오류가 나므로 필요한 모듈 설치.

```bash
(minahblog) [centos@ip-172-31-45-178 mysite]$ sudo pip install bs4
(minahblog) [centos@ip-172-31-45-178 mysite]$ sudo pip install markdown
```

```bash
(minahblog) [centos@ip-172-31-45-178 mysite]$ python manage.py runserver 0:8000
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
January 02, 2022 - 20:45:50
Django version 4.0, using settings 'mysite.settings'
Starting development server at http://0:8000/
Quit the server with CONTROL-C.
```

![image-20220103054642642](/Users/minah.kim/Library/Application Support/typora-user-images/image-20220103054642642.png)

두둥... 되었다!!!!!!!!!!!!!!!!!!!!!!!!!!
