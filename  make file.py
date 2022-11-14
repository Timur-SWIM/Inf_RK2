# make file
def main():
    outfile = open('stdin.txt','w')
    number = input('Введите число:')
    outfile.write(number)
    outfile.close()
if __name__ == '__main__':
    main()

