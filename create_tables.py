#!/usr/bin/env python

if __name__ == "__main__":
    from app import db
    from app.models import *

    db.create_all()
    db.session.commit()