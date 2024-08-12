import os
from app import create_app

app = create_app()

def save_static(url, output_path):
    with app.test_request_context(url):
        response = app.full_dispatch_request()
        with open(output_path, 'w') as f:
            f.write(response.get_data(as_text=True))

if __name__ == "__main__":
    # Define the pages you want to freeze
    pages = [
        ('/', 'index.html'),
        ('/resume', 'resume.html'),
        ('/projects', 'projects.html'),
        ('/contact', 'contact.html')
    ]

    for page in pages:
        url, output_file = page
        output_path = os.path.join('build', output_file)
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        save_static(url, output_path)

    print("Static files have been generated in the 'build' directory.")