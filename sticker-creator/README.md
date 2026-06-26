# sticker-creator

תשתית Python לארכיטקטורת multi-agent ליצירת מדבקות לבית הספר.

## ארכיטקטורה

ההיררכיה היא עץ דו-שכבתי:

```
OrchestratorAgent
├── ContentAgent
└── VisualAgent
```

- **OrchestratorAgent** — הסוכן הראשי. מקבל את כל הפניות מהלקוח, מנתב כל בקשה
  לסוכן המשנה המתאים, ומנהל את זרימת העבודה הכללית.
- **ContentAgent** — אחראי על כתיבת טקסטים ועימוד למדבקות. מדווח ל-Orchestrator.
- **VisualAgent** — אחראי על יצירה וניהול תמונות גרפיות למדבקות. מדווח ל-Orchestrator.

כל הסוכנים יורשים מ-`BaseAgent` (ב-`core/base_agent.py`), שמספקת שם, לוגר, ו-stub
ל-`run()`. כרגע כל הפעולות הספציפיות (`route_request`, `handle_content`,
`handle_visuals`) הן stub-ים — המימוש המלא יתווסף בהמשך.

## מבנה התיקיות

```
sticker-creator/
├── agents/
│   ├── orchestrator_agent.py
│   ├── content_agent.py
│   └── visual_agent.py
├── core/
│   └── base_agent.py
├── utils/
│   └── logger.py
├── main.py
├── requirements.txt
└── README.md
```

## הרצה

```bash
cd sticker-creator
python3 main.py
```

הריצה מאתחלת את `OrchestratorAgent` ומריצה בקשת דוגמה. הלוגים שיוצגו ממחישים
את זרימת הנתונים: קבלת בקשה על ידי ה-Orchestrator → ניתוב → טיפול ע"י
ContentAgent/VisualAgent → דיווח חזרה.
