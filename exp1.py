from http.server import HTTPServer, BaseHTTPRequestHandler

content = """<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>List of Protocols</title>
</head>
<body bgcolor="blue">
    <table border="1" align="center" bgcolor="pink" cellpadding="10">
        <caption><b>List of Protocols</b></caption>
        <tr>
            <th>S.No.</th>
            <th>Name of the Layers</th>
            <th>Name of the Protocols</th>
        </tr>
        <tr>
            <td>1</td>
            <td>Application Layer</td>
            <td>HTTP, FTP, DNS, SMTP, SSH, HTTPS</td>
        </tr>
        <tr>
            <td>2</td>
            <td>Transport Layer</td>
            <td>TCP, UDP</td>
        </tr>
        <tr>
            <td>3</td>
            <td>Internet Layer</td>
            <td>IP, ICMP, IGMP</td>
        </tr>
        <tr>
            <td>4</td>
            <td>Network Access / Link Layer</td>
            <td>Ethernet, Wi-Fi, ARP</td>
        </tr>
    </table>
</body>
</html>"""   # <-- closed here with triple double-quotes

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("GET request received...")
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(content.encode())

print("This is my webserver")
server_address = ('', 8000)
httpd = HTTPServer(server_address, MyServer)
httpd.serve_forever()
