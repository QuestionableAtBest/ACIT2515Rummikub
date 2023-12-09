from pygame.sprite import Sprite,Group

# Idea is that this is the tabletop that stores all the sets of valid runs/groups. I use the rack class to simplify since there are many useful functions
class Table(Sprite):
    def __init__(self):
        super().__init__()
        self.racks = Group()
        
    def check_all_valid(self):
        for rack in self.racks:
            if not rack.is_valid():
                return False
            
    def is_valid(self, rack):
        return rack.valid_run() or rack.valid_set()