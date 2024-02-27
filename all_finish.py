import pygame
import sys
from BUTTON import Button

pygame.init()
clock = pygame.time.Clock()

pygame.display.set_caption('Ппррооеекктт')

current_scene = None


def switch_scenes(scene):
    global current_scene
    current_scene = scene


def scene():
    width, height = 1400, 700

    screen = pygame.display.set_mode((width, height))

    play = Button(500, 250, 380, 110, '', 'images_for_prj/play.png', \
                  'images_for_prj/play5.png', 'images_for_prj/klik.mp3')
    exit = Button(500, 430, 380, 110, '', 'images_for_prj/exit.png', 'images_for_prj/exit2.png',
                  'images_for_prj/klik.mp3')
    bg = pygame.image.load('images_for_prj/fsd.png')
    bg = pygame.transform.scale(bg, (1400, 700))

    play_rect = play.image.get_rect()
    play_rect.y += 250
    play_rect.x += 500
    print(play_rect)

    exit_rect = exit.image.get_rect()
    exit_rect.y += 430
    exit_rect.x += 500

    def main_menu():
        running = True
        contin = 0
        while running:
            screen.blit(bg, (0, 0))
            font = pygame.font.Font('fonts/minecraft-ten-font-cyrillic.ttf', 90)
            text_srfc = font.render('Начало Игры', True, '#474A51')
            screen.blit(text_srfc, (330, 40))
            mouse = pygame.mouse.get_pos()
            if play_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
                contin = 10
            if exit_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
                pygame.quit()
            if contin == 10:
                switch_scenes(scene1)
                running = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    sys.exit()
                play.handle_event(event)
                exit.handle_event(event)
            play.check_hover(pygame.mouse.get_pos())
            play.draw(screen)
            exit.draw(screen)
            exit.check_hover(pygame.mouse.get_pos())
            pygame.display.flip()

    main_menu()


def scene1():
    screen_width = 1700
    screen_height = 900

    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Ппррооеекктт')

    game_over = 0
    count = 0

    size_of_person = 60, 60

    tl_sz = 50

    NUMBER_MAPS = 1

    world_data1 = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 4, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 7, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 7, 0, 7, 7, 7, 6, 6, 7, 7, 7, 7, 0, 7, 7, 7, 7, 7, 0, 0],
        [0, 0, 0, 0, 7, 7, 7, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [6, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 7, 0, 0, 0, 0, 7, 7, 5, 5, 7, 7, 7, 7, 7, 7, 7, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7],
        [0, 0, 0, 0, 0, 0, 1, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0],
        [0, 0, 0, 0, 0, 1, 0, 1, 5, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 7, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 6, 6, 6, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
    ]

    world_data2 = [
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 5, 5, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
    ]

    # def realize_levels(level):
    # player.reset(100,)

    class World:
        def __init__(self, data):
            self.tile_list = []
            grass_image = pygame.image.load('images_for_prj/trava.png')
            dirt_image = pygame.image.load('images_for_prj/z.png')
            stone_image = pygame.image.load('images_for_prj/stone.png')
            row_count = 0
            for row in data:
                col_count = 0
                for tile in row:
                    if tile == 1:
                        img = pygame.transform.scale(grass_image, (tl_sz, tl_sz))
                        img_rect = img.get_rect()
                        img_rect.x = col_count * tl_sz
                        img_rect.y = row_count * tl_sz
                        tile = (img, img_rect)
                        self.tile_list.append(tile)
                    if tile == 2:
                        img = pygame.transform.scale(dirt_image, (tl_sz, tl_sz))
                        img_rect = img.get_rect()
                        img_rect.x = col_count * tl_sz
                        img_rect.y = row_count * tl_sz
                        tile = (img, img_rect)
                        self.tile_list.append(tile)
                    if tile == 3:
                        vrag = Enemies(col_count * tl_sz, row_count * tl_sz - 15)
                        enemies_group.add(vrag)
                        vrag_list.append(vrag.rect)
                    if tile == 4:
                        end = The_End(col_count * tl_sz, row_count * tl_sz)
                        the_end_group.add(end)
                    if tile == 5:
                        sharps = Sharp(col_count * tl_sz, row_count * tl_sz + (tl_sz // 2.5))
                        sharp_group.add(sharps)
                    if tile == 6:
                        poison = Poison(col_count * tl_sz, row_count * tl_sz + (tl_sz // 2))
                        poison_group.add(poison)
                    if tile == 7:
                        img = pygame.transform.scale(stone_image, (tl_sz, tl_sz))
                        img_rect = img.get_rect()
                        img_rect.x = col_count * tl_sz
                        img_rect.y = row_count * tl_sz
                        tile = (img, img_rect)
                        self.tile_list.append(tile)
                    col_count += 1
                row_count += 1

        def draw(self):
            for tile in self.tile_list:
                screen.blit(tile[0], tile[1])
                # pygame.draw.rect(screen, (255, 255, 255), tile[1], 2)

    sharp_group = pygame.sprite.Group()
    walk_right = [
        pygame.image.load('images_for_prj/1.png'),
        pygame.image.load('images_for_prj/2.png'),
        pygame.image.load('images_for_prj/3.png'),
        pygame.image.load('images_for_prj/4.png'),
        pygame.image.load('images_for_prj/5.png'),
        pygame.image.load('images_for_prj/6.png')
    ]
    walk_left = [
        pygame.transform.flip(walk_right[0], True, False),
        pygame.transform.flip(walk_right[1], True, False),
        pygame.transform.flip(walk_right[2], True, False),
        pygame.transform.flip(walk_right[3], True, False),
        pygame.transform.flip(walk_right[4], True, False),
        pygame.transform.flip(walk_right[5], True, False)
    ]

    class Player():
        def __init__(self, x, y):
            self.imaa = pygame.image.load('images_for_prj/dead.png')
            self.gmovr = pygame.transform.scale(self.imaa, (100, 100))
            # self.level = pygame.image.load('images_for_prj/level_complete.png')
            # self.level = pygame.transform.scale(self.level, (900, 225))
            font = pygame.font.Font('fonts/minecraft-ten-font-cyrillic.ttf', 80)
            self.level = font.render('Level', False, '#480607')
            self.level2 = font.render('Completed', False, '#480607')

            self.contine = pygame.image.load('images_for_prj/continue_button-fotor-bg-remover-2024022712436.png')
            self.contine = pygame.transform.scale(self.contine, (500, 500))
            self.images_left = []
            self.images_right = []
            self.index = 0
            self.cnt = 0
            for _ in range(4):
                for i in range(1, 7):
                    self.limage = pygame.image.load(f'images_for_prj/11{i}.png')
                    imageright = pygame.transform.scale(self.limage, (90, 130))
                    self.rimage = pygame.transform.flip(imageright, True, False)
                    self.images_left.append(imageright)
                    self.images_right.append(self.rimage)
            self.image = self.images_left[self.index]
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.width = self.image.get_width()
            self.height = self.image.get_height()

            self.jumping = 0
            self.check_jump = True
            self.dir = 0
            self.jumped = False

        def update(self, game_over):
            pos_x = 0
            pos_y = 0

            walk_sp = 10

            if game_over == 0:
                key = pygame.key.get_pressed()
                if key[pygame.K_SPACE] and self.jumped is False and self.check_jump is False:
                    self.jumping = -15
                    self.jumped = True
                if key[pygame.K_SPACE] is False:
                    self.jumped = False
                if key[pygame.K_LEFT]:
                    pos_x -= 6
                    self.cnt += 1
                    self.dir = -1
                if key[pygame.K_RIGHT]:
                    pos_x += 6
                    self.cnt += 1
                    self.dir = 1
                if key[pygame.K_LEFT] is False and key[pygame.K_RIGHT] is False:
                    self.cnt = 0
                    self.index = 0
                    if self.dir == 1:
                        self.image = self.images_right[0]
                    if self.dir == -1:
                        self.image = self.images_left[0]

                self.cnt += 1
                if self.cnt > walk_sp:
                    self.cnt = 0
                    self.index += 1
                    if self.index >= len(self.images_left):
                        self.index = 0
                    if self.dir == 1:
                        self.image = self.images_right[self.index]
                    if self.dir == -1:
                        self.image = self.images_left[self.index]

                self.jumping += 1
                if self.jumping > 10:
                    self.jumping = 10
                pos_y += self.jumping

                self.check_jump = True
                for i in world.tile_list:
                    if i[1].colliderect(self.rect.x + pos_x, self.rect.y, self.width, self.height):
                        pos_x = 0
                    if i[1].colliderect(self.rect.x, self.rect.y + pos_y, self.width, self.height):
                        if self.jumping < 0:
                            pos_y = i[1].bottom - self.rect.top
                            self.jumping = 0
                        elif self.jumping >= 0:
                            pos_y = i[1].top - self.rect.bottom
                            self.jumping = 0
                            self.check_jump = False

                if pygame.sprite.spritecollide(self, enemies_group, False):
                    game_over = 1
                    print(game_over)

                if pygame.sprite.spritecollide(self, sharp_group, False):
                    game_over = 1

                if pygame.sprite.spritecollide(self, the_end_group, False):
                    game_over = 1000
                    print(game_over)
                if pygame.sprite.spritecollide(self, poison_group, False):
                    game_over = 1

                self.rect.x += pos_x
                self.rect.y += pos_y

                if self.rect.bottom > screen_height:
                    self.rect.bottom = screen_height
                    pos_y = 0
            elif game_over == 1:
                self.image = self.gmovr
                if self.rect.y > 100:
                    self.rect.y -= 5
                self.gamver1 = pygame.image.load('images_for_prj/dsffdsf (1).png')
                self.gamver = pygame.transform.scale(self.gamver1, (800, 800))
                self.restart1 = pygame.image.load('images_for_prj/l7fc3fd41rc.png')
                self.restart = pygame.transform.scale(self.restart1, (300, 300))
                screen.blit(self.restart, (630, 500))
                restart_rect = self.restart1.get_rect()
                restart_rect.x = restart_rect.x + 580
                restart_rect.y = restart_rect.y + 400
                print(restart_rect)
                screen.blit(self.gamver, (400, -200))
                mouse = pygame.mouse.get_pos()
                if restart_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
                    game_over = -1
                    self.rect.x = 10
            elif game_over == 1000:
                screen.blit(self.contine, (590, 280))
                screen.blit(self.level, (400, 190))
                screen.blit(self.level2, (730, 190))
                contin = self.contine.get_rect()
                contin.x += 590
                contin.y += 280
                mouse = pygame.mouse.get_pos()
                if contin.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
                    game_over = 10

            screen.blit(self.image, self.rect)
            return game_over

    enemies_group = pygame.sprite.Group()

    class Sharp(pygame.sprite.Sprite):
        def __init__(self, x, y):
            pygame.sprite.Sprite.__init__(self)
            img = pygame.image.load('images_for_prj/ship.png')
            self.image = pygame.transform.scale(img, (tl_sz, tl_sz // 1.5))
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y

    class Enemies(pygame.sprite.Sprite):
        def __init__(self, x, y):
            pygame.sprite.Sprite.__init__(self)
            self.img = pygame.image.load('images_for_prj/enemy.png')
            self.index = 0
            self.imagess = pygame.transform.scale(self.img, (100, 130))
            self.rimage = pygame.transform.flip(self.imagess, True, False)
            self.images = [self.imagess, self.rimage]
            self.image = self.images[self.index]
            self.rect = self.image.get_rect()

            self.rect.x = x
            self.rect.y = y
            self.enemy_speed = 10
            self.enemy_cnt = 0

            self.index = 0
            self.cnt = 0

            self.jumping = 0
            self.check_jump = True
            self.dir = 0
            self.jumped = False

        def update(self):
            self.rect.x += self.enemy_speed
            self.enemy_cnt += 2
            if abs(self.enemy_cnt) > 30:
                self.enemy_speed *= -1
                self.enemy_cnt *= -1
                self.index = 1

    the_end_group = pygame.sprite.Group()

    class Poison(pygame.sprite.Sprite):
        def __init__(self, x, y):
            pygame.sprite.Sprite.__init__(self)
            img = pygame.image.load('images_for_prj/lava1.png')
            self.image = pygame.transform.scale(img, (tl_sz, tl_sz // 2))
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y

    poison_group = pygame.sprite.Group()

    class The_End(pygame.sprite.Sprite):
        def __init__(self, x, y):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load('images_for_prj/door-fotor-bg-remover-20240227162617.png')
            self.image = pygame.transform.scale(self.image, (180, 108))
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y

    money = [
        pygame.image.load('images_for_prj/mon1.png'),
        pygame.image.load('images_for_prj/mon2.png'),
        pygame.image.load('images_for_prj/mon3.png'),
        pygame.image.load('images_for_prj/mon4.png'),
        pygame.image.load('images_for_prj/mon5.png'),
        pygame.image.load('images_for_prj/mon6.png'),
        pygame.image.load('images_for_prj/mon7.png')
    ]
    money_list = []
    money_animation_count = 0
    money_speed = 10
    money_count_needable = 4
    points = 0

    vrag_list = []

    count_bullet = []
    bullet = pygame.image.load('images/blt.png')
    bullets_left = 3
    world = World(world_data1)
    lbl = pygame.font.Font('fonts/minecraft-ten-font-cyrillic.ttf', 50)
    background = pygame.image.load('images_for_prj/phone1.png')
    heart = pygame.image.load('images_for_prj/heart.png')
    coint = pygame.image.load('images_for_prj/mon4.png')
    image_bul = pygame.image.load('images_for_prj/bul.png')
    image_bul = pygame.transform.scale(image_bul, (80, 80))
    true_heart = pygame.transform.scale(heart, (80, 80))
    true_coin = pygame.transform.scale(coint, (80, 80))
    count_heart = 1
    running = True
    gameplay = True
    player = Player(100, screen_height - 130)
    print(count)
    print(vrag_list)
    all_score = 0
    kills_mob = 0
    sound = pygame.mixer.Sound('images_for_prj/81cebf7e45fdef7.mp3')
    sound.play()
    while running:
        razn = clock.tick(110)
        screen.blit(background, (0, 0))
        label_points = lbl.render(str(points) + '/5', False, '#FFCF40')
        label_hearts = lbl.render(str(count_heart), False, '#CD5C5C')
        label_bullets = lbl.render(str(bullets_left) + '/3', False, '#FFCF40')
        font = pygame.font.Font('fonts/minecraft-ten-font-cyrillic.ttf', 40)
        score = font.render(str(all_score), False, '#646B63')

        text_srfc = font.render('SCORE:', False, '#646B63')
        screen.blit(label_bullets, (1550, 200))
        screen.blit(image_bul, (1430, 200))
        screen.blit(text_srfc, (20, 100))
        screen.blit(score, (200, 100))
        screen.blit(label_points, (150, 20))
        screen.blit(label_hearts, (1530, 15))

        spisok_gde_moneti = [[1200, 700], [50, 500], [850, 350], [60, 45], [1200, 85]]
        screen.blit(true_heart, (1420, 20))
        screen.blit(true_coin, (20, 20))
        if game_over == 0:
            enemies_group.update()
        if game_over == -1:
            switch_scenes(scene)
            running = False
            sound.stop()
        if game_over == 10:
            f = open('images_for_prj/res.txt', 'r+')
            f.writelines(f'{kills_mob} {all_score}')
            print(all_score)
            f.close()
            sound.stop()
            switch_scenes(scene2)
            running = False

        world.draw()
        enemies_group.draw(screen)
        the_end_group.draw(screen)
        sharp_group.draw(screen)
        poison_group.draw(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    pygame.quit()
            if gameplay and event.type == pygame.KEYUP and event.key == pygame.K_q and bullets_left > 0:
                count_bullet.append(bullet.get_rect(topleft=(player.rect.x + 100, player.rect.y + 43)))
                bullets_left -= 1
        if money_animation_count == 6:
            money_animation_count = 0
        else:
            money_animation_count += 1

        if count_bullet:
            for i, elem in enumerate(count_bullet):
                screen.blit(bullet, (elem.x, elem.y))
                elem.x += 10

                if elem.x > 1400:
                    count_bullet.pop(i)

                if enemies_group:
                    for i, vrags in enumerate(enemies_group):
                        if elem.colliderect(vrags):
                            all_score += 100
                            kills_mob += 1
                            enemies_group.remove(vrags)
                            count_bullet.pop(i - 1)
        while money_count_needable >= 0:
            money_list.append(money[money_animation_count].get_rect(
                topleft=(spisok_gde_moneti[money_count_needable][0], spisok_gde_moneti[money_count_needable][1])))
            money_count_needable -= 1
        if money_list:
            for i, mon_ind in enumerate(money_list):
                screen.blit(pygame.transform.scale(money[money_animation_count], (50, 50)), mon_ind)
                if mon_ind.colliderect(player.rect):
                    money_list.pop(i)
                    points += 1
                    all_score += 50
        game_over = player.update(game_over)
        pygame.display.update()


def scene2():
    screen_width = 1700
    screen_height = 900

    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Ппррооеекктт')

    game_over = 0
    count = 0

    size_of_person = 60, 60

    tl_sz = 50

    NUMBER_MAPS = 1

    world_data1 = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 7, 7, 7, 5, 5, 5, 5, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 6, 6, 6, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 3, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 5, 5, 5, 5, 1, 6, 6, 6, 1, 6, 6, 6, 6, 1, 6, 6, 6, 6, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
    ]

    # def realize_levels(level):
    # player.reset(100,)

    class World:
        def __init__(self, data):
            self.tile_list = []
            grass_image = pygame.image.load('images_for_prj/trava.png')
            dirt_image = pygame.image.load('images_for_prj/z.png')
            stone_image = pygame.image.load('images_for_prj/stone.png')
            row_count = 0
            for row in data:
                col_count = 0
                for tile in row:
                    if tile == 1:
                        img = pygame.transform.scale(grass_image, (tl_sz, tl_sz))
                        img_rect = img.get_rect()
                        img_rect.x = col_count * tl_sz
                        img_rect.y = row_count * tl_sz
                        tile = (img, img_rect)
                        self.tile_list.append(tile)
                    if tile == 2:
                        img = pygame.transform.scale(dirt_image, (tl_sz, tl_sz))
                        img_rect = img.get_rect()
                        img_rect.x = col_count * tl_sz
                        img_rect.y = row_count * tl_sz
                        tile = (img, img_rect)
                        self.tile_list.append(tile)
                    if tile == 3:
                        vrag = Enemies(col_count * tl_sz, row_count * tl_sz - 15)
                        enemies_group.add(vrag)
                        vrag_list.append(vrag.rect)
                    if tile == 4:
                        end = The_End(col_count * tl_sz, row_count * tl_sz)
                        the_end_group.add(end)
                    if tile == 5:
                        sharps = Sharp(col_count * tl_sz, row_count * tl_sz + (tl_sz // 2.5))
                        sharp_group.add(sharps)
                    if tile == 6:
                        poison = Poison(col_count * tl_sz, row_count * tl_sz + (tl_sz // 2))
                        poison_group.add(poison)
                    if tile == 7:
                        img = pygame.transform.scale(stone_image, (tl_sz, tl_sz))
                        img_rect = img.get_rect()
                        img_rect.x = col_count * tl_sz
                        img_rect.y = row_count * tl_sz
                        tile = (img, img_rect)
                        self.tile_list.append(tile)
                    col_count += 1
                row_count += 1

        def draw(self):
            for tile in self.tile_list:
                screen.blit(tile[0], tile[1])
                # pygame.draw.rect(screen, (255, 255, 255), tile[1], 2)

    sharp_group = pygame.sprite.Group()
    walk_right = [
        pygame.image.load('images_for_prj/1.png'),
        pygame.image.load('images_for_prj/2.png'),
        pygame.image.load('images_for_prj/3.png'),
        pygame.image.load('images_for_prj/4.png'),
        pygame.image.load('images_for_prj/5.png'),
        pygame.image.load('images_for_prj/6.png')
    ]
    walk_left = [
        pygame.transform.flip(walk_right[0], True, False),
        pygame.transform.flip(walk_right[1], True, False),
        pygame.transform.flip(walk_right[2], True, False),
        pygame.transform.flip(walk_right[3], True, False),
        pygame.transform.flip(walk_right[4], True, False),
        pygame.transform.flip(walk_right[5], True, False)
    ]

    class Player():
        def __init__(self, x, y):
            self.imaa = pygame.image.load('images_for_prj/dead.png')
            self.gmovr = pygame.transform.scale(self.imaa, (100, 100))
            # self.level = pygame.image.load('images_for_prj/level_complete.png')
            # self.level = pygame.transform.scale(self.level, (900, 225))
            font = pygame.font.Font('fonts/minecraft-ten-font-cyrillic.ttf', 80)
            self.level = font.render('Level', False, '#480607')
            self.level2 = font.render('Completed', False, '#480607')

            self.contine = pygame.image.load('images_for_prj/continue_button-fotor-bg-remover-2024022712436.png')
            self.contine = pygame.transform.scale(self.contine, (500, 500))
            self.images_left = []
            self.images_right = []
            self.index = 0
            self.cnt = 0
            for _ in range(4):
                for i in range(1, 7):
                    self.limage = pygame.image.load(f'images_for_prj/11{i}.png')
                    imageright = pygame.transform.scale(self.limage, (90, 130))
                    self.rimage = pygame.transform.flip(imageright, True, False)
                    self.images_left.append(imageright)
                    self.images_right.append(self.rimage)
            self.image = self.images_left[self.index]
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.width = self.image.get_width()
            self.height = self.image.get_height()

            self.jumping = 0
            self.check_jump = True
            self.dir = 0
            self.jumped = False

        def update(self, game_over):
            pos_x = 0
            pos_y = 0

            walk_sp = 10

            if game_over == 0:
                key = pygame.key.get_pressed()
                if key[pygame.K_SPACE] and self.jumped is False and self.check_jump is False:
                    self.jumping = -15
                    self.jumped = True
                if key[pygame.K_SPACE] is False:
                    self.jumped = False
                if key[pygame.K_LEFT]:
                    pos_x -= 6
                    self.cnt += 1
                    self.dir = -1
                if key[pygame.K_RIGHT]:
                    pos_x += 6
                    self.cnt += 1
                    self.dir = 1
                if key[pygame.K_LEFT] is False and key[pygame.K_RIGHT] is False:
                    self.cnt = 0
                    self.index = 0
                    if self.dir == 1:
                        self.image = self.images_right[0]
                    if self.dir == -1:
                        self.image = self.images_left[0]

                self.cnt += 1
                if self.cnt > walk_sp:
                    self.cnt = 0
                    self.index += 1
                    if self.index >= len(self.images_left):
                        self.index = 0
                    if self.dir == 1:
                        self.image = self.images_right[self.index]
                    if self.dir == -1:
                        self.image = self.images_left[self.index]

                self.jumping += 1
                if self.jumping > 10:
                    self.jumping = 10
                pos_y += self.jumping

                self.check_jump = True
                for i in world.tile_list:
                    if i[1].colliderect(self.rect.x + pos_x, self.rect.y, self.width, self.height):
                        pos_x = 0
                    if i[1].colliderect(self.rect.x, self.rect.y + pos_y, self.width, self.height):
                        if self.jumping < 0:
                            pos_y = i[1].bottom - self.rect.top
                            self.jumping = 0
                        elif self.jumping >= 0:
                            pos_y = i[1].top - self.rect.bottom
                            self.jumping = 0
                            self.check_jump = False

                if pygame.sprite.spritecollide(self, enemies_group, False):
                    game_over = 1
                    print(game_over)

                if pygame.sprite.spritecollide(self, sharp_group, False):
                    game_over = 1

                if pygame.sprite.spritecollide(self, the_end_group, False):
                    game_over = 1000
                    print(game_over)
                if pygame.sprite.spritecollide(self, poison_group, False):
                    game_over = 1

                self.rect.x += pos_x
                self.rect.y += pos_y

                if self.rect.bottom > screen_height:
                    self.rect.bottom = screen_height
                    pos_y = 0
            elif game_over == 1:
                self.image = self.gmovr
                if self.rect.y > 100:
                    self.rect.y -= 5
                self.gamver1 = pygame.image.load('images_for_prj/dsffdsf (1).png')
                self.gamver = pygame.transform.scale(self.gamver1, (800, 800))
                self.restart1 = pygame.image.load('images_for_prj/l7fc3fd41rc.png')
                self.restart = pygame.transform.scale(self.restart1, (300, 300))
                screen.blit(self.restart, (630, 500))
                restart_rect = self.restart1.get_rect()
                restart_rect.x = restart_rect.x + 580
                restart_rect.y = restart_rect.y + 400
                print(restart_rect)
                screen.blit(self.gamver, (400, -200))
                mouse = pygame.mouse.get_pos()
                if restart_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
                    game_over = -1
                    self.rect.x = 10
            elif game_over == 1000:
                screen.blit(self.contine, (590, 280))
                screen.blit(self.level, (400, 190))
                screen.blit(self.level2, (730, 190))
                contin = self.contine.get_rect()
                contin.x += 590
                contin.y += 280
                mouse = pygame.mouse.get_pos()
                if contin.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
                    game_over = 10

            screen.blit(self.image, self.rect)
            return game_over

    enemies_group = pygame.sprite.Group()

    class Sharp(pygame.sprite.Sprite):
        def __init__(self, x, y):
            pygame.sprite.Sprite.__init__(self)
            img = pygame.image.load('images_for_prj/ship.png')
            self.image = pygame.transform.scale(img, (tl_sz, tl_sz // 1.5))
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y

    class Enemies(pygame.sprite.Sprite):
        def __init__(self, x, y):
            pygame.sprite.Sprite.__init__(self)
            self.img = pygame.image.load('images_for_prj/enemy.png')
            self.index = 0
            self.imagess = pygame.transform.scale(self.img, (100, 130))
            self.rimage = pygame.transform.flip(self.imagess, True, False)
            self.images = [self.imagess, self.rimage]
            self.image = self.images[self.index]
            self.rect = self.image.get_rect()

            self.rect.x = x
            self.rect.y = y
            self.enemy_speed = 10
            self.enemy_cnt = 0

            self.index = 0
            self.cnt = 0

            self.jumping = 0
            self.check_jump = True
            self.dir = 0
            self.jumped = False

        def update(self):
            self.rect.x += self.enemy_speed
            self.enemy_cnt += 2
            if abs(self.enemy_cnt) > 30:
                self.enemy_speed *= -1
                self.enemy_cnt *= -1
                self.index = 1

    the_end_group = pygame.sprite.Group()

    class Poison(pygame.sprite.Sprite):
        def __init__(self, x, y):
            pygame.sprite.Sprite.__init__(self)
            img = pygame.image.load('images_for_prj/lava1.png')
            self.image = pygame.transform.scale(img, (tl_sz, tl_sz // 2))
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y

    poison_group = pygame.sprite.Group()

    class The_End(pygame.sprite.Sprite):
        def __init__(self, x, y):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load('images_for_prj/minion-fotor-bg-remover-20240227171127.png')
            self.image = pygame.transform.scale(self.image, (200, 200))
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y

    money = [
        pygame.image.load('images_for_prj/mon1.png'),
        pygame.image.load('images_for_prj/mon2.png'),
        pygame.image.load('images_for_prj/mon3.png'),
        pygame.image.load('images_for_prj/mon4.png'),
        pygame.image.load('images_for_prj/mon5.png'),
        pygame.image.load('images_for_prj/mon6.png'),
        pygame.image.load('images_for_prj/mon7.png')
    ]
    money_list = []
    money_animation_count = 0
    money_speed = 10
    money_count_needable = 4
    points = 0

    vrag_list = []

    count_bullet = []
    bullet = pygame.image.load('images/blt.png')
    bullets_left = 3
    world = World(world_data1)
    lbl = pygame.font.Font('fonts/minecraft-ten-font-cyrillic.ttf', 50)
    background = pygame.image.load('images_for_prj/phone1.png')
    heart = pygame.image.load('images_for_prj/heart.png')
    coint = pygame.image.load('images_for_prj/mon4.png')
    image_bul = pygame.image.load('images_for_prj/bul.png')
    image_bul = pygame.transform.scale(image_bul, (80, 80))
    true_heart = pygame.transform.scale(heart, (80, 80))
    true_coin = pygame.transform.scale(coint, (80, 80))
    count_heart = 1
    running = True
    gameplay = True
    player = Player(100, screen_height - 130)
    print(count)
    print(vrag_list)
    all_score = 0
    kills_mob = 0
    sound = pygame.mixer.Sound('images_for_prj/81cebf7e45fdef7.mp3')
    sound.play()
    while running:
        razn = clock.tick(110)
        screen.blit(background, (0, 0))
        label_points = lbl.render(str(points) + '/5', False, '#FFCF40')
        label_hearts = lbl.render(str(count_heart), False, '#CD5C5C')
        label_bullets = lbl.render(str(bullets_left) + '/3', False, '#FFCF40')
        font = pygame.font.Font('fonts/minecraft-ten-font-cyrillic.ttf', 40)
        score = font.render(str(all_score), False, '#646B63')

        text_srfc = font.render('SCORE:', False, '#646B63')
        screen.blit(label_bullets, (1550, 240))
        screen.blit(image_bul, (1430, 250))
        screen.blit(text_srfc, (20, 100))
        screen.blit(score, (200, 100))
        screen.blit(label_points, (150, 20))
        screen.blit(label_hearts, (1530, 15))

        spisok_gde_moneti = [[450, 750], [650, 750], [900, 750], [800, 450], [550, 50]]
        screen.blit(true_heart, (1420, 20))
        screen.blit(true_coin, (20, 20))
        if game_over == 0:
            enemies_group.update()
        if game_over == -1:
            switch_scenes(scene)
            sound.stop()
            running = False
        if game_over == 10:
            f = open('images_for_prj/res1.txt', 'r+')
            f.writelines(f'{kills_mob} {all_score}')
            print(all_score)
            f.close()
            switch_scenes(scene3)
            sound.stop()
            running = False

        world.draw()
        enemies_group.draw(screen)
        the_end_group.draw(screen)
        sharp_group.draw(screen)
        poison_group.draw(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    pygame.quit()
            if gameplay and event.type == pygame.KEYUP and event.key == pygame.K_q and bullets_left > 0:
                count_bullet.append(bullet.get_rect(topleft=(player.rect.x + 100, player.rect.y + 43)))
                bullets_left -= 1
        if money_animation_count == 6:
            money_animation_count = 0
        else:
            money_animation_count += 1

        if count_bullet:
            for i, elem in enumerate(count_bullet):
                screen.blit(bullet, (elem.x, elem.y))
                elem.x += 10

                if elem.x > 1400:
                    count_bullet.pop(i)

                if enemies_group:
                    for i, vrags in enumerate(enemies_group):
                        if elem.colliderect(vrags):
                            all_score += 100
                            kills_mob += 1
                            enemies_group.remove(vrags)
                            count_bullet.pop(i - 1)
        while money_count_needable >= 0:
            money_list.append(money[money_animation_count].get_rect(
                topleft=(spisok_gde_moneti[money_count_needable][0], spisok_gde_moneti[money_count_needable][1])))
            money_count_needable -= 1
        if money_list:
            for i, mon_ind in enumerate(money_list):
                screen.blit(pygame.transform.scale(money[money_animation_count], (50, 50)), mon_ind)
                if mon_ind.colliderect(player.rect):
                    money_list.pop(i)
                    points += 1
                    all_score += 50
        game_over = player.update(game_over)
        pygame.display.update()


def scene3():
    width, height = 1430, 810

    screen = pygame.display.set_mode((width, height))

    bg = pygame.image.load('images_for_prj/end.png')
    bg = pygame.transform.scale(bg, (1430, 810))
    sound = pygame.mixer.Sound('images_for_prj/9f3e49b8de7c9d7.mp3')
    sound.play()

    def finish_menu():
        running = True
        finish1 = open('images_for_prj/res.txt')
        kills1, score1 = map(int, finish1.readline().split())
        finish2 = open('images_for_prj/res1.txt')
        kills2, score2 = map(int, finish2.readline().split())
        print(kills1, score1, kills2, score2)
        while running:
            screen.blit(bg, (0, 0))
            font = pygame.font.Font('fonts/minecraft-ten-font-cyrillic.ttf', 35)
            font1 = pygame.font.Font('fonts/minecraft-ten-font-cyrillic.ttf', 90)
            full_score = font1.render(f'{score2 + score1}', True, (255, 255, 255))
            full_kills = font1.render(f'{kills1 + kills2}', True, (255, 255, 255))
            text_srfc = font.render('Количество Очков', True, (255, 255, 255))
            text_srfc1 = font.render('Количество Убийств', True, (255, 255, 255))
            text_srfc2 = font.render('Чтобы выйти нажмите ESC', True, (255, 255, 255))
            screen.blit(text_srfc, (30, 150))
            screen.blit(text_srfc1, (880, 150))
            screen.blit(text_srfc2, (390, 700))
            screen.blit(full_score, (140, 300))
            screen.blit(full_kills, (1150, 300))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                        pygame.quit()
            pygame.display.flip()

    finish_menu()


switch_scenes(scene)
while current_scene is not None:
    current_scene()
pygame.quit()
