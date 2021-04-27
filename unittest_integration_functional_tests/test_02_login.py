import unittest

class Authentication:
    USERS = [{"username": "user1",
              "password": "pwd1"}]

    def login(self, username, password):
        u = self.fetch_user(username)
        if not u or u["password"] != password:
            return None
        return u

    def fetch_user(self, username):
        for u in self.USERS:
            if u["username"] == username:
                return u
        else:
            return None


class Authorization:
    PERMISSIONS = [{"user": "user1",
                    "permissions": {"create", "edit", "delete"}}]

    def can(self, user, action):
        for u in self.PERMISSIONS:
            if u["user"] == user["username"]:
                return action in u["permissions"]
        else:
            return False

# In this specific case TestAuthentication and TestAuthorization are considered as unittest, namely units of tests taken in their isolation

class TestAuthentication(unittest.TestCase):
    def test_login(self):
        auth = Authentication()
        auth.USERS = [{"username": "testuser", "password": "testpass"}]

        resp = auth.login("testuser", "testpass")

        assert resp == {"username": "testuser", "password": "testpass"}


class TestAuthorization(unittest.TestCase):
    def test_can(self):
        authz = Authorization()
        authz.PERMISSIONS = [{"user": "testuser", "permissions": {"create"}}]

        resp = authz.can({"username": "testuser"}, "create")

        assert resp is True

# This is an example of integration test that tests two different components, namleu TestAuthentication and TestAuthorization

class TestAuthorizeAuthenticatedUser(unittest.TestCase):
    def test_auth(self):
        auth = Authentication()
        authz = Authorization()
        auth.USERS = [{"username": "testuser", "password": "testpass"}]
        authz.PERMISSIONS = [{"user": "testuser", "permissions": {"create"}}]

        u = auth.login("testuser", "testpass")
        resp = authz.can(u, "create")

        assert resp is True

if __name__ == '__main__':
    unittest.main()
