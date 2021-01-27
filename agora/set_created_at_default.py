import pytz
from datetime import datetime
from service.models import Resource
from accounts.models import Organisation

resources = Resource.objects.all()
organisations = Organisation.objects.all()

CREATED_AT = datetime(2020, 12, 31, 0, 0, tzinfo=pytz.UTC)

for r in resources:
    r.created_at = CREATED_AT
    r.save()

for o in organisations:
    o.created_at = CREATED_AT
    o.save()
