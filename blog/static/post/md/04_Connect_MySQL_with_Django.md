# Django에 MySQL 사용하기

## Local (Mac OS Catalina 10.15.7)

brew로 mysql 설치

```bash
$ brew install mysql
$ mysql --version
mysql  Ver 8.0.27 for macos10.15 on x86_64 (Homebrew)
```

mysql 기동

```bash
$ mysql.server start
Starting MySQL
. SUCCESS!

$ mysql -u root
...
mysql>
```

새로운 DB 생성

```bash
mysql> create database blog;
Query OK, 1 row affected (0.00 sec)
```

프로젝트의 settings.py에서 변수 설정

```bash
DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': BASE_DIR / 'db.sqlite3',
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blog',
        'USER': 'root',
        'PASSWORD': '',
    }
}
```

mysqlclient 모듈 설치

```bash
$ pip install mysqlclient
```

프로젝트에서 migrate 실행

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

## Cent OS 8

dnf로 mysql 설치

```bash
$ sudo dnf install mysql-server
Installed:
  libaio-0.3.112-1.el8.x86_64                                      mariadb-connector-c-config-3.1.11-2.el8_3.noarch                 mecab-0.996-1.module_el8.4.0+589+11e12751.9.x86_64
  mysql-8.0.26-1.module_el8.4.0+915+de215114.x86_64                mysql-common-8.0.26-1.module_el8.4.0+915+de215114.x86_64         mysql-errmsg-8.0.26-1.module_el8.4.0+915+de215114.x86_64
  mysql-server-8.0.26-1.module_el8.4.0+915+de215114.x86_64         protobuf-lite-3.5.0-13.el8.x86_64

Complete!
```

mysql 기동

```bash
$ sudo systemctl start mysqld
$ systemctl status mysqld
● mysqld.service - MySQL 8.0 database server
   Loaded: loaded (/usr/lib/systemd/system/mysqld.service; disabled; vendor preset: disabled)
   Active: active (running) since Mon 2022-01-03 18:22:38 UTC; 3s ago
  Process: 120500 ExecStartPost=/usr/libexec/mysql-check-upgrade (code=exited, status=0/SUCCESS)
  Process: 120376 ExecStartPre=/usr/libexec/mysql-prepare-db-dir mysqld.service (code=exited, status=0/SUCCESS)
  Process: 120352 ExecStartPre=/usr/libexec/mysql-check-socket (code=exited, status=0/SUCCESS)
 Main PID: 120456 (mysqld)
   Status: "Server is operational"
    Tasks: 38 (limit: 4855)
   Memory: 446.8M
   CGroup: /system.slice/mysqld.service
           └─120456 /usr/libexec/mysqld --basedir=/usr

Jan 03 18:22:31 ip-172-31-45-178.ap-northeast-2.compute.internal systemd[1]: Starting MySQL 8.0 database server...
Jan 03 18:22:31 ip-172-31-45-178.ap-northeast-2.compute.internal mysql-prepare-db-dir[120376]: Initializing MySQL database
Jan 03 18:22:38 ip-172-31-45-178.ap-northeast-2.compute.internal systemd[1]: Started MySQL 8.0 database server.
```

서버 재기동 시 자동으로 mysql 또한 시작되도록 systemctl enable 설정

```bash
$ sudo systemctl enable mysqld
Created symlink /etc/systemd/system/multi-user.target.wants/mysqld.service → /usr/lib/systemd/system/mysqld.service.
```

mysql 버전 확인

```bash
$ mysql --version
mysql  Ver 8.0.26 for Linux on x86_64 (Source distribution)
```

새로운 DB 생성

```bash
$ mysql -u root
...
mysql> create database blog;
Query OK, 1 row affected (0.00 sec)
```

mysqlclient 모듈 설치

```bash
$ sudo pip install mysqlclient
ERROR: No matching distribution found for mysqlclient
```

[**stackoverflow 페이지**](https://stackoverflow.com/questions/51062920/pip-install-mysqlclient-error)를 참고로 다른 패키지 설치

```bash
$ sudo dnf install python3-devel mysql-devel
Installed:
  mysql-devel-8.0.26-1.module_el8.4.0+915+de215114.x86_64             mysql-libs-8.0.26-1.module_el8.4.0+915+de215114.x86_64                 platform-python-devel-3.6.8-41.el8.x86_64
  python-rpm-macros-3-41.el8.noarch                                   python-srpm-macros-3-41.el8.noarch                                     python3-pip-9.0.3-20.el8.noarch
  python3-rpm-generators-5-7.el8.noarch                               python3-rpm-macros-3-41.el8.noarch                                     python3-setuptools-39.2.0-6.el8.noarch
  python36-3.6.8-38.module_el8.5.0+895+a459eca8.x86_64                python36-devel-3.6.8-38.module_el8.5.0+895+a459eca8.x86_64

Complete!
```

재시도

```bash
$ sudo pip install mysqlclient
Successfully installed mysqlclient-2.1.0
```

성공.



settings.py의 수정사항을 반영하기 위해 EC2 인스턴스 서버에서 git pull 후, migrate 실행

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

python에서는 dbshell이라는 커맨드가 존재하는데, 이는 settings.py에서 설정한 데이터베이스로 접속하게 해주는 명령이다.
이 명령어를 실행하였을 때 아래와 같이 mysql 서버에 제대로 접속이 된다면, 연동에 성공한 것이다.

```bash
(minahblog) [centos@ip-172-31-45-178 mysite]$ python manage.py dbshell
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 31
Server version: 8.0.26 Source distribution

Copyright (c) 2000, 2021, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>
```