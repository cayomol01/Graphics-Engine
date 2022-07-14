from gl import Window
import time

start_time = time.time()

window = Window(1024,512,(1.0,255,0))

for i in range(512):
    window.point(i,i)
    
window.pointViewPort(0,0,(0,0,255))
    
window.finish()


print("--- %s seconds ---" % (time.time() - start_time))

exit()

