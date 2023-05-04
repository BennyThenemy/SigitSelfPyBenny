def my_mp3_playlist(file_path):
    longest_song = ""
    num_of_songs = 0
    artist_with_more_songs = ""

    with open(file_path, "r") as f:

        cd_data = f.read()
        cd_splitted_lines = cd_data.split("\n")
        num_of_songs = len(cd_splitted_lines)

        cd_items = []
        for element in cd_splitted_lines:
            cd_items.append(element.split(";"))

        # artist_with_more_songs:
        dict_artist = {}
        for item in cd_items:

            if item[1] in dict_artist:
                dict_artist[item[1]] += 1
            else:
                dict_artist[item[1]] = 1

        artist_with_more_songs = max(dict_artist, key=dict_artist.get)

        longest_song_num = 0.0
        for item in cd_items:
            time_str = item[2]
            hour_str, minute_str = time_str.split(":")
            hour = int(hour_str)
            minute = int(minute_str)
            time_float = hour + (minute / 60)

            if float(time_float) > float(longest_song_num):
                longest_song_num = time_float
                longest_song = item[0]

        my_cd_dict = {}
        for item in cd_items:
            my_cd_dict[item[0]] = (item[1], item[2])

    return longest_song, num_of_songs, artist_with_more_songs


def main():
    print(my_mp3_playlist("songs.txt"))


if __name__ == '__main__':
    main()
