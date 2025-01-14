def introspection_info(obj):
    # Определяем информацию о объекте
    info = {}

    # Тип объекта
    info['type'] = type(obj).__name__

    # Модуль объекта
    info['module'] = obj.__mul__

    # Атрибуты объекта
    attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith('__')]
    info['attributes'] = attributes

    # Методы объекта
    methods = [method for method in dir(obj) if callable(getattr(obj, method)) and not method.startswith('__')]
    info['methods'] = methods

    return info


# Пример использования функции
if __name__ == "__main__":

    print("\nИнформация о целочисленном объекте:")
    print(introspection_info(42))