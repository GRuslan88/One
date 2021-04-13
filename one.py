from flask import Flask
from flask import render_template
import csv
import pandas as pd

app = Flask(__name__)


@app.route('/')
def root():
    """Чтение файла cvs и  запись в html страницу списка

    Returns:
        html страницу со списком sting_list
    """
    file_csv = 'base.csv'
    sting_list = []
    with open(file_csv, encoding='utf-8') as file_csv:
        csv_file = csv.reader(file_csv, delimiter=';')
        for row in csv_file:
            sting_list.append(row)
    sting_list = pd.DataFrame(sting_list)
    return render_template('index.html', results=sting_list.to_html(header=False, index=False))


# Запуск локального web сервера
# Адресс сайта "http://localhost:5000/"
if __name__ == "__main__":
    app.run(debug=True)
