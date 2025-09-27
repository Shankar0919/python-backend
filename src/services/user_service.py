def transform_user_data(data):
    return {
        "id": data.get("id"),
        "name": data.get("name").title(),
        "active": str(data.get("active")).lower() in ["true", "1", "yes"],
        "dob": data.get("dob")
    }
