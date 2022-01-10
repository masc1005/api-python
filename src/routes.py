from flask import Blueprint
from .controllers.main import topic1, topic2, topic3

bp = Blueprint('roles', __name__)

bp.get('/list_users')(topic1)
bp.get('/list_alchemy')(topic2)
bp.get('/teste')(topic3)
