from django.http import JsonResponse
from django.views import View
import json


class SimpleLoginView(View):
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        print(username, password)
        # 这里可以添加用户名和密码的验证逻辑
        return JsonResponse({'id': 1000})
