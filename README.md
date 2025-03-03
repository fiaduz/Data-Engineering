# Data-Engineering
Top Weekend places to visit
Here's a **README.md** for your "Top Indian Places to Visit" project:  

---

## 🌍 Top Indian Places to Visit 🏕️

This Python project helps users find the best travel destinations in Indian cities based on **Google review ratings, time needed to visit, entrance fees, and popularity**.  

---

## 📌 Features  
✅ Load and clean the dataset  
✅ Rank travel places based on ratings, time, fee, and popularity  
✅ Normalize data for better ranking   
✅ Display top-ranked travel places  

---

## 📂 Dataset  
The dataset should be a CSV file with the following columns:  
- **City** → Name of the city  
- **Name** → Tourist attraction name  
- **Google review rating** → Average rating (out of 5)  
- **Time needed to visit in hrs** → Estimated visit duration  
- **Entrance Fee in INR** → Entry fee cost  
- **Number of Google reviews in lakhs** → Popularity based on review count  

Ensure the dataset file is named **"Top Indian Places to Visit.csv"** and located in the project folder.

---

## 🛠️ Installation & Setup  

### 1️⃣ Clone the Repository  
```sh
git clone https://github.com/yourusername/top-indian-places.git
cd top-indian-places
```

### 2️⃣ Install Dependencies  
```sh
pip install pandas
```

### 3️⃣ Run the Program  
```sh
python main.py
```

---

## 📊 How It Works  
1️⃣ The program **loads and cleans** the dataset.  
2️⃣ The user enters the name of a **city**.  
3️⃣ The algorithm **ranks places** using:  
   - **Ratings (40%)**  
   - **Time needed (30%)**  
   - **Entrance Fee (20%)**  
   - **Popularity (10%)**  
4️⃣ The **top-ranked places** are displayed.  

---

## 🔥 Example Usage  
```sh
Enter the city name: Jaipur
```
💡 **Output:**  
```
Top weekend travel places near Jaipur:
1. Amber Fort - ⭐ 4.7 | ⏳ 2 hrs | 💰 ₹50 | 🔥 2.1L reviews | 🏆 Score: 0.89
2. Hawa Mahal - ⭐ 4.6 | ⏳ 1.5 hrs | 💰 ₹20 | 🔥 1.8L reviews | 🏆 Score: 0.85
...
```

---

