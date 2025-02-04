import os
import subprocess
import webbrowser
from http.server import SimpleHTTPRequestHandler, HTTPServer

PORT = 9231
CSS_PATH = "./markdown.css"  # Updated to use local CSS file

# Convert Markdown file to HTML using Pandoc
def convert_md_to_html(md_file):
    html_file = f"/tmp/{os.path.basename(md_file)}.html"
    try:
        subprocess.run(
            ['pandoc', md_file, '-s', '-c', CSS_PATH, '-o', html_file],
            check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        return html_file
    except subprocess.CalledProcessError:
        return None

class MarkdownHTTPRequestHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        requested_path = self.path.strip('/')
        
        # Default to index.md if no file is requested
        if not requested_path:
            requested_path = "index.md"
        
        # If the file is a markdown file, convert it to HTML first
        if requested_path.endswith('.md'):
            file_path = os.path.join(os.getcwd(), requested_path)
            
            if os.path.isfile(file_path):
                html_file = convert_md_to_html(file_path)
                
                if html_file and os.path.isfile(html_file):
                    self.send_response(200)
                    self.send_header("Content-type", "text/html")
                    self.end_headers()
                    
                    with open(html_file, 'r') as f:
                        self.wfile.write(f.read().encode('utf-8'))
                else:
                    self.send_error(500, "Failed to convert Markdown to HTML")
            else:
                self.send_error(404, "File not found")
        else:
            # If it's not a markdown file, handle normally
            super().do_GET()

def run(server_class=HTTPServer, handler_class=MarkdownHTTPRequestHandler):
    server_address = ('', PORT)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server at http://localhost:{PORT}')
    
    # Open the index.md file in the default web browser
    webbrowser.open(f'http://localhost:{PORT}/index.md')
    
    httpd.serve_forever()

if __name__ == '__main__':
    run()

