from parser import parse_resume_data
from html_create import generate_html, save_html_to_file



def main():

    resume_file_name = "resume_data.txt"
    html_filename = 'resume.html'


    print("Читаем и парсим файл...")
    resume_data = parse_resume_data(resume_file_name)

    # print(resume_data)

    if resume_data:
        print("Подготавливаем HTML страницу...")
        html_data = generate_html(resume_data)
        print(f"Сохраняем страницу HTML в файл {html_filename}...")
        save_html_to_file(html_data, html_filename)
        print("Процесс завершен успешно!")

    else:
        print(f"Не удалось обработать данные из {resume_file_name}")



if __name__ == "__main__":
    main()