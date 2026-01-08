class Bird: ...

class Duck(Bird):
    def quack(self):
        print("Quack!")

def alert(birdie):
    birdie.quack()

def alert_duck(birdie: Duck):
    birdie.quack()

def alert_bird(birdie: Bird):
    birdie.quack()