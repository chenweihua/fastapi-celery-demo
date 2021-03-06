from datetime import timedelta

from celery import Celery

celery_app = Celery(
    'worker',
    backend='redis://:123456@127.0.0.1:6379/0',  # 存储结果
    broker='redis://:123456@127.0.0.1:6379/1'  # 消息中间件
)

celery_app.conf.task_routes = {
    "worker.celery_worker.test_celery": "test-queue",
    "worker.celery_worker.add": "test-queue",
    "worker.celery_worker.add1": "test-queue",
}
celery_app.conf.update(
    task_track_started=True,
    beat_schedule = {
        'ptask':{
            'task':'worker.celery_worker.beat_task',
            'schedule':timedelta(seconds=5)
        }
    },
    timezone = 'Asia/Shanghai'
)
