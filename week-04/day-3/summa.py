class Summ(object):
    def sum_of_numbers(self, numbers = []):
        sum_of_numbers = 0
        for number in numbers:
            sum_of_numbers += number
        return sum_of_numbers