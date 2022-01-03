# Django App 배포

본 자료는 단순히 브라우저에 우선 띄우는 것을 목표로 하는 비공식적인 방법이다.
아직 Apache 등 웹 서버도 따로 연동하지 않았기에,
단순히 서버에서 git에 올려 둔 프로토타입 Django 블로그를 clone하고 Django runserver를 실행하여 우선 띄우도록 한다.
일반적인 배포 방법은 차후 필요하다면 조사 후 업데이트 예정.

```bash
[centos@ip-172-31-45-178 mysite]$ git clone https://github.com/wonderminah/mysite2022.git
[centos@ip-172-31-45-178 mysite]$ sudo mv mysite2022 mysite

[centos@ip-172-31-45-178 mysite]$ python manage.py runserver 0:8000
...
ImportError: Couldn't import Django. Are you sure it's installed and available on your PYTHONPATH environment variable? Did you forget to activate a virtual environment?
```

runserver 전, 가상환경을 activate 해주어야 한다.

```bash
[centos@ip-172-31-45-178 mysite]$ cd ../bin && source activate
(minahblog) [centos@ip-172-31-45-178 bin]$ cd ../mysite && python manage.py runserver 0:8000
...
Starting development server at http://0:8000/
```

## runserver를 [**백그라운드에서 실행**](https://kidnohr.hatenadiary.com/entry/2017/02/01/153327)시키고 싶을 때 

```bash
(minahblog) [centos@ip-172-31-45-178 mysite]$ python manage.py runserver 0.0.0.0:8000 > /dev/null 2>&1 < /dev/null &
```

