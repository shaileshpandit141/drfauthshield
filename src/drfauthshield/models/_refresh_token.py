from __future__ import annotations
from typing import cast
from datetime import datetime
from uuid import UUID, uuid4
from django.db.models import (
    Model,
    UUIDField,
    ForeignKey,
    CASCADE,
    BooleanField,
    CharField,
    DateTimeField,
    Index,
)
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model

User = cast(AbstractUser, get_user_model())


class RefreshToken(Model):
    class Meta:
        db_table = "refresh_tokens"
        ordering = ["-created_at"]
        indexes = [
            Index(fields=["user"]),
            Index(fields=["expires_at"]),
            Index(fields=["revoked"]),
        ]
        verbose_name = "Refresh Token"
        verbose_name_plural = "Refresh Tokens"

    jti: UUIDField[UUID, UUID] = UUIDField(
        primary_key=True, default=uuid4, editable=False
    )
    user: ForeignKey[AbstractUser, AbstractUser] = ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=CASCADE
    )
    revoked: BooleanField[bool, bool] = BooleanField(default=False)
    replaced_by: UUIDField[UUID | None, UUID | None] = UUIDField(null=True, blank=True)
    device_info: CharField[str, str] = CharField(max_length=255, blank=True)
    created_at: DateTimeField[datetime, datetime] = DateTimeField(auto_now_add=True)
    expires_at: DateTimeField[datetime, datetime] = DateTimeField()
    last_used_at: DateTimeField[datetime | None, datetime | None] = DateTimeField(
        null=True, blank=True
    )

    def is_expired(self) -> bool:
        return timezone.now() >= self.expires_at

    def __str__(self) -> str:
        username_field = getattr(self.user, User.USERNAME_FIELD)
        return str(username_field)
