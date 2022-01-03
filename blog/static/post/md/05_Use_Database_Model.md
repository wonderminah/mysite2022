# DB 테이블을 Django의 모델로 연동하기

우선 DB 테이블 작성. 블로그 포스트 데이터를 관리할 posts라는 테이블을 작성한다.

```sql
use blog;
```

```sql
CREATE TABLE posts (
 `post_id` mediumint(7) unsigned NOT NULL auto_increment,
 `target_mdfile` varchar(255) NOT NULL default '',
 `created_datetime` datetime DEFAULT CURRENT_TIMESTAMP,
 `updated_datetime` datetime DEFAULT CURRENT_TIMESTAMP,
 `timestamp` timestamp NOT NULL default CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
 PRIMARY KEY (`post_id`)
);
Query OK, 0 rows affected, 1 warning (0.03 sec)
```

이제 python으로 모델 코드를 작성하여야 하는데,
python에서는 inspectdb라고 하여, 기존 테이블을 읽고 모델의 정의를 만들어 주는 아주 고마운 명령어가 존재한다.
실행하면 아래와 같다.

```bash
(minahblog) [centos@ip-172-31-45-178 mysite]$ python manage.py inspectdb
...
class Posts(models.Model):
    post_id = models.AutoField(primary_key=True)
    target_mdfile = models.CharField(max_length=255)
    created_datetime = models.DateTimeField(blank=True, null=True)
    updated_datetime = models.DateTimeField(blank=True, null=True)
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'posts'
```

위에서 출력된 코드를 models.py에 정의한다. 정의하였다면, 아래와 같이 마이그레이션을 실행해 준다.

```bash
{22-01-04 5:10}P79305:~/PycharmProjects/mysite@main✗✗✗✗✗✗ minah.kim% python manage.py makemigrations
Migrations for 'blog':
  blog/migrations/0001_initial.py
    - Create model Posts
{22-01-04 5:10}P79305:~/PycharmProjects/mysite@main✗✗✗✗✗✗ minah.kim% python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, blog, contenttypes, sessions
Running migrations:
  Applying blog.0001_initial... OK
```

## 테스트

테스트를 위해 dummy 데이터 1행 생성.
모든 컬럼에 default value가 설정되어 있으므로 괄호 안에는 특정 key와 value를 입력하지 않아도 되는 쿼리이다.

```sql
INSERT INTO posts () VALUES ();

SELECT * FROM posts;
+---------+---------------+---------------------+---------------------+---------------------+
| post_id | target_mdfile | created_datetime    | updated_datetime    | timestamp           |
+---------+---------------+---------------------+---------------------+---------------------+
|       1 |               | 2022-01-03 20:14:26 | 2022-01-03 20:14:26 | 2022-01-03 20:14:26 |
+---------+---------------+---------------------+---------------------+---------------------+
1 row in set (0.00 sec)
```

인덱스 페이지에 접속하면 Posts 모델을 print하도록 views.py를 수정

```python
from .models import Posts

def index(request):
    print(Posts.post_id)
```

결과, 무언가 취득된 것이 확인된다.

```bash
<django.db.models.query_utils.DeferredAttribute object at 0x106e2be50>
[03/Jan/2022 20:20:31] "GET / HTTP/1.1" 200 8695
```

직접 데이터가 취득되는지 확인하고 싶으므로, [**getter 및 setter를 정의**](https://www.nblog09.com/w/2019/01/09/python-setter-getter/)하고 다시 호출해 보았으나,
정의의 오류인지 호출 문법의 오류인지 확인은 제대로 안 되었다. 우선 여기까지 해두고 차후 다시 확인 예정.

```python
class Posts(models.Model):
  
		...

    @property
    def post_id(self):
        return self.__post_id

    @property
    def target_mdfile(self):
        return self.__target_mdfile

    @property
    def created_datetime(self):
        return self.__created_datetime

    @property
    def updated_datetime(self):
        return self.__updated_datetime

    @property
    def timestamp(self):
        return self.__timestamp

    @post_id.setter
    def post_id(self, value):
        self.__post_id = value

    @target_mdfile.setter
    def target_mdfile(self, value):
        self.__target_mdfile = value

    @created_datetime.setter
    def created_datetime(self, value):
        self.__created_datetime = value

    @updated_datetime.setter
    def updated_datetime(self, value):
        self.__updated_datetime = value

    @timestamp.setter
    def timestamp(self, value):
        self.__timestamp = value

    @post_id.deleter
    def post_id(self):
        del self.__post_id

    @target_mdfile.deleter
    def target_mdfile(self):
        del self.__target_mdfile

    @created_datetime.deleter
    def created_datetime(self):
        del self.__created_datetime

    @updated_datetime.deleter
    def updated_datetime(self):
        del self.__updated_datetime

    @timestamp.deleter
    def timestamp(self):
        del self.__timestamp
```

