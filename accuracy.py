import pandas as pd
import sys

def accuracy(filepath, Class):
    df = pd.read_csv(filepath)

    count = 0
    ct=0

    print(df)

    print('Total values : ' + str(len(df['CLASS'])))

    for i in range(len(df['CLASS'])):
        if Class == 'I':
            if df['CLASS'][i] == 'I':
                count += 1
            if df['CLASS'][i] == 'C':
                ct += 1
        else:
            if df['CLASS'][i] == 'II':
                count += 1
            if df['CLASS'][i] == 'C':
                ct += 1

    print('Correctly predicted values : ' + str(count))

    print('COMP values: ' + str(ct))
 #   print('BENT values: ' + str(ct))

    accuracy = str(count * 100 / len(df['CLASS']))

    print('accuracy : ' + accuracy + '%')

def main():
    if len(sys.argv) < 3:
        print("Usage: python3 accuracy.py <filepath> <class>", "\nwhere class is I or II (for FR1/FR2)")
        exit(1)
    filepath = sys.argv[1]
    Class = sys.argv[2]
    accuracy(filepath, Class)

if __name__ == "__main__":
    main()