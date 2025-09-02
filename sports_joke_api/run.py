from src import create_app
import os

def run():
    from waitress import serve
    app = create_app()
    
    port = int(os.getenv('PORT', 5555))
    serve(app, host='0.0.0.0', port=port)

if __name__ == "__main__":
    run()