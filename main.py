import os
import http.server
import socketserver


# ANSI escape codes for colors
class Color:
    RED = "\033[91m"  # Error
    CYAN = "\033[96m"  # Information
    BLUE = "\033[94m"  # Input
    GREEN = "\033[92m"  # Success
    YELLOW = "\033[93m"  # Warning
    RESET = "\033[0m"  # Reset


class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Force download for all file types
        self.send_header(
            "Content-Disposition",
            f'attachment; filename="{os.path.basename(self.path)}"',
        )
        super().end_headers()


def start_server(directory, port=8080):
    # Change the current working directory to the specified directory
    os.chdir(directory)

    # Start the server with the custom request handler
    with socketserver.TCPServer(("", port), CustomHTTPRequestHandler) as httpd:
        print(
            f"{Color.GREEN}Serving files from '{directory}' on: http://localhost:{port}{Color.RESET}"
        )
        print(f"{Color.CYAN}Press Ctrl+C to stop the server.{Color.RESET}")

        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print(f"{Color.YELLOW}\nServer is stopping...{Color.RESET}")
        finally:
            httpd.server_close()
            print(f"{Color.YELLOW}Server stopped.{Color.RESET}")


if __name__ == "__main__":
    # Prompt the user to enter the directory path
    directory = input(
        f"{Color.BLUE}Enter the full path of the directory to serve: {Color.RESET}"
    )

    # Check if the directory exists
    if os.path.isdir(directory):
        # Start the server if the directory is valid
        start_server(directory, port=8080)
    else:
        print(f"{Color.RED}Error: The specified directory does not exist.{Color.RESET}")
