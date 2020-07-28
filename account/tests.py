from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIRequestFactory, APIClient

from .views import AccountView, AccountUsernameAccessibilityView
from .models import User

# Create your tests here.
class AccountTest(TestCase):
    fixtures = ["testdatabase.yaml"]

    # setup test case
    def setUp(self):
        self.base_url = "/api/account"
        self.factory = APIRequestFactory()
        self.view = AccountView.as_view()

    # test adding a user
    def testA_add_user(self):
        request_data = {
            "username": "unittesuser01",
            "email": "unittesuser01@soj.ac.cn",
            "password": "unittest",
        }

        request = self.factory.post(self.base_url, data=request_data, format="json")
        res = self.view(request)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        res_json = res.data
        self.assertEqual(type(res_json["res"]["id"]), int)

    def testB_get_user(self):
        user_data = {
            "id": 1,
            "username": "admin",
            "introduction": "# Hello World!",
            "email": "admin@soj.ac.cn",
            "lang": 0,
            "is_staff": True,
            "is_active": True,
            "is_superuser": True,
        }

        request = self.factory.get(self.base_url)
        res = self.view(request, uid=1)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

        res_json = res.data
        res_data = res_json["res"]

        self.assertEqual(res_data.get("id"), user_data["id"])
        self.assertEqual(res_data.get("username"), user_data["username"])
        self.assertEqual(res_data.get("introduction"), user_data["introduction"])
        self.assertEqual(res_data.get("lang"), user_data["lang"])
        self.assertEqual(res_data.get("is_staff"), user_data["is_staff"])
        self.assertEqual(res_data.get("is_active"), user_data["is_active"])
        self.assertEqual(res_data.get("is_superuser"), user_data["is_superuser"])

    def testC_get_404_user(self):
        request = self.factory.get(self.base_url)
        res = self.view(request, uid=-1)
        self.assertEqual(res.status_code, status.HTTP_404_NOT_FOUND)

    def testE_add_exit_user(self):
        request_data = {
            "username": "unittesuser02",
            "email": "unittesuser02@soj.ac.cn",
            "password": "unittest",
        }

        request = self.factory.post(self.base_url, data=request_data, format="json")
        self.view(request)

        request = self.factory.post(self.base_url, data=request_data, format="json")
        res = self.view(request)
        self.assertEqual(res.status_code, status.HTTP_409_CONFLICT)

    def testF_add_user_miss_sth(self):
        request_data = {
            "username": "unittesuser03",
            "email": "unittesuser03@soj.ac.cn",
        }

        request = self.factory.post(self.base_url, data=request_data, format="json")
        res = self.view(request)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def testG_get_user_miss_uid(self):
        request = self.factory.get(self.base_url, format="json")
        res = self.view(request)
        self.assertEqual(res.status_code, status.HTTP_404_NOT_FOUND)


class AccountSessionTest(TestCase):
    fixtures = ["testdatabase.yaml"]

    def setUp(self):
        self.base_url = "/api/account/session"
        self.client = APIClient()

    def testA_create_session(self):
        request_data = {
            "username": "admin",
            "password": "123456",
        }

        res = self.client.post(self.base_url, request_data)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        sid_cookie = res.cookies.get("sessionid")
        self.assertIsNotNone(sid_cookie)
        self.assertEqual(sid_cookie["samesite"], "none")
        self.assertEqual(sid_cookie["path"], "/")

    def testB_logout_session(self):
        user = User.objects.get(username="ztl")
        self.client.force_authenticate(user=user)
        res = self.client.delete(self.base_url)
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)


class AccountUsernameAccessibilityTest(TestCase):
    def setUp(self):
        self.base_url = "/api/account/username/accessibility/"
        self.factory = APIRequestFactory()
        self.view = AccountUsernameAccessibilityView.as_view()

    def testZ_get_accessibility_ok(self):
        request = self.factory.get(self.base_url)
        response = self.view(response, username="unittest")

        self.assertEqual(response.status_data, status.HTTP_204_NO_CONTENT)

    def testZ_get_accessibility_ok(self):
        request = self.factory.get(self.base_url)
        response = self.view(request, username="admin")

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
