import datetime


class CreateFile:
    def __init__(self,path):
        self.path = path
        self.time_op = datetime.datetime.now()
        print(f'Файл {self.path} был создан {datetime.datetime.now()}')
    def __enter__(self):
        self.file = open(self.path, 'w', encoding='utf8')
        return self.file
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        self.time_cl = datetime.datetime.now()
        self.time_dif = self.time_cl - self.time_op
        print(f' Файл {self.path} был закрыт в {self.time_cl} \n Время работы кода сотавило {self.time_dif.seconds} секунд(ы)(у) и {self.time_dif.microseconds} микросекунд.')


if __name__ == '__main__':
    with CreateFile('assay.txt') as file:
        content = input('Расскажите о себе:')
        file = file.write(content)

