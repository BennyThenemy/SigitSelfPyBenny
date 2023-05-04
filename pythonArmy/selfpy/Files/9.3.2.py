def my_mp4_playlist(file_path, new_song):
    with open(file_path, 'r') as file:
        lines = file.readlines()

        while len(lines) < 3:
            lines.append('\n')

        song = lines[2].strip().split(';')
        song[0] = new_song
        lines[2] = ';'.join(song) + '\n'

        with open(file_path, 'w') as file:
            file.writelines(lines)


        with open(file_path, 'r') as file:
            print(file.read())


def main():
    my_mp4_playlist("songs.txt", "Python Love Story")


if __name__ == '__main__':
    main()
