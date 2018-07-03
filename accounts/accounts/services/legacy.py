"""
Provide service API for legacy sessions.

This maps modules and functions required by the accounts service to
corresponding objects in the :mod:`arxiv.users.legacy` module.
"""

from arxiv.users import legacy

init_app = legacy.util.init_app
create_all = legacy.util.create_all
transaction = legacy.util.transaction
models = legacy.models
drop_all = legacy.util.drop_all
exceptions = legacy.exceptions
create = legacy.sessions.create
invalidate = legacy.sessions.invalidate
load = legacy.sessions.load