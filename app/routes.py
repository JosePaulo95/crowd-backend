from flask import jsonify

def configure_routes(app):
    
    @app.route('/youtube/<video_id>/timed-comments/')
    def get_timed_comments(video_id):
        # Lógica aqui
        return jsonify({"message": "Timed comments for video " + video_id})
    
    @app.route('/youtube/<video_id>/live-comments/')
    def get_live_comments(video_id):
        # Lógica aqui
        return jsonify({"message": "Live comments for video " + video_id})
