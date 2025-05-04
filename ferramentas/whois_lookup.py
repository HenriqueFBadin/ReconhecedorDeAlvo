import whois
import datetime


def format_date(date_str):
    if type(date_str) == datetime.datetime:
        return date_str.strftime("%d/%m/%Y")

    if len(date_str) == 8 and date_str.isdigit():
        return datetime.datetime.strptime(date_str, "%Y%m%d").strftime("%d/%m/%Y")

    return datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S").strftime(
        "%d/%m/%Y"
    )


def verifica_lista(valor):
    if type(valor) == list:
        return valor[-1]
    return valor


def preparar_whois(info):

    dados = {}

    dados["dominio"] = info["domain_name"]
    dados["titular"] = info["registrant_name"]
    dados["documento"] = info["registrant_id"]

    if type(info["person"]) == list:
        dados["responsavel"] = ", ".join([nome.title() for nome in info["person"]])
    else:
        dados["responsavel"] = info["person"]

    dados["pais"] = info["country"]
    dados["c_titular"] = info["owner_c"]
    dados["c_tecnico"] = info["tech_c"]
    dados["servidores_dns"] = info["name_server"]
    dados["dns_status"] = format_date(verifica_lista(info["nsstat"].split()[0])) + " AA"
    dados["dns_ultimo_aa"] = (
        format_date(info["nslastaa"]) if "nslastaa" in info and info["nslastaa"] else ""
    )
    dados["saci"] = info["saci"]
    dados["criado"] = format_date(min(info["creation_date"]))
    dados["alterado"] = format_date(verifica_lista(info["updated_date"]))
    dados["expiracao"] = format_date(info["expiration_date"])
    dados["status"] = verifica_lista(info["status"])

    dados["contatos"] = []

    if type(info["nic_hdl_br"]) == list and len(info["nic_hdl_br"]) > 1:
        total = len(info["nic_hdl_br"])
        for i in range(total):
            dados["contatos"].append(
                {
                    "id": info["nic_hdl_br"][i],
                    "nome": (
                        info["person"][i].title()
                        if type(info["person"]) == list and len(info["person"]) > i
                        else info["person"].title()
                    ),
                    "email": info["email"],
                    "criado": (
                        format_date(info["creation_date"][i + 1])
                        if len(info["creation_date"]) > i + 1
                        else ""
                    ),
                    "alterado": (
                        format_date(info["updated_date"][i + 1])
                        if len(info["updated_date"]) > i + 1
                        else ""
                    ),
                }
            )

    else:

        dados["contatos"].append(
            {
                "id": info["nic_hdl_br"],
                "nome": info["person"],
                "email": info["email"],
                "criado": format_date(info["creation_date"][-1]),
                "alterado": format_date(info["updated_date"][-1]),
            }
        )
    return dados


def whois_lookup():
    domain = input("Informe qual o domínio que deseja analisar: ")
    whois_info = whois.whois(domain)
    dados = preparar_whois(whois_info)

    print(f"domínio:       {dados['dominio']}")
    print(f"titular:       {dados['titular']}")
    print(f"documento:     {dados['documento']}")
    print(f"responsável:   {dados['responsavel']}")
    print(f"país:          {dados['pais']}")
    print(f"c-titular:     {dados['c_titular']}")
    print(f"c-técnico:     {dados['c_tecnico']}")

    for dns in dados["servidores_dns"]:
        print(f"servidor DNS:  {dns}")
        print(f"status DNS:    {dados['dns_status']}")
        print(f"último AA:     {dados['dns_ultimo_aa']}")

    if dados["saci"]:
        print(f"saci:          {dados['saci']}")

    print(f"criado:        {dados['criado']}")
    print(f"alterado:      {dados['alterado']}")
    print(f"expiração:     {dados['expiracao']}")
    print(f"status:        {dados['status'].title()}")

    for contato in dados["contatos"]:
        print(f"\nContato (ID):  {contato['id']}")
        print(f"nome:          {contato['nome']}")
        print(f"e-mail:        {contato['email']}")
        print(f"criado:        {contato['criado']}")
        print(f"alterado:      {contato['alterado']}")

    # print(whois_info)
