from flask import jsonify
from app.repositories.index import get_all_contexts_repository, get_context_repository


def configure_routes(app):
    @app.route("/")
    def get_contexts_controller():
        return jsonify({"contexts": get_all_contexts_repository()})

    @app.route("/<context_id>/<video_id>/timed-comments/")
    def get_timed_comments_controller(context_id: str, video_id: str):
        context = get_context_repository(context_id)
        coments = context["timed_comments_service"].get_by_video_id(video_id)

        return jsonify({"timed-comments": coments})
