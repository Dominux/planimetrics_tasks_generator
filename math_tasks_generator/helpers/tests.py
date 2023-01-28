from typing import Type

from math_tasks_generator.base import MathTask, MathTaskGenerator
from math_tasks_generator.helpers.functions import get_task_path


def test_math_task(math_task: Type[MathTask], task_gen: Type[MathTaskGenerator]):
    path = get_task_path(math_task)

    for i in range(10):
        # Creating path
        path_i = path / str(i)
        path_i.mkdir(parents=True, exist_ok=True)
        filepath = path_i / str(math_task._task_number)

        # Generating params and task
        params = task_gen.gen_params()
        task = math_task(params)

        # Saving prompt
        with filepath.with_suffix(".txt").open("w") as f:
            f.write(task.prompt)

        # Saving vector
        with filepath.with_suffix(".svg").open("w") as f:
            f.write(task.vector)
