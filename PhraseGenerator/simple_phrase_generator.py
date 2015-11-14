# coding: utf8

def generate_phrase(class_number):
    if class_number == 1:
        return u'спит'
    elif class_number == 2:
        return u'лежит'
    elif class_number == 3:
        return u'сидит'
    elif class_number == 4:
        return u'идет'
    elif class_number == 5:
        return u'стоит'
    elif class_number == 6:
        return u'моется'
    elif class_number == 7:
        return u'играет лежа'
    elif class_number == 8:
        return u'играет'
    elif class_number == 9:
        return u'ласка'
    else:
        return u'не определен'

