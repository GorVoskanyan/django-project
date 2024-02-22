from django.http import HttpRequest, HttpResponse


def set_useragent_on_request_middleware(get_response):
    print('Initial call')

    def middleware(request: HttpRequest):
        print('Before get response')
        request.user_agent = request.META['HTTP_USER_AGENT']
        response = get_response(request)
        print('After get response')
        return response
    return middleware


class CountRequestsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.requests_count = 0
        self.responses_count = 0
        self.exceptions_count = 0
        self.test_ip = {}

    # def __call__(self, request: HttpRequest):
    #     self.requests_count += 1
    #     print('Requests count:', self.requests_count)
    #     response = self.get_response(request)
    #     self.responses_count += 1
    #     print('Responses count:', self.responses_count)
    #     return response

    def __call__(self, request):

        ip_address = request.META.get('REMOTE_ADDR')
        if ip_address in self.test_ip:
            self.test_ip[ip_address] += 1
        else:
            self.test_ip[ip_address] = 1
        if self.test_ip[ip_address] >= 5:
            result = HttpResponse('YOU ARE BLOCKED')
            # pass_admin = input()
            # if pass_admin == '1234':
            #     self.requests_count = 0
            # else:
            #     return result
            return result
        response = self.get_response(request)
        self.responses_count += 1
        print('Responses count:', self.responses_count)
        return response

    def process_exception(self, request: HttpRequest, exception: Exception):
        self.exceptions_count += 1
        print('Got', self.exceptions_count, 'exceptions so far')
