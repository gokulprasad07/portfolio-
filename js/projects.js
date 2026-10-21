/* ===== EDIT THIS FILE to update your portfolio content =====
   A link is shown only when its path/URL is filled in. Empty "" = "not added yet". */
const PROFILE = {
  email: "mgp647gokul@gmail.com",
  github: "https://github.com/gokulprasad07",
  linkedin: "https://www.linkedin.com/in/gokulprasadm",
  resume: "assets/documents/Gokul_Prasad_Resume.pdf"
};

const SKILLS = {
  "Programming": ["Python", "C", "Java"],
  "Frontend": ["HTML", "CSS", "JavaScript (learning)"],
  "AI/ML & Data Science": ["Machine Learning", "Regression", "Classification", "Clustering", "Pandas", "NumPy", "Matplotlib", "Seaborn", "Plotly", "Scikit-learn", "Jupyter Notebook"],
  "Analytics & Databases": ["Excel", "Power BI", "SQL", "Data Visualization"],
  "Developer Tools": ["Git", "GitHub", "VS Code", "Google AI Studio", "API Integration"],
  "Creative": ["Graphic Design", "Poster Design", "Logo Design", "Branding", "Video Editing", "Motion Graphics", "Reels Editing"]
};

const LINK_TYPES = ["Source Code", "Live Demo", "Documentation", "Dataset", "Notebook", "Report"];
const T = "assets/images/tourist-";

const PROJECTS = [
  { id: "tourist", title: "Tourist Behaviour & Travel Analysis", category: "AI/ML & Data", status: "Completed, 2026",
    stack: ["Python", "Pandas", "NumPy", "Matplotlib", "Seaborn", "Plotly", "Scikit-learn"],
    summary: "End-to-end analysis of 1,508 tourist records, with K-Means segmentation and a Random Forest satisfaction model.",
    problem: "Understand who travels, where they go, how they travel, what they spend and how satisfied they are.",
    details: [
      ["Dataset", "1,508 rows, 13 columns: Age, Gender, Country, Travel_Frequency, Travel_Type, Destination, Trip_Duration, Accommodation_Type, Transportation, Activities, Total_Spending, Satisfaction_Rating."],
      ["Cleaning", "Missing values in Gender, Transportation and Activities (6 each) filled with the mode; 8 duplicate rows removed, leaving 1,500 rows."],
      ["Exploratory analysis", "Age, gender and origin country; travel frequency and type; transport and activities; destination summaries; spending and trip duration; satisfaction; correlation heatmap; travel type vs transport."],
      ["Clustering", "K-Means with 4 clusters on standardized Age, Trip Duration, Spending and Satisfaction, after an elbow check for k = 2 to 6."],
      ["Classification", "Random Forest (200 trees) in a scikit-learn pipeline predicting satisfaction category (Low 1-2, Medium 3, High 4-5) from 11 features, on a 300-row test set."],
      ["Results (from the notebook)", "Accuracy 56.67%. Per class, High: precision 0.60 / recall 0.74; Medium: 0.49 / 0.38; Low: 0.00 / 0.00 (only 9 test samples). Macro F1 is 0.36, so the model mainly separates High from Medium and does not detect Low."],
      ["Insights printed by the notebook", "Most visited destination: Rajasthan. Highest average satisfaction: Kerala. Highest-spending travel type: Family. Most used transport: Train."],
      ["Not yet added", "The dataset CSV was not provided, so no dataset link is shown. No report or dashboard exists yet."]],
    images: [[T+"age-distribution.png", "Age distribution of tourists"], [T+"top-origin-countries.png", "Top tourist origin countries"],
      [T+"correlation-heatmap.png", "Correlation between key metrics"], [T+"kmeans-elbow.png", "K-Means elbow check"], [T+"confusion-matrix.png", "Satisfaction model confusion matrix"]],
    links: { "Notebook": "projects/tourist-analytics/Tourist_Behaviour_and_Travel_Analysis_Colab_FINAL.ipynb" } },
  { id: "house", title: "House Price Prediction", category: "AI/ML & Data", status: "Flask app source (data not included)",
    stack: ["Python", "Flask", "Pandas", "Scikit-learn", "Linear Regression"],
    summary: "Flask web app that trains Linear Regression on startup and predicts a price from user input.",
    problem: "Estimate a house price from its area, bedrooms and bathrooms.",
    details: [
      ["Features and target", "Features: area, bedrooms, bathrooms. Target: price, read from house_data.csv."],
      ["Workflow", "The model is fitted on the full dataset at startup. A form posts three integers to /predict, which returns the price in rupees on the page."],
      ["Evaluation", "app.py has no train/test split or metrics, so none are reported."],
      ["Not yet added", "house_data.csv and templates/index.html were not provided, so the app can't run from this folder yet. No live demo."]],
    links: { "Source Code": "projects/house-price-prediction/app.py" } },
  { id: "translator", title: "Python Translator Tool", category: "Python Utilities", status: "Desktop app (Tkinter)",
    stack: ["Python", "Tkinter", "googletrans"],
    summary: "Tkinter language translator with Translate and Clear controls, using the googletrans library.",
    problem: "Translate typed text between languages from a simple desktop window.",
    details: [["Implementation", "TranslatorApp class in translator_calculator_bill.py, opened from a master menu. It needs googletrans (pip install googletrans==3.1.0a0) and Pillow, and shows a warning if they are missing."], ["Screenshots", "[Add a screenshot of the window]"]],
    links: { "Source Code": "projects/python-utilities/translator_calculator_bill.py" } },
  { id: "receipt", title: "Billing Software (Bill Receipt Generator)", category: "Python Utilities", status: "Desktop app (Tkinter)",
    stack: ["Python", "Tkinter"],
    summary: "Billing system with customer details, item groups, tax totals and a bill area.",
    problem: "Calculate and print customer bills without manual arithmetic.",
    details: [["Functionality", "Customer name, phone and bill number with a bill search. Items are grouped into Medical, Grocery and Cold Drinks, with per-category totals and tax, and a Total button that fills the bill area."], ["Samples", "[Add a screenshot using dummy customer data only]"]],
    links: { "Source Code": "projects/python-utilities/translator_calculator_bill.py" } },
  { id: "calc", title: "Calculator Program", category: "Python Utilities", status: "Desktop app (Tkinter)",
    stack: ["Python", "Tkinter"], summary: "Tkinter calculator launched from the same menu as the translator and billing apps.",
    problem: "A basic desktop calculator.", details: [["Implementation", "CalculatorApp class in translator_calculator_bill.py."], ["Screenshots", "[Add a screenshot]"]],
    links: { "Source Code": "projects/python-utilities/translator_calculator_bill.py" } },
  { id: "piano", title: "Piano Simulator", category: "Python Utilities", status: "Desktop app (Tkinter)",
    stack: ["Python", "Tkinter", "Pillow", "playsound"],
    summary: "23-key on-screen piano, bundled with a paint program and name generator in one launcher.",
    problem: "Play piano notes from an on-screen keyboard.",
    details: [["Implementation", "PianoApp builds alternating black and white key buttons; each key plays Piano<N>.mp3 via playsound."], ["Limitation", "The MP3 files were not provided, so sound is untested. In all_intership_program.py the sound call is disabled and only prints a message."],
      ["Bundled apps", "Paint (pen, brush, colour picker, eraser, size slider) and a Name Generator using the names library."]],
    links: { "Source Code": "projects/python-utilities/paint_piano_name_genarator.py" } },
  { id: "portfolio", title: "Personal Portfolio Website", category: "Web", status: "This site",
    stack: ["HTML", "CSS", "JavaScript"], summary: "This portfolio, written in vanilla HTML, CSS and JavaScript with no frameworks.",
    problem: "Present design and development work in one maintainable place.",
    details: [["Source and live URL", "[Add after publishing to GitHub Pages or Netlify]"]], links: {} }
];

/* Creative items: { title, category, type: "image"|"video", src, thumb, description } */
const CREATIVE = [];
const CREATIVE_CATEGORIES = ["Logo Design", "Brand Identity", "Poster Design", "Social Media", "Video Editing", "Motion Graphics", "Reels"];
