from django.contrib import admin
from .models import Polls
from .models import Choice
from .models import User



admin.site.register(Polls)
admin.site.register(Choice)
admin.site.register(User)

