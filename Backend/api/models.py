#!/usr/bin/env python3
"""
This module contains the users table config
"""

from api import db
from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as so

class User(db.Model):
    """
    This class contains the users table config
    """
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    username: so.Mapped[str] = so.mapped_column(sa.String(64), index=True,
                                                unique=True)
    email: so.Mapped[str] = so.mapped_column(sa.String(120), index=True,
                                             unique=True)
    password_hash: so.Mapped[Optional[str]] = so.mapped_column(sa.String(256))

    def __repr__(self):
        return '<User {}>'.format(self.username)
