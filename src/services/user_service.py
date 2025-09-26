def transform_user_data(data: dict) -> dict:
    data["name"] = data["name"].strip().title()
    return data
