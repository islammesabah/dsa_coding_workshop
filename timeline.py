import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime, timedelta

# 1. Setup Data
# We define the sequence of tasks and breaks
schedule = [
    {"Task": "Coding & GenAI (Univ)", "Duration": 45, "Type": "Work"},
    {"Task": "Break", "Duration": 10, "Type": "Break"},
    {"Task": "Cursor IDE", "Duration": 75, "Type": "Work"},
    {"Task": "Break", "Duration": 10, "Type": "Break"},
    {"Task": "Coding Toolbox", "Duration": 15, "Type": "Work"},
    {"Task": "DSA Group", "Duration": 5, "Type": "Work"},
    {"Task": "Final Q&A", "Duration": 20, "Type": "Work"},
]

# 2. Calculate Timestamps
start_time = datetime.strptime("02:00", "%H:%M")
plot_data = []
current_time = start_time

for item in schedule:
    end_time = current_time + timedelta(minutes=item["Duration"])
    plot_data.append({
        "Task": item["Task"],
        "Start": current_time,
        "End": end_time,
        "Duration": item["Duration"],
        "Color": "#3498db" if item["Type"] == "Work" else "#e74c3c"
    })
    current_time = end_time

# 3. Create the Plot
fig, ax = plt.subplots(figsize=(10, 6))

for i, task in enumerate(reversed(plot_data)):
    # Calculate relative start and width in minutes
    rel_start = (task["Start"] - start_time).total_seconds() / 60
    ax.barh(i, task["Duration"], left=rel_start, 
            color=task["Color"], edgecolor='black')
    
    # Add duration label inside the bar
    ax.text(rel_start + task["Duration"]/2, i, 
            f'{task["Duration"]}m', va='center', ha='center', 
            color='white', fontweight='bold')

# Set y-tick labels
ax.set_yticks(range(len(plot_data)))
ax.set_yticklabels([task["Task"] for task in reversed(plot_data)])

# 4. Formatting
ax.set_xlabel("Time (Minutes from start)")
ax.set_title("Session Timeline", fontsize=14, pad=20)
ax.grid(axis='x', linestyle='--', alpha=0.6)

# Set X-axis ticks to show actual clock time
total_minutes = int((current_time - start_time).total_seconds() / 60)
ticks = list(range(0, total_minutes + 1, 30))
tick_labels = [(start_time + timedelta(minutes=t)).strftime("%H:%M") for t in ticks]
ax.set_xticks(ticks)
ax.set_xticklabels(tick_labels)

plt.tight_layout()
plt.savefig('session_timeline.png', dpi=300, bbox_inches='tight')
plt.close(fig)