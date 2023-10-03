from app import create_app

app = create_app()

with app.app_context():
    from app import models

    from app import admin_views

    admin_views.admin_views()

if __name__ == "__main__":
    app.run(debug=True)
