def register_user(email, name):
    if not email:
        raise ValueError("Email is required")
    print(f"Registering user: {name} with email: {email}")
