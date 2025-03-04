# UML Class Diagram (ASCII Representation)

```
  +--------------------+
  |   UserDatabase    |
  |------------------ |
  | - users{}         |
  | - passwords{}     |
  |------------------ |
  | + add_cashier()   |
  | + delete_cashier()|
  | + view_cashiers() |
  | + authenticate()  |
  +--------------------+
              │
              ▼
  +--------------------+
  |       User       |
  |------------------|
  | - username       |
  | - role           |
  |------------------|
  | + get_role()     |
  +--------------------+
   |          ▲
----          │
|     --------------------------------------
|     │                                    │
| +--------------------+        +--------------------+
| |      Cashier      |         |      Manager      |
| |------------------ |         |------------------ |
| | (inherits User)   |         | (inherits User)   |
| +--------------------+        +--------------------+
|
---------------------------------------------
            |                               |
            ▼  Uses                         ▼  Uses
  +-------------------▼         ▼-------------------+
  |     Inventory     |         |   SalesTracker    |
  |------------------ |         |------------------ |
  | - products{}      |         | - sales_history[] |
  |------------------ |         |------------------ |
  | + add_product()   |         | + record_sale()   |
  | + delete_product()|         | + view_sales_history() |
  | + update_stock()  |         | + get_total_revenue()  |
  | + view_inventory()|         +--------------------+
  +--------------------+                         ▲
              ▲                                  |
              │ Manages                          │ Tracks
              ▼                                  ▼
  +--------------------+         +--------------------+
  |      Product      |         |        Sale       |
  |------------------ |         |------------------ |
  | - name            |         | - product_name    |
  | - category        |         | - quantity        |
  | - price           |         | - total_price     |
  | - stock           |         | - cashier_name    |
  |------------------ |         | - timestamp       |
  | + update_stock()  |         |------------------ |
  +--------------------+        | + __str__()       |
                                +--------------------+
```

## Explanation of Relationships

- **Inheritance:** `Cashier` and `Manager` **inherit** from `User`.
- **Association (`has-a`) Relationships:**
  - `UserDatabase` **manages** multiple `User` objects.
  - `Inventory` **manages** multiple `Product` objects.
  - `SalesTracker` **manages** multiple `Sale` transactions.
  - `Sale` **tracks** `Product` details.
- **Dependency (`uses`) Relationships:**
  - `Cashier` and `Manager` **use** `Inventory` to update stock.
  - `Cashier` **uses** `SalesTracker` to record sales.
  - `SalesTracker` depends on `Sale` objects to track transactions.

# UML Sequence Diagrams (ASCII Representation)

## Login Sequence
```
     User          Menu          UserDatabase
      |             |                  |
      |  Login()    |                  |
      |------------>|                  |
      |             | Authenticate()   |
      |             |----------------->|
      |             | validate user    |
      |             |<-----------------|
      | display menu|     |            |
      |<------------|                  |
```

## Record Sale Sequence
```
     Cashier       Menu               Inventory       SalesTracker
      |             |                    |               |
      | RecordSale()|                    |               |
      |------------>| CheckStock()       |               |
      |             |------------------->|               |
      |             | Stock is available |               |
      |             |<-------------------|               |
      |             | RegisterSale()     |               |
      |             |----------------------------------->|
      |             | deduct stock       |               |
      |             |------------------->|               |
      | show sale   |                    |               |
      |<------------|                    |               |
```

## Add New Cashier (Manager Only)
```
     Manager        Menu           UserDatabase
      |              |                 |
      | AddCashier() |                 |
      |------------->| StoreUser()     |
      |              |---------------->|
      |              | confirmation    |
      |              |<----------------|
      |<-------------|                 |
```

## Update Inventory Sequence
```
     Cashier/Manager     Menu            Inventory
         |                |                 |
         | UpdateStock()  |                 |
         |--------------->| ModifyStock()   |
         |                |---------------->|
         |                | confirmation    |
         |<---------------|                 |
```