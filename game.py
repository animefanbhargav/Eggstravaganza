from sprites import *

class Game:
    def __init__(self):
        
        self.window = pg.display.set_mode((WIDTH,HEIGHT))
        self.clock = pg.time.Clock()
        self.refresh()


    def refresh(self):
        self.running = True
        self.eggs = pg.sprite.Group()
        self.bubbles = pg.sprite.Group()
        self.score = 0
        self.currentEggs =0
        #self.maxEggs = 100
        self.shooter = Bubble(self)
        self.arrow = Arrow(self)
        self.last_clicked = pg.time.get_ticks()
        self.click_thres = 200


    def draw(self):
        self.bubbles.update()
        self.bubbles.draw(self.window)

        self.eggs.update()
        self.eggs.draw(self.window)

        self.arrow.update()
        self.window.blit(self.arrow.image,self.arrow.rect)

        self.shooter.update()
        self.window.blit(self.shooter.image,self.shooter.rect)

        


    def check_events(self):
        now = pg.time.get_ticks()
        if pg.mouse.get_pressed()[0] and now-self.last_clicked >self.click_thres:
            #Mouse clicked
            self.bubbles.add(Bubble(self,self.shooter.pos,self.arrow.direction,(rand(1,255),rand(1,255),rand(1,255))))
            self.last_clicked = now

    def spawn_eggs(self):
        r = rand(1,100)
        if r < 5:
            egg = Egg(self)
            self.eggs.add(egg)
            self.currentEggs+=1
            

    def run(self):
        while self.running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()
            
            self.spawn_eggs()
            self.check_events()
            self.window.fill(-1)
            self.draw()
            pg.display.update()
            self.clock.tick(60)



game = Game()
game.run()