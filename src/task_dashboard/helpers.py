from typing import Any, Dict, cast

import flask


def titlize(value: str) -> str:
    return " ".join(map(str.capitalize, value.split(" ")))


def repr_task(log: Dict[str, Any]) -> str:
    if not log:
        return "Task data missing!"
    if "task" not in log:
        return cast(str, log["task_name"])
    func = log["task"].get("task_path", log["task_name"])
    args = ", ".join(map(repr, log["task"]["args"]))
    kwargs = ", ".join(k + "=" + repr(v) for k, v in log["task"]["kwargs"].items())
    all_args = ", ".join([args, kwargs])
    return f"{func}({all_args})"


def register_template_helpers(app: flask.Flask) -> None:
    app.template_filter("repr_task")(repr_task)
    app.template_filter("titlize")(titlize)
