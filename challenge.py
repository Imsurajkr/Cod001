ipAddress: object = input("Please enter your Ip address ")
if '.' != ipAddress[-1]:
    ipAddress += "."
segments = 1
segment_length: int = 0
# character = ""

for character in ipAddress:
    if character == ".":
        print("segment {} contains {} character".format(segments, segment_length))
        segments += 1
        segment_length = 0
    else:
        segment_length += 1

# Unless the final character in the string was a . then we haven't printed the last segment

# if character != ".":
#     print("segemnt {} contains {} characters ".format(segments,segment_length))
# Character have a value whether for loops run or not
