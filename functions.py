import random
import dice

path = ['dice1.jpg', 'dice2.jpg', 'dice3.jpg', 'dice4.jpg', 'dice5.jpg', 'dice6.jpg']

rnd_dice = random.randint(0,5)
photo_dice = dice.imread(path[rnd_dice])
dice.imshow(str(rnd_dice + 1), photo_dice)
dice.waitKey(0)