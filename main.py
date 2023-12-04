
# Import necessary modules
import tkinter as tk
# Define main function
def main():
    r = tk.Tk()
    r.title('Counting Seconds')
    button = tk.Button(r, text='Stop', width=25, command=r.destroy)
    button.pack()
    r.mainloop()

# Call the main function
if __name__ == "__main__":
    main()
