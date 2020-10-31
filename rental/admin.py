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

    # readonly_fields = ('user',)
    # exclude = ('user', )

    def save_model(self, request, obj, form, change):   # setea el campo user de property automagicamente al guardarlocament
        if not request.user.is_superuser:
            obj.user = request.user

        super(PropertyAdmin, self).save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super(PropertyAdmin, self).get_queryset(request)
        self.readonly_fields = ()

        if request.user.is_superuser:
            return qs

        self.readonly_fields = ('user',)    # si el que agrega la property es un anfitrion, no deja elegir el campo

        property_ct = ContentType.objects.get_for_model(Property)
        log_entries = Property.objects.filter(
            user=request.user
        )
        user_property_ids = [a.id for a in log_entries]
        return qs.filter(id__in=user_property_ids)

        
class ReservationAdmin(admin.ModelAdmin):

    readonly_fields = ('property', )

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
