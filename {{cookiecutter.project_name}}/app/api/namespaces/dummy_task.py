from flask_restx import Namespace, Resource, fields

from app.api.helpers.tasks import queue_redis_task

namespace = Namespace("dummy_task", description="Trigger dummy task")

parser = namespace.parser()
parser.add_argument(
    "nap_length", type=int, help="Length of time for the task to sleep", required=True
)

task_model = namespace.model(
    "Dummy Task",
    {"task_id": fields.String(required=True, description="The task details")},
)


@namespace.route("/")
@namespace.expect(parser)
class DummyTask(Resource):
    @namespace.doc("Queue dummy task")
    @namespace.marshal_with(task_model)
    def post(self):
        """Queue a dummy task with the nap length provided."""
        args = parser.parse_args()
        task_id = queue_redis_task("dummy_task", args["nap_length"])
        return {"task_id": task_id}
