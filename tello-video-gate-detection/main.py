import tello
from tello_control_ui import TelloUI


def main():

    drone = tello.Tello('', 8889)  
    vplayer = TelloUI(drone,"./img/")
    
	# start the Tkinter mainloop
    vplayer.root.mainloop() 

if __name__ == "__main__":
    main()
    
    while(1):
      frame = vplayer.frame
      if frame is None:
        print ("No frame")
      else:
        print ("Got frame shape {0}".format(frame.shape))

