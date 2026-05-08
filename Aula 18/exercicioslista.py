notas = []
alunos = []

while True:
    for i in range(8):
        nota = float(input(f"Digite a {i+1} nota: "))
        if nota >= 0 and nota <=10:
            notas.append(nota)
        else:
            print("Nota invalida")
        
        if len(notas) >= 8:
            break   
        

    media = sum(notas) / len(notas)

    print(f"media: {media}")

    ordem = 1

    for n in notas:
        print(f"Nota {ordem} - {n:.1f}")
        ordem += 1

