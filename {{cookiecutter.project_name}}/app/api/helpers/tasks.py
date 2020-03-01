from flask import current_app


def queue_redis_task(task_name: str, *args):
    """
    Create and queue an rq task which executes the input function with the args
    provided.
    """
    current_app.task_queue.enqueue(f"app.rq_tasks.{task_name}", *args)
