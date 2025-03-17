from django.http import HttpResponse


def index(request):
    # host = request.META["HTTP_HOST"]  # получаем адрес сервера
    # user_agent = request.META["HTTP_USER_AGENT"]  # получаем данные бразера
    # path = request.path  # получаем запрошенный путь
    #
    # return HttpResponse(f"""
    #     <p>Host: {host}</p>
    #     <p>Path: {path}</p>
    #     <p>User-agent: {user_agent}</p>
    # """)
    #return HttpResponse("Hello, tractor driver!", headers={"SecretCode": "21234567"})
    return HttpResponse("<h2>Главная</h2>")


def about(request, name, age):
    return HttpResponse(f"""
            <h2>О пользователе</h2>
            <p>Имя: {name}</p>
            <p>Возраст: {age}</p>
    """)


def user(request, name="Undefined", age = 0):
    return HttpResponse(f"<h2>Имя: {name}  Возраст: {age}</h2>")


def products(request):
    return HttpResponse("Список товаров")


def new(request):
    return HttpResponse("Новые товары")


def top(request):
    return HttpResponse("Наиболее популярные товары")


def products(request, id):
    return HttpResponse(f"Товар {id}")


def comments(request, id):
    return HttpResponse(f"Комментарии о товаре {id}")


def questions(request, id):
    return HttpResponse(f"Вопросы о товаре {id}")