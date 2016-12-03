from datetime import datetime
from time import sleep

from celery.utils.log import get_task_logger
from sqlalchemy.sql.functions import func

from papp_base.worker import CeleryDbConn
from papp_noop.storage.NoopTable import NoopTable
from papp_noop.worker.NoopCeleryApp import celeryApp
from txhttputil import toStr
from txcelery.defer import CeleryClient

logger = get_task_logger(__name__)


def add1(val):
    return val + 1

@CeleryClient
@celeryApp.task
def task1(inStr):
    logger.info("Received %s", inStr)
    sleep(1.0)
    return toStr(datetime.utcnow())


@CeleryClient
@celeryApp.task
def dbTask(string1):
    logger.info('Running')
    session = CeleryDbConn.getDbSession()
    session.add(NoopTable(string1=string1))
    session.commit()

    id = session.query(func.max(NoopTable.id))[0]

    return id