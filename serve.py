#!/usr/bin/env python3
import http.server
import socketserver
import sys
import webbrowser
from pathlib import Path

PORT = 8000
DIRECTORY = Path(__file__).parent.resolve()

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(DIRECTORY), **kwargs)

    def log_message(self, format, *args):
        # Custom clean log output
        sys.stdout.write(f"[{self.log_date_time_string()}] {format % args}\n")

def run_server(port=PORT):
    handler = CustomHTTPRequestHandler
    
    # Allow port reuse
    socketserver.TCPServer.allow_reuse_address = True
    
    try:
        with socketserver.TCPServer(("", port), handler) as httpd:
            url = f"http://localhost:{port}"
            print("=" * 55)
            print(f" 🚀 카페 룰렛 웹 서버가 시작되었습니다!")
            print(f" 🌐 접속 주소: \033[1;36m{url}\033[0m")
            print(f" 📁 서빙 디렉토리: {DIRECTORY}")
            print(f" 🛑 종료하려면 Ctrl+C 를 누르세요.")
            print("=" * 55)
            
            # Automatically try to open in default browser
            try:
                webbrowser.open(url)
            except Exception:
                pass
                
            httpd.serve_forever()
    except OSError as e:
        if e.errno == 48 or "Address already in use" in str(e):
            print(f"⚠️  포트 {port}가 이미 사용 중입니다. 포트 {port + 1}로 재시도합니다.")
            run_server(port + 1)
        else:
            print(f"❌ 서버 실행 중 오류 발생: {e}")
    except KeyboardInterrupt:
        print("\n👋 서버를 안전하게 종료합니다.")
        sys.exit(0)

if __name__ == "__main__":
    port = PORT
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        port = int(sys.argv[1])
    run_server(port)
