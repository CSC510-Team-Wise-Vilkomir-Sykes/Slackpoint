from copy import deepcopy

from models import *

class ViewDeadlineTasks:
    def __init__(self):
        """
        Initialise ViewTasks Class. Set progress for filtering tasks.

        :param progress: Optional Filter on tasks according to their progress.
        :type progress: float
        :raise:
        :return: ViewPoints object
        :rtype: ViewPoints object

        """
        self.payload = {"response_type": "ephemeral", "blocks": []}
    
    def get_list(self):
        """
        Return a list of tasks formatted in a slack message payload.

        :param None:
        :type None:
        :raise None:
        :return: Slack message payload with list of tasks.
        :rtype: dict

        """
        tasks = []
        # db query to get all tasks that have progress < 1
        
        tasks_with_deadline = (
            Task.query.join(Assignment)
            .add_columns(
                Assignment.user_id,
                Assignment.progress,
                Task.task_id,
                Task.points,
                Task.description,
                Task.deadline,
            )
            .filter(Task.deadline == datetime.utcnow().strftime("%Y-%m-%d"))
            .filter(Assignment.progress < 1)
            .all()
        )
        tasks.extend(tasks_with_deadline)

        # parse them
        for task in tasks:
            point = deepcopy(self.base_point_block_format)
            point["text"]["text"] = point["text"]["text"].format(
                id=task.task_id,
                points=task.points,
                description=task.description,
                deadline=task.deadline,
            )
            self.payload["blocks"].append(point)
        if not self.payload["blocks"]:
            self.payload["blocks"].append(
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": ">Currently there are no SlackPoints available",
                    },
                }
            )
        return self.payload

