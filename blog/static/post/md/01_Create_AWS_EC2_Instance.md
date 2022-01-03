# AWS EC2 인스턴스 생성

![image-20211231131510648](static/post/img/image-20211231131510648.png)

![image-20211231131524042](static/post/img/image-20211231131524042.png)

![image-20211231131536742](static/post/img/image-20211231131536742.png)

![image-20211231131555140](static/post/img/image-20211231131555140.png)

![image-20211231131656029](static/post/img/image-20211231131656029.png)

종료 시 삭제 체크박스를 해제, 암호화를 alias/aws/ebs로 설정



![image-20211231131722721](static/post/img/image-20211231131722721.png)

![image-20211231131841397](static/post/img/image-20211231131841397.png)

새 보안 그룹 생성 대신, 기존 보안 그룹 선택에 체크



![image-20211231131920644](static/post/img/image-20211231131920644.png)

![image-20211231132104495](static/post/img/image-20211231132104495.png)

![image-20211231132153913](static/post/img/image-20211231132153913.png)

![image-20211231132222406](static/post/img/image-20211231132222406.png)

로컬 PC에 Key 파일을 다운받은 후, 중요한 파일이므로 권한을 400으로 변경

```bash
{21-12-31 13:29}P79305:~/Desktop/AWS minah.kim% chmod 400 aws-ec2-keypair-rsa.pem
{21-12-31 13:29}P79305:~/Desktop/AWS minah.kim% ll aws-ec2-keypair-rsa.pem
-r--------@ 1 minah.kim  679754705   1.7K Dec 31 13:21 aws-ec2-keypair-rsa.pem
```

![image-20211231133010725](static/post/img/image-20211231133010725.png)

```bash
{21-12-31 13:37}P79305:~/Desktop/AWS minah.kim% ssh -i "aws-ec2-keypair-rsa.pem" ec2-user@ec2-13-125-252-157.ap-northeast-2.compute.amazonaws.com
ssh: connect to host ec2-13-125-252-157.ap-northeast-2.compute.amazonaws.com port 22: Operation timed out
```

ssh 통신을 위해 인바운드 규칙에서 22번 포트를 열어줘야 했다. 보안설정을 변경해보자. [**참조 페이지**](https://qiita.com/yokoto/items/338bd80262d9eefb152e)



![image-20211231134023406](static/post/img/image-20211231134023406.png)

![image-20211231134303623](static/post/img/image-20211231134303623.png)

ssh를 내 IP로 추가



```bash
{22-01-03 2:51}P79305:~/Desktop/AWS minah.kim% ssh -i "aws-ec2-keypair-rsa.pem" centos@ec2-13-125-213-99.ap-northeast-2.compute.amazonaws.com
Activate the web console with: systemctl enable --now cockpit.socket
```

접속 완료



디스크 초기상태 확인

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
