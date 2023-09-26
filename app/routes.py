from flask import jsonify
from app.errors.errors import (
    InvalidPlatformError,
    NetworkErrorException,
    QuotaExceededException,
    ExternalServiceFieldException,
)
from app.repositories.index import get_all_contexts_repository, get_context_repository


def configure_routes(app):
    @app.route("/")
    def get_contexts_controller():
        return jsonify({"contexts": get_all_contexts_repository()})

    @app.route("/platform/<platform>/video/<video_id>/timed-comments/")
    def get_timed_comments_controller(platform: str, video_id: str):
        try:
            context = get_context_repository(platform)
            coments = context["comments_service"].get_by_video_id(video_id)
            return jsonify({"timed-comments": coments})
        except InvalidPlatformError as e:
            return jsonify({"error": str(e)}), 400
        except ExternalServiceFieldException as e:
            return jsonify({"error": str(e)}), 400
        except QuotaExceededException as e:
            return jsonify({"error": str(e)}), 403
        except NetworkErrorException as e:
            return jsonify({"error": str(e)}), 403
