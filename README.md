# 0. 세팅
- 회원 가입 유스 케이스
    a. 전달 받은 이메일과 패스워드를 User 테이블에 저장한다.
    b. 중복된 이메일이 존재한다면 에러를 발생시킨다.
    c. 패스워드는 사람이 읽지 못하게 암호화 되어야 한다.

# 1. 세팅
## API Test
1. openapi docs (swagger)
    - http://127.0.0.1:8000/docs
2. curl
    - ``curl -X GET http://localhost:8000 | jq``
3. postman

## DB
``docker run --name mysql-local -p 3306:3306/tcp -e MYSQL_ROOT_PASSWORD=test -d mysql:8``

# 2. 구현

### user
- 회원 리소스
