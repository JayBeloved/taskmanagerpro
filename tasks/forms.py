from django.db import models
from tasks import models

spt = Categories(category="Spiritual", description="Things spirtually inclined", catcode="spt")

spt.save()
