l=float(input("enter the length:"))
w=float(input("enter the width:"))
h=float(input("enter the height:"))
def cuboid(l,w,h):
    surface_area=2*(l*w+l*h+w*h)
    return surface_area

surface_area=cuboid(l,w,h)
print("Surface area is:",surface_area)

def cuboid(l,w,h):
    volume=(l*w*h)
    return volume
volume=cuboid(l,w,h)
print("Volume is:",volume)    


    

