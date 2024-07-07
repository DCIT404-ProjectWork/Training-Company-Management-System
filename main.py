import tkinter as tk
from tkinter import messagebox
from db_connection import get_connection
import oracledb
import shutil
import os

import tkinter as tk
from tkinter import messagebox, simpledialog

# Establish a database connection
def connect_to_oracle():
    try:
        conn_str = 'system/admin@localhost:1521/xepdb1'
        connection = oracledb.connect(conn_str)
        return connection
    except oracledb.Error as error:
        messagebox.showerror("Database Error", f"Error connecting to Oracle database: {error}")
        return None
    

class TrainingCompanyUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Training Company Management System")
        self.geometry("800x800")

        self.create_widgets()

        # super().__init__()
        # self.title("Training Company Management")
        # self.geometry("600x400")
        
        # Create database connection
        self.connection = connect_to_oracle()
        if not self.connection:
            self.destroy()
            return

        # Create UI elements
        # self.create_insert_form()
        # self.create_retrieve_form()
        # self.create_update_form()
        # self.create_delete_form()
        # self.create_backup_form()
    def create_widgets(self):
        # Delegate registration fields
        tk.Label(self, text="Delegate No").grid(row=0, column=0, padx=10, pady=10)
        self.delegate_no = tk.Entry(self)
        self.delegate_no.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(self, text="Delegate First Name").grid(row=1, column=0, padx=10, pady=10)
        self.delegate_first_name = tk.Entry(self)
        self.delegate_first_name.grid(row=1, column=1, padx=10, pady=10)

        tk.Label(self, text="Delegate Last Name").grid(row=2, column=0, padx=10, pady=10)
        self.delegate_last_name = tk.Entry(self)
        self.delegate_last_name.grid(row=2, column=1, padx=10, pady=10)

        tk.Label(self, text="Delegate Title:").grid(row=3, column=0, padx=10, pady=10)
        self.delegateTitle = tk.Entry(self)
        self.delegateTitle.grid(row=3, column=1, padx=10, pady=10)

        tk.Label(self, text="Street:").grid(row=4, column=0, padx=10, pady=10)
        self.delegateStreet = tk.Entry(self)
        self.delegateStreet.grid(row=4, column=1, padx=10, pady=10)

        tk.Label(self, text="City:").grid(row=5, column=0, padx=10, pady=10)
        self.delegateCity = tk.Entry(self)
        self.delegateCity.grid(row=5, column=1, padx=10, pady=10)

        tk.Label(self, text="State:").grid(row=6, column=0, padx=10, pady=10)
        self.delegateState = tk.Entry(self)
        self.delegateState.grid(row=6, column=1, padx=10, pady=10)

        tk.Label(self, text="Zip Code:").grid(row=7, column=0, padx=10, pady=10)
        self.delegateZipCode = tk.Entry(self)
        self.delegateZipCode.grid(row=7, column=1, padx=10, pady=10)

        tk.Label(self, text="Tel No:").grid(row=8, column=0, padx=10, pady=10)
        self.attTelNo = tk.Entry(self)
        self.attTelNo.grid(row=8, column=1, padx=10, pady=10)

        tk.Label(self, text="Fax No:").grid(row=9, column=0, padx=10, pady=10)
        self.attFaxNo = tk.Entry(self)
        self.attFaxNo.grid(row=9, column=1, padx=10, pady=10)

        tk.Label(self, text="Email Address:").grid(row=10, column=0, padx=10, pady=10)
        self.attEmailAddress = tk.Entry(self)
        self.attEmailAddress.grid(row=10, column=1, padx=10, pady=10)

        tk.Label(self, text="Client No:").grid(row=11, column=0, padx=10, pady=10)
        self.clientNo = tk.Entry(self)
        self.clientNo.grid(row=11, column=1, padx=10, pady=10)

        # Buttons
        self.insert_button = tk.Button(self, text="Insert Record", command=self.insert_record)
        self.insert_button.grid(row=12, column=0, padx=10, pady=10)

        self.retrieve_button = tk.Button(self, text="Retrieve Record", command=self.retrieve_record)
        self.retrieve_button.grid(row=12, column=1, padx=10, pady=10)

        self.update_button = tk.Button(self, text="Update Record", command=self.update_record)
        self.update_button.grid(row=13, column=0, padx=10, pady=10)

        self.delete_button = tk.Button(self, text="Delete Record", command=self.delete_record)
        self.delete_button.grid(row=13, column=1, padx=10, pady=10)

        self.backup_button = tk.Button(self, text="Backup", command=self.backup_database)
        self.backup_button.grid(row=14, column=0, columnspan=2, padx=10, pady=10)


    # def create_backup_form(self):
    #     # Backup Form
    #     backup_frame = tk.LabelFrame(self.root, text="Backup Database")
    #     backup_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    #     # Entry fields
    #     tk.Label(backup_frame, text="Backup Directory:").grid(row=0, column=0, sticky=tk.E)
    #     self.backup_dir = tk.Entry(backup_frame)
    #     self.backup_dir.grid(row=0, column=1)

    #     tk.Label(backup_frame, text="Backup File Name:").grid(row=1, column=0, sticky=tk.E)
    #     self.backup_file = tk.Entry(backup_frame)
    #     self.backup_file.grid(row=1, column=1)

    #     # Backup Button
    #     backup_btn = tk.Button(backup_frame, text="Backup", command=self.backup_database)
    #     backup_btn.grid(row=2, columnspan=2, pady=10)

    def insert_record(self):
        try:
            delegateNo = int(self.delegate_no.get())
            delegateTitle = self.delegateTitle.get()
            delegateFName = self.delegate_first_name.get()
            delegateLName = self.delegate_last_name.get()
            delegateStreet = self.delegateStreet.get()
            delegateCity = self.delegateCity.get()
            delegateState = self.delegateState.get()
            delegateZipCode = self.delegateZipCode.get()
            attTelNo = self.attTelNo.get()
            attFaxNo = self.attFaxNo.get()
            attEmailAddress = self.attEmailAddress.get()
            clientNo = int(self.clientNo.get())

            cursor = self.connection.cursor()
            cursor.callproc("insert_delegate", [delegateNo, delegateTitle, delegateFName, delegateLName, delegateStreet, delegateCity, delegateState, delegateZipCode, attTelNo, attFaxNo, attEmailAddress, clientNo])
            cursor.close()
            messagebox.showinfo("Success", "Record inserted successfully.")
        except oracledb.Error as error:
            messagebox.showerror("Database Error", f"Error inserting record: {error}")

    def retrieve_record(self):
        delegate_no = self.delegate_no.get()

        if not delegate_no:
            messagebox.showerror("Error", "Delegate No is required!")
            return

        try:
            connection = get_connection()
            cursor = connection.cursor()

            # Call the PL/SQL stored procedure
            p_first_name = cursor.var(oracledb.STRING)
            p_last_name = cursor.var(oracledb.STRING)
            p_success = cursor.var(oracledb.STRING)
            p_error_msg = cursor.var(oracledb.STRING)

            cursor.callproc('retrieve_delegate', [delegate_no, p_first_name, p_last_name, p_success, p_error_msg])

            if p_success.getvalue() == 'Success':
                self.delegate_first_name.delete(0, tk.END)
                self.delegate_first_name.insert(0, p_first_name.getvalue())

                self.delegate_last_name.delete(0, tk.END)
                self.delegate_last_name.insert(0, p_last_name.getvalue())
            else:
                messagebox.showerror("Error", f"Error retrieving delegate: {p_error_msg.getvalue()}")

            cursor.close()
            connection.close()

        except oracledb.DatabaseError as e:
            messagebox.showerror("Database Error", str(e))

    def update_record(self):
        try:
            delegateNo = int(self.delegate_no.get())
            delegateTitle = self.delegateTitle.get()
            delegateFName = self.delegate_first_name.get()
            delegateLName = self.delegate_last_name.get()
            delegateStreet = self.delegateStreet.get()
            delegateCity = self.delegateCity.get()
            delegateState = self.delegateState.get()
            delegateZipCode = self.delegateZipCode.get()
            attTelNo = self.attTelNo.get()
            attFaxNo = self.attFaxNo.get()
            attEmailAddress = self.attEmailAddress.get()
            clientNo = int(self.clientNo.get())

            cursor = self.connection.cursor()
            cursor.callproc("update_delegate", [delegateNo, delegateTitle, delegateFName, delegateLName, delegateStreet, delegateCity, delegateState, delegateZipCode, attTelNo, attFaxNo, attEmailAddress, clientNo])
            cursor.close()
            messagebox.showinfo("Success", "Record updated successfully.")
        except oracledb.Error as error:
            messagebox.showerror("Database Error", f"Error updating record: {error}")

    def delete_record(self):
        delegate_no = self.delegate_no.get()

        if not delegate_no:
            messagebox.showerror("Error", "Delegate No is required!")
            return
        
        try:
            delegateNo = int(self.delegate_no.get())
            cursor = self.connection.cursor()
            cursor.callproc("delete_delegate", [delegateNo])
            cursor.close()
            messagebox.showinfo("Success", "Record deleted successfully.")
        except oracledb.Error as error:
            messagebox.showerror("Database Error", f"Error deleting record: {error}")

    def backup_database(self):
        try:
            backup_dir = self.backup_dir.get()
            backup_file = self.backup_file.get()
            cursor = self.connection.cursor()
            cursor.callproc("backup_database", [backup_dir, backup_file])
            cursor.close()
            messagebox.showinfo("Success", "Database backup created successfully.")
        except oracledb.Error as error:
            messagebox.showerror("Database Error", f"Error backing up database: {error}")

# Main code to run the user interface
if __name__ == "__main__":
    # root = tk.Tk()
    app = TrainingCompanyUI()
    app.mainloop()

# Create a class for the user interface
# class TrainingCompanyUI:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Training Company Management System")

#         # Create database connection
#         self.connection = connect_to_oracle()
#         if not self.connection:
#             self.root.destroy()
#             return

#         # Create UI elements
#         self.create_widgets()

#     def create_widgets(self):
#         # Insert Record Button
#         insert_btn = tk.Button(self.root, text="Insert Record", command=self.insert_record)
#         insert_btn.pack(pady=10)

#         # Retrieve Record Button
#         retrieve_btn = tk.Button(self.root, text="Retrieve Record", command=self.retrieve_record)
#         retrieve_btn.pack(pady=10)

#         # Update Record Button
#         update_btn = tk.Button(self.root, text="Update Record", command=self.update_record)
#         update_btn.pack(pady=10)

#         # Delete Record Button
#         delete_btn = tk.Button(self.root, text="Delete Record", command=self.delete_record)
#         delete_btn.pack(pady=10)

#         # Backup Button
#         backup_btn = tk.Button(self.root, text="Backup Database", command=self.backup_database)
#         backup_btn.pack(pady=10)

#     def insert_record(self):
#         try:
#             delegateNo = simpledialog.askinteger("Insert Record", "Enter Delegate No:")
#             delegateTitle = simpledialog.askstring("Insert Record", "Enter Delegate Title:")
#             delegateFName = simpledialog.askstring("Insert Record", "Enter Delegate First Name:")
#             delegateLName = simpledialog.askstring("Insert Record", "Enter Delegate Last Name:")
#             delegateStreet = simpledialog.askstring("Insert Record", "Enter Delegate Street:")
#             delegateCity = simpledialog.askstring("Insert Record", "Enter Delegate City:")
#             delegateState = simpledialog.askstring("Insert Record", "Enter Delegate State:")
#             delegateZipCode = simpledialog.askstring("Insert Record", "Enter Delegate Zip Code:")
#             attTelNo = simpledialog.askstring("Insert Record", "Enter Delegate Tel No:")
#             attFaxNo = simpledialog.askstring("Insert Record", "Enter Delegate Fax No:")
#             attEmailAddress = simpledialog.askstring("Insert Record", "Enter Delegate Email Address:")
#             clientNo = simpledialog.askinteger("Insert Record", "Enter Client No:")

#             cursor = self.connection.cursor()
#             cursor.callproc("insert_delegate", [delegateNo, delegateTitle, delegateFName, delegateLName, delegateStreet, delegateCity, delegateState, delegateZipCode, attTelNo, attFaxNo, attEmailAddress, clientNo])
#             cursor.close()
#             messagebox.showinfo("Success", "Record inserted successfully.")
#         except oracledb.Error as error:
#             messagebox.showerror("Database Error", f"Error inserting record: {error}")

#     def retrieve_record(self):
#         try:
#             delegateNo = simpledialog.askinteger("Retrieve Record", "Enter Delegate No:")
#             cursor = self.connection.cursor()
#             p_cursor = cursor.var(oracledb.CURSOR)
#             cursor.callproc("retrieve_delegate", [delegateNo, p_cursor])
#             rows = p_cursor.getvalue().fetchall()
#             cursor.close()

#             if rows:
#                 for row in rows:
#                     print(row)
#                     messagebox.showinfo("Record Retrieved", str(row))
#             else:
#                 messagebox.showwarning("No Data", "No record found for the provided Delegate No.")
#         except oracledb.Error as error:
#             messagebox.showerror("Database Error", f"Error retrieving record: {error}")

#     def update_record(self):
#         try:
#             delegateNo = simpledialog.askinteger("Update Record", "Enter Delegate No:")
#             delegateTitle = simpledialog.askstring("Update Record", "Enter Delegate Title:")
#             delegateFName = simpledialog.askstring("Update Record", "Enter Delegate First Name:")
#             delegateLName = simpledialog.askstring("Update Record", "Enter Delegate Last Name:")
#             delegateStreet = simpledialog.askstring("Update Record", "Enter Delegate Street:")
#             delegateCity = simpledialog.askstring("Update Record", "Enter Delegate City:")
#             delegateState = simpledialog.askstring("Update Record", "Enter Delegate State:")
#             delegateZipCode = simpledialog.askstring("Update Record", "Enter Delegate Zip Code:")
#             attTelNo = simpledialog.askstring("Update Record", "Enter Delegate Tel No:")
#             attFaxNo = simpledialog.askstring("Update Record", "Enter Delegate Fax No:")
#             attEmailAddress = simpledialog.askstring("Update Record", "Enter Delegate Email Address:")
#             clientNo = simpledialog.askinteger("Update Record", "Enter Client No:")

#             cursor = self.connection.cursor()
#             cursor.callproc("update_delegate", [delegateNo, delegateTitle, delegateFName, delegateLName, delegateStreet, delegateCity, delegateState, delegateZipCode, attTelNo, attFaxNo, attEmailAddress, clientNo])
#             cursor.close()
#             messagebox.showinfo("Success", "Record updated successfully.")
#         except oracledb.Error as error:
#             messagebox.showerror("Database Error", f"Error updating record: {error}")

#     def delete_record(self):
#         try:
#             delegateNo = simpledialog.askinteger("Delete Record", "Enter Delegate No:")
#             cursor = self.connection.cursor()
#             cursor.callproc("delete_delegate", [delegateNo])
#             cursor.close()
#             messagebox.showinfo("Success", "Record deleted successfully.")
#         except oracledb.Error as error:
#             messagebox.showerror("Database Error", f"Error deleting record: {error}")

#     def backup_database(self):
#         try:
#             backup_dir = simpledialog.askstring("Backup Database", "Enter Backup Directory:")
#             backup_file = simpledialog.askstring("Backup Database", "Enter Backup File Name:")
#             cursor = self.connection.cursor()
#             cursor.callproc("backup_database", [backup_dir, backup_file])
#             cursor.close()
#             messagebox.showinfo("Success", "Database backup created successfully.")
#         except oracledb.Error as error:
#             messagebox.showerror("Database Error", f"Error backing up database: {error}")

# # Main code to run the user interface
# if __name__ == "__main__":
#     root = tk.Tk()
#     app = TrainingCompanyUI(root)
#     root.mainloop()
