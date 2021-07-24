import unittest


class MyTestCase(unittest.TestCase):
    def player(x, y):
        screen.blit(playerImg, (x, y))

        playerX += playerX_change
        if playerX <= 0:
            playerX = 0
        elif playerX >= 736:
            playerX = 736

class MyTestCase(unittest.TestCase):
    def isCollision(enemyX, enemyY, bulletX, bulletY):

        distance = math.sqrt(math.pow(enemyX - bulletX, 2) + (math.pow(enemyY - bulletY, 2)))

    if distance < 27:
        return True
    else:
        return False

    collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
    if collision:
        explosionSound = mixer.Sound("explosion.wav")
        explosionSound.play()
        bulletY = 480
        bullet_state = "ready"
        score_value += 1
        enemyX[i] = random.randint(0, 736)
        enemyY[i] = random.randint(50, 150)

class MyTestCase(unittest.TestCase):
    def show_score(x, y):
        score = font.render("Score : " + str(score_value), True, (255, 255, 255))
        screen.blit(score, (x, y))
