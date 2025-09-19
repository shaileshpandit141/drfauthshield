from typing import TypedDict
from datetime import timedelta


class JwtKeyDict(TypedDict):
    """RSA/ECDSA Key configuration for signing and verifying JWTs."""

    PRIVATE: str
    PUBLIC: str
    KID: str


class TokenLifeTimeDict(TypedDict):
    """Defines the lifetimes for access and refresh tokens."""

    ACCESS: timedelta
    REFRESH: timedelta


class DrfAuthShieldSettingsDict(TypedDict):
    """Configuration for JWT-based authentication."""

    ISSUER: str
    AUDIENCE: str
    SUBJECT_CLAIM: str
    KEYS: JwtKeyDict
    LIFETIME: TokenLifeTimeDict
    ALGORITHM: str
