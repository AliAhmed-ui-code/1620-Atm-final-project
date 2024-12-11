from tkinter import *
from logic import *
from tkinter import messagebox
import csv

class Gui:
    def __init__(self, window)->None:
        """
        This function creates the widgets on the gui
        :param window: This is the GUI window that is created in Main
        """
        def toggle(option):
            if option == "Checking":
                self.var2.set(0)
                self.frame_eight.pack()
                self.frame_nine.pack()
                self.frame_eleven.pack()
            elif option == "Savings":
                self.var1.set(0)
                self.frame_eight.pack()
                self.frame_nine.pack()
                self.frame_eleven.pack()
            #Source for chexboxes: https://www.geeksforgeeks.org/python-tkinter-checkbutton-widget/

        self.window = window
        # Title
        self.frame_one = Frame(self.window)
        self.title_name = Label(self.frame_one, text='ATM', font=("Times New Roman", 40))
        self.title_name.pack(padx=200)
        self.frame_one.pack(anchor='w')
        # First Name
        self.frame_two = Frame(self.window)
        self.first_name = Label(self.frame_two, text='First Name', font=("Times New Roman", 15))
        self.first_name_entry = Entry(self.frame_two, width=20)
        self.first_name.pack(padx=10, side='left')
        self.first_name_entry.pack(padx=10, side='left')
        self.frame_two.pack(anchor='w')
        # Last Name
        self.frame_three = Frame(self.window)
        self.last_name = Label(self.frame_three, text='Last Name', font=("Times New Roman", 15))
        self.last_name_entry = Entry(self.frame_three, width=20)
        self.last_name.pack(padx=10, side='left')
        self.last_name_entry.pack(padx=10, side='left')
        self.frame_three.pack(anchor='w')
        # Pin
        self.frame_four = Frame(self.window)
        self.pin = Label(self.frame_four, text='Pin', font=("Times New Roman", 15))
        self.pin_entry = Entry(self.frame_four, show="*", width=15)
        self.pin.pack(side='left', padx=10)
        self.pin_entry.pack(side='left')
        self.frame_four.pack(anchor='w')
        # Search button
        self.frame_five = Frame(self.window)
        self.search_button = Button(self.frame_five, text='SEARCH', command=self.search)
        self.search_button.pack()
        self.frame_five.pack()
        # Welcome Label
        self.frame_six = Frame(self.window)
        self.welcome_label = Label(self.frame_six, text="", fg="black", font=("Times New Roman", 15))
        self.action_label = Label(self.frame_six, text='', fg='black', font=("Times New Roman", 15))
        self.welcome_label.pack()
        self.action_label.pack(pady=10)
        self.frame_six.pack()
        # Button (Checking vs Savings)
        self.frame_seven = Frame(self.window)
        self.var1 = IntVar()  # Make these instance variables
        self.var2 = IntVar()
        cb_checking = Checkbutton(self.frame_seven, text='Checking', font=("Times New Roman", 15), variable=self.var1, command=lambda: toggle('Checking'))
        cb_savings = Checkbutton(self.frame_seven, text='Savings', font=("Times New Roman", 15), variable=self.var2, command=lambda: toggle('Savings'))
        cb_checking.pack(side='left', padx=40)
        cb_savings.pack(side='left', padx=40)
        # Radio buttons (Withdraw vs. Deposit)
        self.frame_eight = Frame(self.window)
        self.radio_answer = IntVar()
        self.radio_answer.set(0)  # Default value
        self.radio_Withdraw = Radiobutton(self.frame_eight, text='Withdraw', font=("Times New Roman", 15),variable=self.radio_answer, value=1)
        self.radio_Deposit = Radiobutton(self.frame_eight, text='Deposit', font=("Times New Roman", 15),variable=self.radio_answer, value=2)
        self.radio_Withdraw.pack(side='left', padx=40)
        self.radio_Deposit.pack(side='left', padx=40)
        # Amount
        self.frame_nine = Frame(self.window)
        self.amount_label = Label(self.frame_nine, text='AMOUNT', font=("Times New Roman", 15))
        self.amount_entry = Entry(self.frame_nine, width=30)
        self.amount_label.pack(padx=10, side='left')
        self.amount_entry.pack(padx=10, side='left')
        # Final Result
        self.frame_ten = Frame(self.window)
        self.final_balance = Label(self.frame_ten, text=f'', font=("Times New Roman", 15))
        self.final_balance.pack(side='left', padx=30)
        # Enter and Exit Button
        self.frame_eleven = Frame(self.window)
        self.Enter_button = Button(self.frame_eleven, text='Enter', command=self.enter, font=("Times New Roman", 15))
        self.Exit_button = Button(self.frame_eleven, text='Exit', command=self.leave, font=("Times New Roman", 15))
        self.Enter_button.pack(side='left', padx=40, pady =20)
        self.Exit_button.pack(side='left', padx=40, pady =20)

    def search(self)->None:
        """
        This function is called when the search button is pushed on the GUI
        :return: If all the values are valid then it opens up the ATM and allows you access your bank account.
        """
        try:
            entered_pin = self.pin_entry.get()
            first_name = self.first_name_entry.get()
            last_name = self.last_name_entry.get()
            if len(entered_pin) != 4:
                raise ValueError
            with open('Banking_info.csv', "r") as csv_file:
                reader = csv.DictReader(csv_file)
                for row in reader:
                    if entered_pin == row['PIN'] and first_name == row['First Name'] and last_name == row['Last Name']:
                        self.welcome_label.config(text=f"Welcome! {first_name} {last_name}", fg="green")
                        self.action_label.config(text=f"What would like to do Next", fg="black")
                        self.frame_seven.pack()
                welcome = self.welcome_label.cget("text")
                if welcome == '':
                    raise NameError
        except ValueError:
            messagebox.showerror("Invalid Input", "Pin must only be numbers and 4 characters long")
            self.pin_entry.delete(0, END)
        except FileNotFoundError:
            self.welcome_label.config(text="Error: PIN file not found!", fg="red")
        except NameError:
            messagebox.showerror("Invalid Input", "Please enter your information again")
            self.first_name_entry.delete(0, END)
            self.last_name_entry.delete(0, END)
            self.pin_entry.delete(0, END)

    def enter(self)->None:
        """
        This method is called when all the values are valid from search
        :return: If all values are valid then it sends your values to the logic file where you will either deposit or withdraw money from a bank account.
        """
        try:
            # Retrieve user inputs
            entered_pin = self.pin_entry.get()
            first_name = self.first_name_entry.get()
            last_name = self.last_name_entry.get()
            status = self.radio_answer.get()  # Get radio button selection
            amount = self.amount_entry.get()

            # Check if the amount is valid
            if not amount.replace('.', '', 1).isdigit() or float(amount) <= 0:
                raise ValueError()

            amount = float(amount)  # Convert to float

            # Determine which account type was selected
            balance_type = ''
            if self.var1.get():  # Checking account selected
                balance_type = "Checking Balance"
            elif self.var2.get():  # Savings account selected
                balance_type = "Savings Balance"
            else:
                raise NameError()

            # Read the existing data from the CSV into memory
            rows = []
            with open('Banking_info.csv', "r", newline='', encoding='utf-8') as csv_file:
                reader = csv.DictReader(csv_file)
                for row in reader:
                    # Check if the current row matches the user
                    if entered_pin == row['PIN'] and first_name == row['First Name'] and last_name == row['Last Name']:
                        balance = float(row[balance_type])  # Get the current balance
                        if status == 1:  # Withdraw
                            new_balance = withdraw(balance, amount)
                        elif status == 2:  # Deposit
                            new_balance = deposit(balance, amount)
                        else:
                            raise TypeError("Invalid operation")

                        # Update the balance in the current row
                        row[balance_type] = str(new_balance)
                    # Add the row to the list (whether modified or not)
                    rows.append(row)

            # Write the updated data back to the CSV file
            with open('Banking_info.csv', "w", newline='', encoding='utf-8') as csv_file:
                fieldnames = ['First Name', 'Last Name', 'PIN', 'Checking Balance', 'Savings Balance']
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writeheader()  # Write the header
                writer.writerows(rows)  # Write all rows (modified or not)
                #sourc for updating csv file: https://stackoverflow.com/questions/11033590/change-specific-value-in-csv-file-via-python
            # Update the UI with the new balance
            self.final_balance.config(text=f'Your Balance is = {new_balance}')

            # Reset the form fields
            self.amount_entry.delete(0, END)
            self.var1.set(0)
            self.var2.set(0)
            self.radio_answer.set(0)
            self.frame_ten.pack()

        except ValueError:
            messagebox.showerror("Invalid Input", "Invalid amount entered.")
            self.amount_entry.delete(0, END)
        except NameError:
            messagebox.showerror("Error", "Please choose a bank account.")
        except TypeError:
            messagebox.showerror("Error", "Please select an action.")
        except LookupError:
            messagebox.showerror("Error", "User not found. Please try again.")
        except FileNotFoundError:
            messagebox.showerror("Error", "Banking information file not found!")
        #source for messageboxes: https://stackoverflow.com/questions/2963263/how-can-i-create-a-simple-message-box-in-python
    def leave(self)->None:
        """
        This function closes you out of the GUI
        :return: Ends the GUI
        """
        self.window.destroy()

