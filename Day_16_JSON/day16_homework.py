# TODO read emojihub.json into a Python data structure
# add new key emoji to each dictionary with value of emoji
# to do so you will need to extract Unicode numerical value from htmlCode value
# save the new data structure to a file called emojihub_with_emoji.json
# TIP: remember about ensure_ascii=False and encoding='utf-8'

# for those who did not finish the exercise in class
# alternative assignment would be to use the classword to find a public API not seen in class
# and use requests to get the data and parse it into a Python data structure
# then save it to a file

# so a single entry should look like this:
    # {
    #     "name": "pear",
    #     "category": "food and drink",
    #     "group": "food fruit",
    #     "htmlCode": [
    #         "&#127824;"
    #     ],
    #     "unicode": [
    #         "U+1F350"
    #     ],
    #     "emoji": "🍐" 
    # },
    # more fruits would follow