# Video Game Store Cashier System

## Table of Contents
- [1. User Roles](#1-user-roles)
- [2. Products & Inventory Management](#2-products--inventory-management)
- [3. Sales Tracking](#3-sales-tracking)
- [4. Reports & Data](#4-reports--data)
- [5. User Interface (Command-Line Menu)](#5-user-interface-command-line-menu)
- [6. Login & Logout Behavior](#6-login--logout-behavior)
- [7. Future Extensions (Not Implemented Now)](#7-future-extensions-not-implemented-now)

---

## 1. User Roles

There are two types of users in the system: **cashiers** and **managers**.

### Cashier (Regular User)
- Can **log in** to the system.
- Can **record a sale**, which:
  - Deducts the sold quantity from stock.
  - Logs the sale under their name.
- Can **update inventory** (e.g., when new stock arrives).
- Can **view stock levels**.
- Can **view their own sales history**.
- Can **search for a product** by name to view its **stock, category, and price**.
- Can **log out**, returning to the login screen.

### Manager (Admin User)
- Has **all the same abilities as a cashier**.
- Additionally, can:
  - **Create new cashiers** in the system.
  - **Delete cashiers** if they leave the company.
  - **View all sales history** (for every cashier).
  - **View total store revenue**.
  - **See a list of all registered cashiers**.
  - **Add new products** to the store inventory.
  - **Delete products** from the store inventory.
- Can **log out**, returning to the login screen.

---

## 2. Products & Inventory Management

- The store sells **video games, consoles, and accessories**.
- Each product has:
  - A **name** (e.g., "PlayStation 5").
  - A **category** (Game, Console, or Accessory).
  - A **price** (must be **positive**).
  - A **quantity in stock** (cannot be negative).
- Cashiers and managers can **update inventory** when new stock arrives.
- Users **cannot sell more than what is in stock**.
- Managers can **add new products** to the inventory.
- Managers can **delete products** from the inventory.

---

## 3. Sales Tracking

- A cashier **records a sale** by:
  - Selecting a product.
  - Entering the quantity sold.
  - The system **calculates the total price**.
  - The **stock is updated automatically**.
  - The sale is **logged under the cashier’s name**.
- Each sale is stored in **sales history**.

---

## 4. Reports & Data

- Cashiers can **view their own sales history**.
- Managers can **view sales history for all cashiers**.
- Managers can **see a list of all registered cashiers**.
- The system **tracks total revenue** earned from all sales.
- Users can **search for a product** by entering its name and viewing its **full details** (category, price, and stock levels).

---

## 5. User Interface (Command-Line Menu)

The system runs on a **simple text-based menu**.

### Login Screen
1. **Log in as a Cashier**  
2. **Log in as a Manager**  
3. **Exit the Program**  

### Cashier Menu
1. **Record a Sale**  
2. **Update Inventory**  
3. **View Stock**  
4. **Search for a Product**  
5. **View My Sales History**  
6. **Log Out (Returns to Login Screen)**  

### Manager Menu (Has extra options)
1. **Record a Sale**  
2. **Update Inventory**  
3. **View Stock**  
4. **Search for a Product**  
5. **View My Sales History**  
6. **View All Sales History**  
7. **Create New Cashier**  
8. **Delete Cashier**  
9. **View All Cashiers**  
10. **Add a New Product**  
11. **Delete a Product**  
12. **Log Out (Returns to Login Screen)**  

---

## 6. Login & Logout Behavior

- When a user **logs out**, they return to the **login screen**.
- Users can **log in as a different cashier or manager** without restarting the program.
- Users can **exit the program** from the login screen.