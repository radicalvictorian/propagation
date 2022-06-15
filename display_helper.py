def get_rgb_density(density):
    if density > 101325*4.5:
        output=(1,0,0)
    elif density > 101325*3.5:
        output=(0.5,0.5,0)
    elif density > 101325*2.5:
        output=(0,1,0)
    elif density > 101325*1.25:
        output=(0,0.5,0.5)
    else:
        output=(0,0,1)
    return output
