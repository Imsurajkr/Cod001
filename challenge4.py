# Given the tuple below that represents the Imelda  May album "More Mhyem", Write
# Code to print the album details, followed by a listening of all the tracks in the album
#
# Indent the tracks by a single tab stop when printing them ( remember that you can pass
# More than one item to the print function, separting them with a comma ).

# imelda = "More Mayhem", "Imelda May", 2011, (
#     (1, "pulling the rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kantish Town")
# )
# print(imelda)
# title, artist, year, tracks = imelda
# for song in tracks:
#     track, title = song
#
#     print("\t Track number {}, Title{}".format(track, title ))
#----------------------------------------------------------------------
# albumName, name, year, tracks = imelda
# # print(albumName)
# # print(name)
# # print(year)
# # print(tracks)
# for album in imelda:
#     print("\t")
#     print(album)
# print("--" * 50)
# for i in tracks:
#     print("""
#     s.no: {}\n
#     details: {}\n
#     """.format(i[0], i[1]))
#
#
#     # print(i[1])
# # print(track1)
# # print(track2)
# # print(track3)
# # print(track4)
# --------------------------------------------------------------------

# imelda = "More Mayhem", "Imelda May", 2011, (
#     [(1, "pulling the rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kantish Town")]
# )
# print(imelda)
# imelda[3].append((5, "All for you"))
# title, artist, year, tracks = imelda
# tracks.append((6, "eternity"))
# for song in tracks:
#     track, title = song
#     print("\t Track Number {} , Title {}".format(track, title))
#
#





























