def diceDp(target, faces, memory):

     if target == 0:
         return 1

     if memory.get(target):
         return memory.get(target)

     acc = 0
     for face in range(1, faces + 1):
         if face > target:
             continue

         acc += diceDp(target-face, faces, memory)

     memory[target]  = acc

     return acc

print(diceDp(10,5, {}))
