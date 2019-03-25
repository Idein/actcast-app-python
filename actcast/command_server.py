import io, socket, threading
from PIL import Image


class CommandServer(threading.Thread):
    def __init__(self, sock_path):
        super(CommandServer, self).__init__()
        self.sock_path = sock_path
        self.event = threading.Event()
        self.event.clear()
        self.img_lock = threading.Lock()
        self.img = None

    def run(self):

        # Wait photo
        while not self.event.is_set():
            with self.img_lock:
                if self.img is None:
                    continue
                else:
                    break
        if self.img is None:
            return

        s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        try:
            os.unlink(self.sock_path)
        except FileNotFoundError as e:
            pass # ignore
        s.bind(self.sock_path)
        s.settimeout(1)
        s.listen(1)
        while not self.event.is_set():
            try:
                conn, addr = s.accept()
                [request_id, command_id, command_data_length] = map(int, readTokens(conn, 3))
                command_data = readBytes(conn, command_data_length)
                if command_id == 0: # Take Photo
                    header = "data:image/png;base64,"
                    with self.img_lock:
                        img = Image.fromarray(self.img, mode='RGB')
                        pngimg = io.BytesIO()
                        img.save(pngimg, format='PNG')
                        b64img = base64.b64encode(pngimg.getbuffer())
                    conn.sendall("{} {} {} {}{}\n".format(request_id, 0, len(header)+len(b64img), header, b64img.decode('utf-8')).encode('utf-8'))
                else:
                    conn.sendall("{} 2 0\n".format(request_id))
                conn.close()
            except socket.timeout:
                pass
            except Exception as e:
                traceback.print_exc()
        os.remove(self.sock_path)

    def update_image(self, image):
        with self.img_lock:
            self.img = image

    def stop(self):
        self.event.set()
