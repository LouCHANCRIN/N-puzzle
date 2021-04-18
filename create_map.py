import os

for i in range(3, 15):
    for j in range(0, 50):
        os.system(f'python3 resources/n-puzzle-gen.py -u {i} > resources/unsolvable/unsolvable-{i}-{j}.txt ')
