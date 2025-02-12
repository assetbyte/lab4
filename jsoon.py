import json
def parse(file):
    print("Interface Status\n"+"="*80)
    print(f"{'DN':<50} {'Description':<20} {'Speed':<7} {'MTU':<6}")
    print("-"*50, "-"*20, "-"*7, "-"*6)
    f = open(file, 'r')
    data = json.load(f) #JSON -> PYTHON
    f.close()
    for i in data["imdata"]:
        attr = i["l1PhysIf"]["attributes"]
        dn = attr['dn']
        desc = attr['descr']
        speed = attr['speed']
        mtu = attr['mtu']
        print(f"{dn:<50} {desc:<20} {speed:7} {mtu:<6}")
parse("sample.json")