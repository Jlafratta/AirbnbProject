from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.admin.models import LogEntry, ADDITION
from django.contrib.contenttypes.models import ContentType

# Register your models here.

from .models import Property
from .models import PropertyImage
from .models import Reservation
from .models import ReservationDate
from .models import User


class ReservationDateInline(admin.TabularInline):
    model = ReservationDate
    fk_name = 'property'
    max_num = 7


class PropertyImageInline(admin.TabularInline):
    model = PropertyImage
    fk_name = 'property'
    max_num = 10


class PropertyAdmin(admin.ModelAdmin):
    inlines = [ReservationDateInline, PropertyImageInline, ]

    def get_queryset(self, request):
        qs = super(PropertyAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs

        property_ct = ContentType.objects.get_for_model(Property)
        log_entries = LogEntry.objects.filter(
            content_type=property_ct,
            user=request.user,
            action_flag=ADDITION
        )
        user_property_ids = [a.object_id for a in log_entries]
        return qs.filter(id__in=user_property_ids)


class ReservationAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        qs = super(ReservationAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs

        property_ct = ContentType.objects.get_for_model(Property)
        log_entries = LogEntry.objects.filter(
            content_type=property_ct,
            user=request.user,
            action_flag=ADDITION
        )
        user_property_ids = [a.object_id for a in log_entries]
        return qs.filter(id__in=user_property_ids)


# Admin models register
admin.site.register(Property, PropertyAdmin)
admin.site.register(Reservation, ReservationAdmin)
# admin.site.register(ReservationDate)
admin.site.register(User, UserAdmin)
