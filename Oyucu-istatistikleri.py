goals = {
    "Ahmet": [1, 0, 2, 1],
    "Burak": [0, 0, 1],
    "Can": [2, 2, 0, 1, 0],
}
print(goals)
toplam_goller = {oyuncu: sum(gol_listesi) for oyuncu, gol_listesi in goals.items()}
print(toplam_goller)
en_iyi_oyuncu = max(toplam_goller, key=toplam_goller.get)
print(en_iyi_oyuncu)
print(en_iyi_oyuncu, toplam_goller[en_iyi_oyuncu])