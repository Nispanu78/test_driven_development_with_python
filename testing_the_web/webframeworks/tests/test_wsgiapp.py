import webtest


class TestWSGIApp:
    def test_home(self, wsgiapp):
        client = webtest.TestApp(wsgiapp)

        response = client.get("http://httpbin.org/").text

        assert 'Hello World' in response