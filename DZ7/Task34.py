def x_sound(sound):
    lines = sound.split()

    first_line_syllables = count_syllables(lines[0])

    for line in lines[1:]:
        if count_syllables(line) != first_line_syllables:
            return "Пам парам"

    return "Парам пам-пам"

def count_syllables(line):
    vowels = "аеёиоуыэюя"
    count = 0

    for char in line:
        if char.lower() in vowels:
            count += 1

    return count

sound = input("Введите песню: ")
result = x_sound(sound)
print(result)