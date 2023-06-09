# pip install easyocr 
import easyocr
def textRecognize(filePath, textFileName='result.txt'):
    reader = easyocr.Reader(['ru', 'en'])
    result = reader.readtext(filePath, detail=0, paragraph=True)

    with open(textFileName, 'w') as file:
        for line in result:
            file.write(f'{line}\n\n')

    return f'Result wrote into {textFileName}'


def main():
    filePath = input('Enter a file path: ')
    print(textRecognize(filePath=filePath, textFileName='readme_first.txt'))

if __name__ == '__main__':
    main()