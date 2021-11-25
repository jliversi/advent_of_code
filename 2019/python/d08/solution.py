with open('input.txt') as f:
    INPUT = [int(x) for x in f.read()]

DIMS = (25,6)

IMG_SIZE = DIMS[0] * DIMS[1]

NUM_LAYERS = len(INPUT)//IMG_SIZE
LAYERS = [INPUT[(i*IMG_SIZE):(i*IMG_SIZE)+IMG_SIZE] for i in range(NUM_LAYERS)]


TRUE_IMAGE = []
for i, pixel in enumerate(LAYERS[0]):
    offset = 0
    while pixel == 2:
        offset += 1
        pixel = LAYERS[offset][i]
    TRUE_IMAGE.append('#' if pixel == 1 else ' ')


ROWS = [TRUE_IMAGE[(i*DIMS[0]):(i*DIMS[0])+DIMS[0]] for i in range(DIMS[1])]
for el in ROWS:
    print(''.join(el))







# PART 1
# LAYER_ZERO_COUNT = list(map(lambda x: x.count(0), LAYERS))
# MIN_LAYER_IDX = 0
# for i, el in enumerate(LAYER_ZERO_COUNT):
#     if el < LAYER_ZERO_COUNT[MIN_LAYER_IDX]:
#         MIN_LAYER_IDX = i

# a = LAYERS[MIN_LAYER_IDX]
# b = a.count(1) * a.count(2)
# print(b)