import sys, os
import json
import azure.functions as func

# Thêm project root vào sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from function_app import HelloApi

def test_helloapi_with_name():
    # giả lập request GET có query string ?name=Tram
    req = func.HttpRequest(
        method="GET",
        url="/api/HelloApi",
        params={"name": "Tram"},
        body=b""   # body rỗng, tránh NoneType lỗi
    )

    resp = HelloApi(req)

    assert resp.status_code == 200
    assert "Hello, Tram" in resp.get_body().decode()

def test_helloapi_without_name():
    # giả lập request GET không có query
    req = func.HttpRequest(
        method="GET",
        url="/api/HelloApi",
        params={},
        body=b""   # body rỗng
    )

    resp = HelloApi(req)

    assert resp.status_code == 200
    body = resp.get_body().decode()
    assert "Pass a name" in body

def test_helloapi_post_with_body():
    # giả lập POST request có JSON body
    body = json.dumps({"name": "Tram"}).encode("utf-8")
    req = func.HttpRequest(
        method="POST",
        url="/api/HelloApi",
        params={},
        body=body
    )

    resp = HelloApi(req)

    assert resp.status_code == 200
    assert "Hello, Tram" in resp.get_body().decode()
