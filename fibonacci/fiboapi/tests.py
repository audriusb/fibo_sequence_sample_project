"""
App tests
"""
from rest_framework.test import APIRequestFactory, APITestCase
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from django.http.request import HttpRequest

from fibonacci.fiboapi.views import FiboSeqView
from fibonacci.fiboapi.generators import Fibonacci_Sequence


class FiboSequenceTestCase(APITestCase):
    def setUp(self):
        self.request_factory = APIRequestFactory()
        self.view = FiboSeqView()

    def _request_get(self, params):
        bad_req = Request(HttpRequest()) #make instance
        bad_req._request.GET = params #add bad values
        return bad_req

    def test_generator_should_return_dict_with_sequence(self):
        result = Fibonacci_Sequence().generate_fibonnaci_seq(0,2)

        #must be a dict
        self.assertIsInstance(result, dict)

        #must contain sequence
        self.assertIsInstance(result['sequence'], list)
        self.assertEqual(len(result['sequence']), 2)

    def test_generator_shuould_raise_index_error(self):
        with self.assertRaises(IndexError): #negative start
            Fibonacci_Sequence().generate_fibonnaci_seq(-1,2)
        with self.assertRaises(IndexError): #end < start
            Fibonacci_Sequence().generate_fibonnaci_seq(3,2)
        with self.assertRaises(IndexError): #end too big
            Fibonacci_Sequence().generate_fibonnaci_seq(0,1000000)

    def test_api_should_return_error(self):
        bad_resp = Response({'error': 'Invalid range requested'}, 
            status=status.HTTP_400_BAD_REQUEST) #expect error

        #try too big number
        bad_req = self._request_get({'length':'1000000000'})  
        self.assertEqual(self.view.list(bad_req).status_code, bad_resp.status_code,)
        self.assertEqual(self.view.list(bad_req).data, bad_resp.data)

        #try invalid number
        bad_req = self._request_get({'length':'-1'}) 
        self.assertEqual(self.view.list(bad_req).status_code, bad_resp.status_code,)
        self.assertEqual(self.view.list(bad_req).data, bad_resp.data)

        #try non integer
        bad_req = self._request_get({'length':'aasda.sdasd'})  
        self.assertEqual(self.view.list(bad_req).status_code, bad_resp.status_code,)
        self.assertEqual(self.view.list(bad_req).data, bad_resp.data)

        #try without param
        bad_req = self._request_get({})  
        self.assertEqual(self.view.list(bad_req).status_code, bad_resp.status_code,)
        self.assertEqual(self.view.list(bad_req).data, bad_resp.data)

    def test_api_should_return_sequence(self):
        good_req = self._request_get({'length':'5'})  

        #must return List
        self.assertIsInstance(self.view.list(good_req).data['sequence'], list)

        #must return status 200
        self.assertEqual(self.view.list(good_req).status_code, status.HTTP_200_OK)

        #must return fibonacci sequence
        self.assertEqual(self.view.list(good_req).data['sequence'], [0, 1, 1, 2, 3])
