import time


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return self.nickname


class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

    def __eq__(self, other):
        if isinstance(other, Video):
            if self.title == other.title and self.duration == other.duration:
                return True
        return False


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname and user.password == hash(password):
                self.current_user = user
                break
        else:
            print('пользователь не найден')

    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print(f"Пользователь {nickname} уже существует")
                break
        else:
            temp_user = User(nickname, password, age)
            self.users.append(temp_user)
            self.current_user = temp_user

    def log_out(self):
        self.current_user = None

    def add(self, *videos):
        for v in videos:
            if v not in self.videos:
                self.videos.append(v)

    def get_videos(self, key_word):
        res = list()
        for v in self.videos:
            if key_word.lower() in v.title.lower():
                res.append(v.title)
        return res

    def watch_video(self, film_name):
        if self.current_user is None:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return
        for v in self.videos:
            if film_name == v.title:
                if v.adult_mode and self.current_user.age < 18:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    return

                for i in range(v.duration):
                    print(i + 1, end=" ")
                    time.sleep(1)
                print("Конец видео")
                return


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт#
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')

