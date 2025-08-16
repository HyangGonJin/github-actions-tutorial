import pytest
from app import app


# 1. 테스트용 클라이언트를 생성하는 'fixture'
@pytest.fixture
def client():
    # 2. 앱을 테스트 모드로 설정
    app.config["TESTING"] = True
    # 3. 테스트 클라이언트 생성
    with app.test_client() as client:
        # 4. 테스트 함수에 클라이언트 전달
        yield client


# 5. 실제 테스트를 수행하는 함수
def test_hello_world(client):
    # 6. '/' 경로로 GET 요청을 보냄
    rv = client.get("/")
    # 7. 응답 데이터에 'Hello, World!'가 포함되어 있는지 확인
    assert b"Hello, World!" in rv.data
