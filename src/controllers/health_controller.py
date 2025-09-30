from flask import jsonify


def health_check():
    return jsonify({
        "message": "Shankar Python Backend Application is Up and Running successfully"
    }), 200
