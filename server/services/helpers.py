def getValueBetweenTag(tag, string):
    startTag = '<'+tag+'>'
    closeTag = '</'+tag+'>'

    return getValueBetween(startTag, closeTag, string)

def getValueBetween(before, after, string):
    try:
        values = string.split(before)
        value = values[1].split(after)[0]
        return value
    except:
        print("Could not get value between " + before + " and " + after + " for string :"+string)
    