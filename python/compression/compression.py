class Compression:
    def compress(self, chars):  # in place
        # Which element we are on
        i = 1
        # How many occurences of the current element have been counted
        counter = 1

        # The length of chars will change, so the loop is "while" instead of
        # a "for"
        while i <= len(chars) - 1:
            # If last and current match, increment the counter and delete the element.
            # i stays the same because elements to the right will shift left 
            # one spot into the deleted space.
            if chars[i-1] == chars[i]:
                counter += 1
                del chars[i]
            else:
                # If no match, and counter is 1, leave the element and move on
                if counter == 1:
                    i += 1
                # If no match, and counter is more than 1, insert string of 
                # counter into the chars array.
                # Also, increment i to skip to the next element after the 
                # counter string.
                else:
                    chars[i:i] = list(str(counter))  # similar to insert(), but inserts elements instead of the array
                    i += 1 + len(str(counter))
                # Reset the counter to 1
                counter = 1

        # Handle the last element
        if counter > 1:
            chars += list(str(counter))

        return len(chars)


# Code with no comments:
class Compression:
    def compress(self, chars):  # in place
        i = 1
        counter = 1
        while i <= len(chars) - 1:
            if chars[i-1] == chars[i]:
                counter += 1
                del chars[i]
            else:
                if counter == 1:
                    i += 1
                else:
                    chars[i:i] = list(str(counter))  # similar to insert(), but inserts elements instead of the array
                    i += 1 + len(str(counter))
                counter = 1
        if counter > 1:
            chars += list(str(counter))

        return len(chars)

