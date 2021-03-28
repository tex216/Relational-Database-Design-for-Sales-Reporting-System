from django.contrib import admin

from .models import STORE, CHILDCARE, CITY, PRODUCT, SELL,DAY, SALE
from .models import CATEGORY, ASSIGNED, HOLIDAY, DISCOUNT, ADVERTISIN_GCAMPAIGN, HOLD

admin.site.register(STORE)
admin.site.register(CHILDCARE)
admin.site.register(CITY)
admin.site.register(PRODUCT)
admin.site.register(SELL)
admin.site.register(DAY)
admin.site.register(SALE)
admin.site.register(CATEGORY)
admin.site.register(ASSIGNED)
admin.site.register(HOLIDAY)
admin.site.register(DISCOUNT)
admin.site.register(ADVERTISIN_GCAMPAIGN)
admin.site.register(HOLD)