from __future__ import annotations
from django.contrib.admin import ModelAdmin, register
from .models import RefreshToken


@register(RefreshToken)
class RefreshTokenAdmin(ModelAdmin): # type: ignore
    list_display = (
        "pk",
        "user",
        "device_info",
        "revoked",
        "created_at",
        "last_used_at",
        "expires_at",
    )
    list_filter = (
        "revoked",
        "created_at",
        "expires_at",
        "device_info",
    )
    search_fields = (
        "jti",
        "device_info",
        "user__username",
        "user__email",
    )
    autocomplete_fields = ("user",)
    date_hierarchy = "created_at"
