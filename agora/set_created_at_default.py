import pytz
from datetime import datetime
from django.utils import timezone
from service.models import Resource
from accounts.models import Organisation

resources = Resource.objects.all()
organisations = Organisation.objects.all()
published_resources = Resource.objects.filter(state='published')
published_organisations = Resource.objects.filter(state='published')

CREATED_AT = datetime(2020, 12, 31, 0, 0, tzinfo=pytz.UTC)
NOW = datetime.now(timezone.utc)

for r in resources:
    r.created_at = CREATED_AT
    r.save()

for o in organisations:
    o.created_at = CREATED_AT
    o.save()

for p in published_resources:
    p.published_at = NOW
    p.save()

for o in published_organisations:
    o.published_at = NOW
    o.save()
