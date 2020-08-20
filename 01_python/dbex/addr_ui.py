from addr_models import Addr
def print_list(total, rows):
    print("=" * 50)
    print("No  이름       전화번호    주소")
    print("=" * 50)
    for ix, row in enumerate(rows, 1):
        print(f"{ix} : {row.name:10}{row.phone:10} {row.addr:10}")
    print("=" * 50)
    print(f"총 {total} 건")

def input_addr_info():
    name = input("이름    :")
    phone = input("전화번호:")
    addr = input("주소    :")
    return Addr(name, phone, addr)

def input_new_addr(data):
    phone = input(f"전화번호({data.phone}):")
    if not phone:
        phone = data.phone
    addr = input(f"주소({data.addr}):")
    if not addr:
        addr = data.addr
    return Addr(data.name, phone, addr)