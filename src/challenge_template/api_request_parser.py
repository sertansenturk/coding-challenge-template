class APIRequestParser:
    @staticmethod
    def parse_post_request(request):
        data = request.get_data().decode("utf-8")
        return f"Received {request.method} request: '{data}'"
