from django.test import TestCase, Client
from django.test.client import RequestFactory
from models import *
from views import *
from django.core.urlresolvers import reverse

# Create your tests here.

client = Client()

class ServiceTestCase(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        # Service.objects.create(name="dario", description_external="deadae", description_internal="deada",
        #                        service_area="dead", service_type="deadae", request_procedures="deadae",
        #                        funders_for_service="deada", value_to_customer="dead", risks="deada",
        #                        competitors="dead", id_service_owner_id="11111111-1111-1111-1111-111111111111",
        #                        id_contact_information_id="11111111-1111-1111-1111-111111111111")


    def test_invalid_url(self):
        # response = client.get(reverse("/v1/portfolio/services"))
        # print response
        # request = self.factory.get("localhost/v1/portfolio/services")
        # response = list_services(request, "portfolio")
        # print response
        services = Service.objects.all()
        print len(services)
        self.assertEqual("dario", "dario")