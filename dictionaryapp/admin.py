from django.contrib import admin
from .models import chomolokko, bn, en, SearchLog

admin.site.register(chomolokko)
admin.site.register(bn)
admin.site.register(en)
admin.site.register(SearchLog)