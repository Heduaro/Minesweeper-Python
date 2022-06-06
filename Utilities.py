import Settings

#not calling immediately function in case of bugs
def height_prcnt(percentage):
    return (Settings.HEIGHT / 100) * percentage

def width_prcnt(percentage):
    return (Settings.WIDTH / 100) * percentage