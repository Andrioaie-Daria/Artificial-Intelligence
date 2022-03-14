# import the pygame module, so you can use it


from GUI.GUI import GUI


# define a main function
def main():
    view = GUI()
    view.run()


# run the main func
# tion only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__ == "__main__":
    # call the main function
    main()
