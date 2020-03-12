def count_dice(processed, target, faces):

    if target == 0:
        print(processed)
        return

    for face in range(1, faces +1)
        if face > target:
            continue

        count_dice(processed +str(face), target - face, faces)

def dicePath3(processed, targrt, faces):

    if target == 0:
        if len(processed) <= 3:
           print(processed)
        return

    for face in range(1,faces + 1):
        if face > target:
            continue
        dicePath3(processed + str(face), target - face, faces)


def count_dice3(processed, targrt, faces):
    if target == 0:
        return 1
    else:
        return 0
    acc = 0

    for face in range(1,faces + 1):
        if face > target:
            continue
    countdice3(processed + str(face), target - face, faces)