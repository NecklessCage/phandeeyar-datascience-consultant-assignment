from sylseg import syllable_break

with open('aux/common-words.txt') as f:
    common_words = [l.strip() for l in f]
with open('aux/dict-words.txt') as f:
    dict_words = [l.strip() for l in f]
with open('aux/stop-words.txt') as f:
    stop_words = [l.strip() for l in f]
print(len(common_words), len(dict_words), len(stop_words))

def wb(_input):
    _input = syllable_break(str(_input).replace(' ', ''))

    result = []
    offset = 0
    LIMIT = 7

    while offset < len(_input):
        chunk_end = offset + LIMIT
        chunk_found = False

        for i in range(chunk_end, offset, -1):
            chunk = ''.join(_input[offset:i])

            if chunk in dict_words or chunk in common_words or chunk in stop_words:
                # Found the word in data
                chunk_found = True
                result.append(chunk)

                # Resetting offset to resume
                offset = i
                break


        # Didn't found the word of any
        # long-short combination in the chunk
        if not chunk_found:
            # Now, the current syllable is a word
            result.append(_input[offset])
            offset += 1
    return result