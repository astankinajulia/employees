import logging

import aiohttp_jinja2
import jinja2
from aiohttp import web

import db
from config import config
from views import index

log = logging.getLogger('web')


async def make_app():
    db.start()

    app = web.Application()
    aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader(str(config.BASE_DIR + '/templates')))
    app.add_routes(
        [
            web.get('/employees', index),
        ]
    )

    return app
