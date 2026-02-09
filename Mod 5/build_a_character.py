def create_character(name, **attributes):
    print(f"Character: {name}")
    for attr, value in attributes.items():
        print(f"  {attr}: {value}")

create_character(
    "Aria",
    strength=8,
    agility=10,
    magic=6,
    alignment="chaotic good"
)

########################################################
def build_request(url, **params):
    query = "&".join(f"{k}={v}" for k, v in params.items())
    print(f"{url}?{query}")

build_request("http//myserver.com/mysite/search", q="python", page=2, sort="recent")
