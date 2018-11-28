import os


DIR = 'Migrations'


def find_string(path, string):
    try:
        with open(path) as file:
            for line in file:
                if string in line:
                    return line
    except IOError as err:
        print(
            'Error while trying to read {}'.format(
                err))
    except UnicodeDecodeError:
        pass  # Damn unicode
    return ''


def find_in_files(string, files, basedir):
    assert isinstance(files, (list, tuple)), 'we only accept lists or tuples'

    matched = []
    for file_path in files:
        file_path = os.path.join(basedir, file_path)
        if find_string(file_path, string):
            matched.append(file_path)
    return matched


def main():
    files = os.listdir(DIR)
    while len(files) >= 1:
        string = input('Input string to search for: ')
        files = find_in_files(string, files, DIR)
        print('Matches: {}'.format(files))
        print('Number of files matched: {}'.format(len(files)))

    print('Program is finished')


main()
#
# if __name__ == '__main__':
#     main()