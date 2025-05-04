import whois
import datetime


def format_date(date_str):
    if not date_str:
        return "não informado"
    try:
        if type(date_str) == datetime.datetime:
            return date_str.strftime("%d/%m/%Y")
        if len(date_str) == 8 and date_str.isdigit():
            return datetime.datetime.strptime(date_str, "%Y%m%d").strftime("%d/%m/%Y")
        return datetime.datetime.strptime(date_str[:19], "%Y-%m-%d %H:%M:%S").strftime(
            "%d/%m/%Y"
        )
    except Exception:
        return "não informado"


def verifica_lista(valor):
    if type(valor) == list:
        return valor[-1]
    return valor


def preparar_whois(info):
    dados = {}

    dados["dominio"] = verifica_lista(info.get("domain_name", "não informado"))
    dados["titular"] = info.get("registrant_name", "não informado")
    dados["documento"] = info.get("registrant_id", "não informado")

    # Responsável
    responsavel = info.get("person", "não informado")
    if type(responsavel) == list and responsavel:
        dados["responsavel"] = ", ".join([r.title() for r in responsavel])
    else:
        dados["responsavel"] = responsavel if responsavel else "não informado"

    # País, contatos
    dados["pais"] = info.get("country", "não informado")
    dados["c_titular"] = info.get("owner_c", "não informado")
    dados["c_tecnico"] = info.get("tech_c", "não informado")
    dados["org"] = info.get("org", "não informado")

    # DNS
    dns_servers = info.get("name_server") or info.get("name_servers")
    if type(dns_servers) == list and dns_servers:
        dados["servidores_dns"] = dns_servers
    elif type(dns_servers) == str:
        dados["servidores_dns"] = [dns_servers]
    else:
        dados["servidores_dns"] = ["não informado"]

    # Datas
    criacoes = info.get("creation_date", [])
    alteracoes = info.get("updated_date", [])
    expiracoes = info.get("expiration_date", "")

    if type(criacoes) == list and criacoes:
        dados["criado"] = format_date(criacoes[0])
    elif criacoes:
        dados["criado"] = format_date(criacoes)
    else:
        dados["criado"] = "não informado"

    if type(alteracoes) == list and alteracoes:
        dados["alterado"] = format_date(alteracoes[0])
    elif alteracoes:
        dados["alterado"] = format_date(alteracoes)
    else:
        dados["alterado"] = "não informado"

    if type(expiracoes) == list and expiracoes:
        dados["expiracao"] = format_date(expiracoes[0])
    elif expiracoes:
        dados["expiracao"] = format_date(expiracoes)
    else:
        dados["expiracao"] = "não informado"

    # DNS Status
    nsstat = info.get("nsstat", "")
    dados["dns_status"] = (
        format_date(nsstat.split()[0]) + " AA" if nsstat else "não informado"
    )
    dados["dns_ultimo_aa"] = format_date(info.get("nslastaa", ""))

    # SACI e status
    dados["saci"] = info.get("saci", "não informado")

    status = info.get("status", [])
    if type(status) == list and status:
        dados["status"] = status[-1]
    else:
        dados["status"] = status if status else "não informado"

    # Emails
    email = info.get("email") or info.get("emails")
    if type(email) == list and email:
        dados["emails"] = ", ".join(email)
    elif type(email) == str and email:
        dados["emails"] = email
    else:
        dados["emails"] = "não informado"

    # Contatos
    dados["contatos"] = []

    nics = info.get("nic_hdl_br", [])
    pessoas = info.get("person", [])
    if type(nics) == list and len(nics) > 1:
        for i in range(len(nics)):
            dados["contatos"].append(
                {
                    "id": nics[i],
                    "nome": (
                        pessoas[i].title()
                        if type(pessoas) == list and len(pessoas) > i
                        else "não informado"
                    ),
                    "email": (
                        emails[i]
                        if type(emails) == list and len(emails) > i
                        else dados["emails"]
                    ),
                    "criado": (
                        format_date(criacoes[i + 1])
                        if type(criacoes) == list and len(criacoes) > i + 1
                        else "não informado"
                    ),
                    "alterado": (
                        format_date(alteracoes[i + 1])
                        if type(alteracoes) == list and len(alteracoes) > i + 1
                        else "não informado"
                    ),
                }
            )
    else:
        dados["contatos"].append(
            {
                "id": nics if nics else "não informado",
                "nome": (
                    pessoas.title()
                    if type(pessoas) == str
                    else (
                        pessoas[0].title()
                        if type(pessoas) == list and pessoas
                        else "não informado"
                    )
                ),
                "email": dados["emails"],
                "criado": format_date(criacoes[-1]) if criacoes else "não informado",
                "alterado": (
                    format_date(alteracoes[-1]) if alteracoes else "não informado"
                ),
            }
        )

    return dados


def whois_lookup():
    domain = input("Informe qual o domínio que deseja analisar: ")
    whois_info = whois.whois(domain)
    print(whois_info)
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
