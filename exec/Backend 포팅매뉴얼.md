# Backend 포팅매뉴얼

## 소개

diète Backend 빌드 매뉴얼

## 기술스택 및 라이브러리

| Project                | Version | Description     |
| ---------------------- | ------- | --------------- |
| Python                 | 3.10.1  |                 |
| Django                 | 3.2.9   |                 |
| djangorestframework    | 3.13.1  |                 |
| openpyxl               | 3.0.9   |                 |
| Pillow                 | 1.6.2   |                 |
| PyJWT                  | 9.0.1   |                 |
| mysql-connector-python | 8.0.28  | DB              |
| google-images-download | 2.8.0   | 이미지 다운로드 |
| VS Code                | 1.64.2  | IDE             |

## 개발 환경 구성

> Windows 10 기준으로 개발 환경 구성 방법을 설명한다.

### 1. Python 및 필요 라이브러리 설치

- **Python v3.7** 이상 권장

  - Python 공식 웹사이트 : https://www.python.org/downloads/

  - 설치 확인(CMD)

    ```bash
    > python
    Python 3.8.10 (default, Mar 15 2022, 12:22:08)
    [GCC 9.4.0] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    ```

  

- Python 설치 후 `{origin_DIR}/Server` 이동하여 필요 라이브러리 설치

  - > 가상환경 상태에서 설치
    >
    > `python -m venv {venv_name}`
    >
    > `source {venv_name}/Scripts/activate `
    >
    > `pip install -r requirements.txt`

  - `pip install -r requirements.txt`

  - Django 서버 로컬 구동 확인

    ```bash
    > python manage.py makemigrations
    > python manage.py migrate
    > python manage.py runserver
    ```

- WSGI[gunicorn] 설치

  - gunicorn 공식 웹사이트 : https://gunicorn.org/
  - 또는 개인 Terminal에서 `pip install gunicorn`
  - 설치확인

- 서버 시작

  - `sudo systemctl daemon-reload`
  -  `sudo systemctl start gunicorn`
  - `sudo systemctl status gunicorn.service `

  

### 2. DB 구성 

> 이미 설치되어 있거나 원격 DB를 사용하는 경우 설치 부분 생략

- MySQL 사이트에서 **Windows (x86, 32-bit), MSI Installer (435.7M)** 설치 파일 다운로드 및 실행
  -  MySQL 공식 웹사이트 : https://dev.mysql.com/downloads/mysql/

- 명령 프롬프트(cmd) 확인

  ```shell
  > mysql --version
  ```

- db_uploader.py 실행

  - cd Server 후 `python db_uploader.py` 

  - Server/datas 안에 있는 diète_data.xlsx 파일 DB 삽입 확인

    


### 3. 프로젝트 다운로드 및 설정

- 프로젝트 다운로드

  ```shell
  git clone -b BE <repo URL> servwr
  ```

- `Server/my_settings.py`

  ```properties
  DATABASES = {
      'default' : {
          'ENGINE': 'django.db.backends.mysql',
          'NAME': 'diete',
          'USER': 'diete',
          'PASSWORD': 'diete104',
          'HOST': 'j6b104.p.ssafy.io',
          'PORT': '3306',
      }
  }
  ```



## 디렉토리 구조

```
<-- Django -->
.{Server}
└─ datas /* 데이터 파일 */
└─ images /* 이미지 파일 */
└─ menus
	├─ ...
    ├─ urls.py	/* api 요청을 보내기 위한 url 매핑 파일 */
    └─ views.py	
└─ records
└─ search
└─ user
├─ db_uploader.py /* DB 데이터 저장 파일 */
├─ image_adapter.py
├─ image_crawler.py
├─ image_updater.py
├─ manage.py /* Django - Project 상호작용 연동 파일 */
└─ requirements.txt /* 필요 라이브러리 저장 파일 */
```

