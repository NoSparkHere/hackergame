from django.test import TestCase
from .auth_providers.ustc import LoginView as USTCLoginView
from .auth_providers.sustech import LoginView as SUSTECHLoginView
from unittest import mock
from contextlib import contextmanager


USTC_CAS_EXAMPLE_RESPONSE = """<cas:serviceResponse xmlns:cas='http://www.yale.edu/tp/cas'>
<cas:authenticationSuccess>
<cas:user>SA21011000</cas:user>
<attributes>
<cas:xbm>1</cas:xbm>
<cas:logintime>2020-02-30 12:34:56</cas:logintime>
<cas:gid>2201234567</cas:gid>
<cas:loginip>192.0.2.0</cas:loginip>
</attributes>
</cas:authenticationSuccess>
</cas:serviceResponse>"""

SUSTECH_CAS_EXAMPLE_RESPONSE = """<cas:serviceResponse xmlns:cas='http://www.yale.edu/tp/cas'>
<cas:authenticationSuccess>
    <cas:user>11899999</cas:user>
    <cas:attributes>
      <cas:mail>11899999@mail.sustech.edu.cn</cas:mail>
      <cas:givenName>San</cas:givenName>
      <cas:sn>ZHANG</cas:sn>
      <cas:cn>ZHANG San</cas:cn>
    </cas:attributes>
  </cas:authenticationSuccess>
</cas:serviceResponse>"""


class MockResponse:
    def __init__(self, text):
        self.text = text

    def read(self):
        return self.text.encode("utf-8")


@contextmanager
def mock_urlopen(url, timeout=None):
    success = False
    if "ustc.edu.cn" in url:
        if "serviceValidate" in url:
            success = True
            yield MockResponse(USTC_CAS_EXAMPLE_RESPONSE)
    elif "sso.cra.ac.cn" in url:
        if "serviceValidate" in url:
            success = True
            yield MockResponse(SUSTECH_CAS_EXAMPLE_RESPONSE)
    if not success:
        raise ValueError("Unknown URL")


class AuthProviderCASServiceValidateTest(TestCase):
    @mock.patch("frontend.auth_providers.cas.urlopen", new=mock_urlopen)
    def test_ustc(self):
        v = USTCLoginView()
        v.service = "http://example.com/accounts/ustc/login/"
        v.ticket = "ST-1234567890"
        tree = v.check_ticket()
        self.assertEqual(tree.tag, "{http://www.yale.edu/tp/cas}authenticationSuccess")
        self.assertEqual(v.identity, "2201234567")
        self.assertEqual(v.sno, "SA21011000")

    @mock.patch("frontend.auth_providers.cas.urlopen", new=mock_urlopen)
    def test_sustech(self):
        v = SUSTECHLoginView()
        v.service = "http://example.com/accounts/sustech/login/"
        v.ticket = "ST-1234567890"
        tree = v.check_ticket()
        self.assertEqual(tree.tag, "{http://www.yale.edu/tp/cas}authenticationSuccess")
        self.assertEqual(v.identity, "11899999")
        self.assertEqual(v.mail, "11899999@mail.sustech.edu.cn")
        self.assertEqual(v.name, "ZHANG San")
