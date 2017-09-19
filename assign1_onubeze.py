import re
from datetime import date


class Average:
    def __init__(self, numbers):
        self.numbers = numbers

    def get_average(self):
        sum_numbers = 0
        for n in self.numbers:
            sum_numbers += n
        av = sum_numbers / len(self.numbers)
        if av < 6:
            print("Low Average")
        elif av > 12:
            print("High Average")
        elif av >= 6:
            print("Medium Average")

    @classmethod
    def from_string(cls, string_input):
        return list(map(int, re.findall('\d+', string_input)))


def article_info(article):
    info_list = article.split('/')
    name = info_list[4]
    date_added = date(int(info_list[1]), int(info_list[2]), int(info_list[3]))
    duration = (date.today() - date_added).days
    return tuple([name, date_added.strftime("%d-%m-%Y"), duration])


def main():
    input_string = input("Enter an alphanumeric string: ")
    numbers = Average.from_string(input_string)
    obj = Average(numbers)
    obj.get_average()

    print(article_info("articles/2010/10/21/my_summer"))


if __name__ == "__main__":
    main()
