import os
import sys
import socket
import qrcode
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
        """
        Adds a Content-Disposition header to trigger file download for specific file types.

        This method overrides the default `end_headers` to include an additional header
        when files with certain extensions are accessed. It sets the "Content-Disposition"
        header, prompting the browser to download the file rather than displaying it directly
        in the browser window. If the file's extension matches any in the predefined list of
        downloadable extensions, the Content-Disposition header is set.
        """

        # Apply download prompt only to specific file types
        downloadable_extensions = (
            # Documents
            ".pdf",
            ".doc",
            ".docx",
            ".xls",
            ".xlsx",
            ".ppt",
            ".pptx",
            ".txt",
            ".odt",
            ".rtf",
            ".tex",
            ".wpd",
            # Images
            ".png",
            ".jpg",
            ".jpeg",
            ".gif",
            ".bmp",
            ".tiff",
            ".svg",
            ".ico",
            ".webp",
            # Audio
            ".mp3",
            ".wav",
            ".aac",
            ".ogg",
            ".flac",
            ".m4a",
            ".wma",
            ".aiff",
            # Video
            ".mp4",
            ".avi",
            ".mkv",
            ".mov",
            ".wmv",
            ".flv",
            ".webm",
            ".3gp",
            ".mpeg",
            ".m4v",
            # Archives and Compressed Files
            ".zip",
            ".tar",
            ".gz",
            ".tar.gz",
            ".rar",
            ".7z",
            ".bz2",
            ".xz",
            ".tgz",
            ".iso",
            # Code Files
            ".js",
            ".css",
            ".html",
            ".py",
            ".java",
            ".cpp",
            ".cs",
            ".php",
            ".rb",
            ".go",
            ".pl",
            ".rs",
            ".swift",
            ".ts",
            # Data Files
            ".csv",
            ".json",
            ".xml",
            ".yaml",
            ".yml",
            ".sql",
            ".db",
            ".dbf",
            ".mdb",
            ".log",
            # Executables
            ".exe",
            ".msi",
            ".bat",
            ".sh",
            ".bin",
            ".dmg",
            ".pkg",
            # Other
            ".epub",
            ".mobi",
            ".azw3",
            ".ics",
            ".vcf",
        )

        if self.path.endswith(downloadable_extensions):
            self.send_header(
                "Content-Disposition",
                f'attachment; filename="{os.path.basename(self.path)}"',
            )
        super().end_headers()


def get_ip():
    """
    Retrieves the local machine's primary IP address.

    This function establishes a UDP connection to Google's public DNS server (8.8.8.8)
    to retrieve the local IP address used for network communication. This method
    ensures that the correct local network IP is returned, rather than the localhost
    (127.0.0.1). In the event of a failure, it defaults to returning "127.0.0.1" and
    prints an error message.

    Returns:
        str: The IP address of the machine or "127.0.0.1" if retrieval fails.
    """

    # Connect to an external host to get the primary IP address
    try:
        # Attempt to connect to a common public IP (Google's DNS server)
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.connect(("8.8.8.8", 80))
            ip = s.getsockname()[0]
    except Exception as e:
        print(
            f"{Color.RED}Error: Retrieving IP failed. Cannot retrieve your machine IP.{Color.RESET}"
        )
        ip = "127.0.0.1"  # Default to localhost if unable to retrieve IP

    return ip


def generate_qr_code(link):
    """
    Generates and displays a QR code for a given link.

    This function creates a QR code using the `qrcode` library, encoding the provided
    link as a QR code image. The generated QR code is displayed on the screen, allowing
    users to scan it to easily access the link on their mobile devices.

    Args:
        link (str): The URL or link to encode in the QR code.
    """

    # Generate a QR code for the provided link
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(link)
    qr.make(fit=True)

    # Generate and display the QR code
    img = qr.make_image(fill="black", back_color="white")
    img.show()


def start_server(directory, port=8080):
    """
    Starts an HTTP server in the specified directory, serving files and displaying access options.

    This function changes the current working directory to the specified path and sets up
    an HTTP server using `CustomHTTPRequestHandler` to handle requests. It retrieves the
    local IP address, creates an access link, and displays both the link and a QR code
    for easy access. The server runs indefinitely, listening on the specified port.

    Args:
        directory (str): The directory path from which files will be served.
        port (int, optional): The port on which the server will listen. Defaults to 8080.
    """

    # Change the current working directory to the specified directory
    os.chdir(directory)

    # Get the local IP address and generate the network link
    ip = get_ip()
    link = f"http://{ip}:{port}"

    # Start the server with the custom request handler
    with socketserver.TCPServer(("", port), CustomHTTPRequestHandler) as httpd:
        print(f"{Color.GREEN}Serving files from '{directory}' on: {link}{Color.RESET}")
        print(f"{Color.CYAN}Press Ctrl+C to stop the server.{Color.RESET}")

        # Display options to open by link or QR code
        print(
            f"\n{Color.GREEN}To access the server, use one of the following options:{Color.RESET}"
        )
        print(
            f"{Color.CYAN}  1. Open the following link in your browser: {link}{Color.RESET}"
        )
        print(
            f"{Color.CYAN}  2. Or scan the QR code to access from your device:{Color.RESET}\n"
        )

        # Generate and display the QR code
        generate_qr_code(link)

        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print(f"\n{Color.YELLOW}Server is stopping...{Color.RESET}")
        finally:
            httpd.server_close()
            print(f"{Color.YELLOW}Server stopped.{Color.RESET}")


if __name__ == "__main__":
    """
    Main entry point for the script.

    This block checks for a command-line argument specifying the directory to serve.
    If provided, it verifies whether the directory exists:
    - If the directory is valid, it starts the server in the specified directory.
    - If no directory is provided or if the specified path is invalid, it displays an
      error message and exits the program.

    Expected Usage:
        python script_name.py <directory_path>
    """

    # Use directory argument from the command line
    if len(sys.argv) > 1:
        directory = sys.argv[1]
    else:
        print(f"{Color.RED}Error: No directory path provided.{Color.RESET}")
        sys.exit(1)

    # Check if the directory exists
    if os.path.isdir(directory):
        # Start the server if the directory is valid
        start_server(directory, port=8080)
    else:
        print(f"{Color.RED}Error: The specified directory does not exist.{Color.RESET}")
