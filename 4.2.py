from flask import Flask, jsonify, request
import json
import os

app = Flask(__name__)

DATA_FILE = "users.json"


# ---------- helpers ----------
def load_users():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_users(users):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(users, f, indent=2, ensure_ascii=False)


def response(status: str, data=None, message=""):
    return jsonify({
        "status": status,
        "data": data,
        "message": message
    })


# ---------- routes ----------
@app.route("/users", methods=["GET"])
def get_users():
    users = load_users()
    return response("success", users, "Список користувачів")


@app.route("/users", methods=["POST"])
def create_user():
    users = load_users()
    payload = request.json

    if not payload or "name" not in payload:
        return response("error", None, "Поле 'name' обовʼязкове"), 400

    new_id = max([u["id"] for u in users], default=0) + 1
    user = {
        "id": new_id,
        "name": payload["name"]
    }

    users.append(user)
    save_users(users)

    return response("success", user, "Користувача створено"), 201


@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    users = load_users()
    user = next((u for u in users if u["id"] == user_id), None)

    if not user:
        return response("error", None, "Користувача не знайдено"), 404

    return response("success", user, "Користувач знайдений")


@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    users = load_users()
    payload = request.json

    for user in users:
        if user["id"] == user_id:
            user["name"] = payload.get("name", user["name"])
            save_users(users)
            return response("success", user, "Користувача оновлено")

    return response("error", None, "Користувача не знайдено"), 404


@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    users = load_users()
    new_users = [u for u in users if u["id"] != user_id]

    if len(new_users) == len(users):
        return response("error", None, "Користувача не знайдено"), 404

    save_users(new_users)
    return response("success", None, "Користувача видалено")


if __name__ == "__main__":
    app.run(debug=True)
