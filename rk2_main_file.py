#rk2_main_file
'''программа принимает неотрицательное число и выводит пользователю это же число в обратном порядке'''
def main():
    #открывем файлы для чтения и для записи
    outfile = open('stdin.txt', 'r')
    infile = open('stdout.txt', 'w')

    #получаем данные с файла stdin.txt
    num = int(outfile.read())
    num_line = str(num)

    #условие неотрицательности
    if num >= 0:
        num_line = num_line[::-1]
    else:
        print("Полученное число отрицательное\n Введите заново")

    #записываем полученное число в файл stdout.txt
    infile.write(num_line)
    print('Данные успшно записаны в файл stdout.txt')

    #закрывем используемые файлы
    outfile.close()
    infile.close()
if __name__ == "__main__":
    main()
    

