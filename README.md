# TMPS  
**University Course:** Software Design Techniques and Mechanisms  

## [Lab0: Applying SOLID Principles](https://github.com/LiviuTofan/TMPS/tree/main/src/Lab0)  

### Objective  
Implement two SOLID principles in a simple system to demonstrate their practical application.

### Description  
A system was created where users can log in, and upon login, the system sends notifications via multiple channels (Email, SMS, Push Notification).  

### Implementation  
- **SRP (Single Responsibility Principle):** Responsibilities for authentication and notification sending were separated into distinct classes.  
- **OCP (Open/Closed Principle):** The system supports adding new notification methods (e.g., Push Notifications) without modifying existing code.  

This approach resulted in a modular and extensible system design.

---

## [Lab1: Creational Design Patterns](https://github.com/LiviuTofan/TMPS/tree/main/src/Lab1)

### Objective  
Get familiar with Creational Design Patterns (CDPs) and implement at least three patterns in a specific domain.  

### Description  
The domain chosen was a pizza ordering system. Several CDPs were implemented to manage pizza creation and customization.  

### Implementation  
1. **Singleton Pattern:** Ensures only one oven instance exists, simplifying temperature and baking management.  
2. **Factory Method Pattern:** Allows for creating various pizza types (e.g., Margherita, Pepperoni) based on requested types, making it easy to extend with new types.  
3. **Prototype Pattern:** Enables cloning of existing pizzas to create modified versions without altering the original.  

These patterns made the system flexible, reusable, and easy to extend.

---

## [Lab2: Structural Design Patterns](https://github.com/LiviuTofan/TMPS/tree/main/src/Lab2)

### Objective  
Understand and apply at least three Structural Design Patterns in a chosen domain.  

### Description  
The pizza ordering system was further enhanced by incorporating Structural Design Patterns to improve modularity and scalability.  

### Implementation  
1. **Facade Pattern:** Simplified the interface for ordering pizzas through an `OrderFacade` class, hiding complexities like price calculations and preparation steps.  
2. **Adapter Pattern:** Enabled compatibility with an external payment service through a `PaymentAdapter`, facilitating currency conversion.  
3. **Composite Pattern:** Managed pizza ingredients by grouping them into hierarchical structures, allowing uniform treatment of individual and composite ingredients.  
4. **Proxy Pattern:** Added control over oven access using an `OvenProxy` class, ensuring safety with lock and unlock mechanisms.  

By applying these patterns, the system became more structured and aligned with real-world requirements. The resulting project is modular, maintainable, and ready for deployment in a pizza chain like Andy's Pizza.  
