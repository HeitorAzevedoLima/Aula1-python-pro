dict = {
    "BUGOU": "Algo travou/parou de funcionar",
    "CRINGE": "Algo muito vergonhoso",
    "HATER": "Pessoa que constantemente critica algo ou alguem",
    "VLW": "Abreviacao da palavra 'valeu'",
    "BISCOITAR": "Postar algo apenas para chamar atencao",
    "BLZ": "Abreviacao para a palavra 'beleza'",
    "VDD": "Abreviacao para a palavra 'Verdade'",
}
P = input("Digite uma palavra Moderna que voce nao consegue entender (em letra maiuscula)")
if P in dict.keys():
    print(dict[P])
else:
    print('Essa palavra ainda nao foi implementada')
