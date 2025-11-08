# Yon prototip app ki ka itilize pou fè eleksyon an Ayiti.

# Defini yon fonksyon pou pwosesis vot la.

def pwosesis_vot():
    # Nou itilize "list" pou kreye baz done kap anrejistre enfòmasyon sou kandida yo nan chak pos elektif.

    # Kandida pou pos prezidan:
    Kandida_prezidan = [["Lewis", "PLACIDE"], ["Muscadin", "JEAN"], ["Lorvens", "JULES"], ["Kelson", "DASTINOT"], ["Okenn", "KANDIDA"]]

    # Kandida pou pos senate:
    Kandida_senate = [["Clefton", "SIMON"], ["Catherine", "FLON"], ["Robinson", "LAGUERRE"], ["Antoine", "PIERRE"], ["Okenn", "KANDIDA"]]

    # Kandida pou pos depite:
    Kandida_depite = [["Nissage", "SAGET"], ["Vilbrun", "GUILLAUME"], ["Bernard", "LESCOT"], ["Ely", "JOSEPH"], ["Okenn", "KANDIDA"]]

    # Mande elekte a pou chwazi kandida pou chak pos elektif
    print("\nSilvouple chwazi yon kandida pou chak pos elektif:\n")

    # Pos prezidan
    print("Kandida pou pos prezidan:")
    for i, prezidan in enumerate(Kandida_prezidan, 1):
        print(f"{i}. {prezidan[0]} {prezidan[1]}")

    chwa_prezidan = int(input("Rantre nimewo ou wè devan kandida ou ap vote prezidan an: "))
    vot_prezidan = Kandida_prezidan[chwa_prezidan - 1]

    # Pos senate
    print("\nKandida pou pos senate:")
    for i, senate in enumerate(Kandida_senate, 1):
        print(f"{i}. {senate[0]} {senate[1]}")

    chwa_senate = int(input("Rantre nimewo ou wè devan kandida ou ap vote pou senate a: "))
    vot_senate = Kandida_senate[chwa_senate - 1]

    # Pos depite
    print("\nKandida pou pos depite:")
    for i, depite in enumerate(Kandida_depite, 1):
        print(f"{i}. {depite[0]} {depite[1]}")

    chwa_depite = int(input("Rantre nimewo ou wè devan kandida ou ap vote pou depite a: "))
    vot_depite = Kandida_depite[chwa_depite - 1]

    # Afiche rezime chwa elekte a
    print("\n️Ou chwazi:")
    print(f"Prezidan: {vot_prezidan[0]} {vot_prezidan[1]}")
    print(f"Senate:   {vot_senate[0]} {vot_senate[1]}")
    print(f"Depite:   {vot_depite[0]} {vot_depite[1]}")

    # Konfime chwa yo
    konfime = input("\nÈske chwa ou yo kòrèk? (wi/non): ").strip().lower()

    if konfime == "wi":
        print("\n Mèsi paske ou ranpli devwa sivik ou! Vot ou a anrejistre.")
        return True
    else:
        print("\n Nou dezole, vot ou yo anile. Rekòmanse pwosesis la...\n")
        return False


def main():
    # Byenvini sou sistèm elektoral la
    print("\n Byenvini sou sistèm elektoral la! Nou kontan pou’n akonpanye ou ranpli devwa sivik ou.")
    print("----------------------------------------------------")

    # Lis kat idantifikasyon nasyonal (CIN) ki valid yo
    valid_CIN = ["1068102213", "1068102214", "1068102215", "1068102216", "1068102217"]

    # Lis pou CIN ki gentan vote yo
    CIN_vote = []

    # Bouk prensipal pou kontwole eleksyon an
    while True:
        CIN_elekte = input("\nSilvouple rantre yon kat idantifikasyon nasyonal valid: ").strip()

        # Verifye si CIN elekte a valid
        if CIN_elekte not in valid_CIN:
            print(" Nimewo kat idantifikasyon nasyonal ou a pa valid. Silvouple rantre yon nimewo kat ki valid.")
            continue

        # Verifye si CIN elekte a gentan vote
        if CIN_elekte in CIN_vote:
            print("️ Nimewo kat idantifikasyon nasyonal sa gentan vote. Silvouple rantre yon lòt nimewo ki valid.")
            continue

        print(" Nimewo kat idantifikasyon nasyonal ou verifye ak sikse! Kontinye ak pwosesis vot la...\n")

        # Lanse pwosesis vot la
        vot_konfime = pwosesis_vot()

        # Si vot lan reyisi, ajoute CIN lan nan lis moun ki vote
        if vot_konfime:
            CIN_vote.append(CIN_elekte)
            print(f"\n️ Nimewo CIN: {CIN_elekte} vote avèk siksè.\n")

        # Mande si nou ta renmen kontinye ak pwochen elekte
        kontinye = input("Èske gen yon lòt moun ki pral vote? (wi/non): ").strip().lower()

        if kontinye != "wi":
            print("\nMèsi paske ou itilize sistèm elektoral la. Jounen elektoral la bout.")
            break

        print("\n🔁 Nou pral rekòmanse pwosesis pou pwochen elekte a...\n")


# Nap lanse pwogram nan
if __name__ == "__main__":
    main()
