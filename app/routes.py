from flask import jsonify

from app.contexts.index import get_all_contexts


def configure_routes(app):
    @app.route("/")
    def get_contexts():
        return jsonify({"contexts": get_all_contexts()})

    # @app.route('/youtube/<video_id>/timed-comments/')
    # def get_timed_comments(video_id):
    #     # Lógica aqui
    #     return jsonify({"message": "Timed comments for video " + video_id})

    # @app.route('/youtube/<video_id>/live-comments/')
    # def get_live_comments(video_id):
    #     # Lógica aqui
    #     return jsonify({"message": "Live comments for video " + video_id})
