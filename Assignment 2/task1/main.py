from GUI.GUI import *

# define a main function
def main():
    gui = GUI()
    gui.run()


# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()