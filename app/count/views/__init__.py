from flask import Blueprint

view = Blueprint(
    'view',
    __name__,
    static_folder="../../static",
    template_folder="../../temaplates"
    )

from . import count
