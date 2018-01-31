import yaml

from django.conf import settings
from apimas.django.adapter import DjangoAdapter


with open(settings.FILEPATH_SPEC, 'r') as apimasfile:
        spec = yaml.safe_load(apimasfile)

adapter = DjangoAdapter()
adapter.construct(spec)
