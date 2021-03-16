import csv
import re

WRITE = "write.csv"
CSV_PATH = "base.csv"


def csv_reader(file_obj):
    """Чтение файла cvs и  запись в список

    Args:
        file_obj: TextIOWrapper
    Returns
    список list
    """
    sting_list = []
    reader = csv.reader(file_obj, delimiter=';')
    for row in reader:
        sting_list.append(row)

    return sting_list


def csv_telega(file_obj_t):
    """Чтение файла cvs и  запись в список

    Args:
        file_obj_t: TextIOWrapper
    Returns
    список listT
    """
    string_list = []
    with open(file_obj_t, encoding='utf-8') as file_obj:
        reader = csv.reader(file_obj, delimiter=';')
        for row in reader:
            for i in row:
                string_list.append(i)

    return string_list


def min_list(offers_list):
    """Нахождение минимальной цены

    Args:
        offers_list: список;
     Returns:
        int: индекс списка с минимальной ценой
    """
    count, min, index = 0, 0, 0
    for row in offers_list:
        if not row:
            count += 1
            continue
        string_price = row[2]
        regex_num = re.compile(r'\d+')
        price = ''.join(regex_num.findall(string_price))
        if int(price) < min or min == 0:
            min = int(price)
            index = int(count)
        count += 1
    return index


def file_write_csv(best_offer, index, file):
    """Запись в файл строки из листа с минимальной ценой

    Args:
        best_offer: список
        index: индекс списка с минимальной ценой
        file: файл для записи
    Returns:
        файл с данными
    """
    list_x = best_offer[index]
    with open(file, 'w', encoding='utf-8') as file_csv:
        csv_writer = csv.writer(file_csv, delimiter=';')
        csv_writer.writerow([list_x[0], list_x[1], list_x[2]])


def file_offers():
    """

    Returns:
        list: список сохраненых предложений из файла
    """
    with open(CSV_PATH, "r", encoding='utf-8') as f_obj:
        return csv_reader(f_obj)


best_offer_index = min_list(file_offers())
file_write_csv(file_offers(), best_offer_index, WRITE)
