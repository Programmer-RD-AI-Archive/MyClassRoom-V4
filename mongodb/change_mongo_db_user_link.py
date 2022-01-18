import json

with open(
        "/home/indika/Programming/Projects/Python/Web-Dev/MCR-V4/private/mongodb-client.json"
) as info:
    info_ = json.load(info)
    link = input(" - Link \n - ")
    ok_or_not = input(" - Is it correct ? (Y/N) \n - ")
    while ok_or_not.upper() == "N":
        link = input(" - Link \n - ")
        ok_or_not = input(" - Is it correct ? (Y/N) \n - ")
    info_["MongoDB-Client-Url"] = link
    with open(
            "/home/indika/Programming/Projects/Python/Web-Dev/MCR-V4/private/mongodb-client.json",
            "w",
    ) as _info:
        json.dump(info_, _info)
