from random import randint





class Cat:

    cat = []

    def play_with_cat(self):
        angry = randint(1, 100)
        if self.cat[0]['is_sleeping'] == True:
            if self.cat[0]['mood'] <=0:
                self.cat[0]['mood'] = 0
            else:
                self.cat[0]['is_sleeping'] = False
                self.cat[0]['mood'] -= 5
        elif angry >= 75:
            self.cat[0]['mood'] = 0
        else:
            if self.cat[0]['satiety'] <= 0:
                self.cat[0]['satiety'] = 0
            else:
                self.cat[0]['mood'] += 15
                self.cat[0]['satiety'] -= 10

    def feed_the_cat(self):
        if self.cat[0]['is_sleeping'] == True:
            self.cat[0]['is_sleeping'] = False
            self.cat[0]['satiety'] += 0
        elif self.cat[0]['satiety'] >= 70:
            self.cat[0]['mood'] -= 30
        else:
            self.cat[0]['satiety'] += 15
            self.cat[0]['mood'] += 5
    
    def put_to_sleep(self):
        self.cat[0]['is_sleeping'] = True
