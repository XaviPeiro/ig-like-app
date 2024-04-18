from time import sleep


def app(environment, start_response):
    """Simplest possible application object"""
    """
        1- Add "intensive"
    """
    sleep(.02)
    data = b'Hello, World!\n'
    status = '200 OK'
    response_headers = [
        ('Content-type', 'text/plain'),
        ('Content-Length', str(len(data)))
    ]
    start_response(status, response_headers)
    return iter([data])


if __name__ == "__main__":
    # run server (guinicorn)
    print("running server...")

