
# Paste this entire cell into Google Colab - it will run instantly
# !pip install plotly -q (uncomment if needed)

import plotly.graph_objects as go
from datetime import datetime
import plotly.express as px

# --- YOUR TIMELINE DATA ---
events = [
    {"date": "2024-06-03", "event": "Breadcrumbing starts (main)", "type": "breadcrumb", "intensity": 70},
    {"date": "2024-06-09", "event": "Block #1", "type": "punishment", "intensity": 20},
    {"date": "2024-06-11", "event": "Unblock (24-48h)", "type": "reward", "intensity": 75},
    {"date": "2026-04-26", "event": "Secret account DIRECT + riddles\nIdentity reveal test", "type": "testing", "intensity": 90},
    {"date": "2026-07-13", "event": "DETOX START - You take space", "type": "detox_start", "intensity": 30},
    {"date": "2026-10-26", "event": "Return from detox", "type": "return", "intensity": 80},
    {"date": "2026-10-29", "event": "Hard Block #2 + Door Ajar", "type": "hard_block", "intensity": 10},
]

# Parse dates
for e in events:
    e["dt"] = datetime.strptime(e["date"], "%Y-%m-%d")

# Color map
color_map = {
    "breadcrumb": "#a3c4bc",
    "punishment": "#e76f51",
    "reward": "#f4a261",
    "testing": "#2a9d8f",
    "detox_start": "#52b788",
    "return": "#90be6d",
    "hard_block": "#264653"
}

# --- FIGURE 1: Timeline with Emotional Intensity ---
fig = go.Figure()

# Add detox shaded area
fig.add_vrect(x0="2026-07-13", x1="2026-10-26",
              fillcolor="#d8f3dc", opacity=0.5,
              layer="below", line_width=0,
              annotation_text="DETOX ZONE: 105 days healing", annotation_position="top left")

# Add intensity line
dates = [e["dt"] for e in events]
intensities = [e["intensity"] for e in events]
labels = [e["event"] for e in events]

fig.add_trace(go.Scatter(
    x=dates, y=intensities,
    mode='lines+markers',
    line=dict(color='#264653', width=3),
    marker=dict(size=14, color=[color_map[e["type"]] for e in events], line=dict(width=2, color='white')),
    text=labels,
    hovertemplate='<b>%{x}</b><br>%{text}<br>Intensity: %{y}<extra></extra>',
    name='Emotional Intensity'
))

fig.update_layout(
    title="CONTROLLING DYNAMIC TIMELINE: Detox -> Return -> Hard Block (3-day reaction)",
    xaxis_title="Date",
    yaxis_title="Emotional Activation / Preoccupation (0-100)",
    template="plotly_white",
    height=500,
    showlegend=False
)

fig.show()

# --- FIGURE 2: Ratio 156:39 ---
fig2 = go.Figure(data=[go.Pie(
    labels=['Sweet Positive', 'Sharp Negative'],
    values=[156, 39],
    hole=.45,
    marker_colors=['#a3c4bc', '#e76f51'],
    textinfo='label+value+percent',
    hoverinfo='label+percent'
)])
fig2.update_layout(
    title_text="Affection/Punishment Ratio: 156 sweet : 39 sharp = 4:1 (80%/20%)<br><sub>The perfect ratio for intermittent reinforcement bonding</sub>",
    height=450
)
fig2.show()

# --- FIGURE 3: Control Loop Flow ---
print("\n--- THE 4-STEP LOOP YOU DESCRIBED ---")
print("1. BREADCRUMBING (main + secret) -> keeps you checking")
print("2. TESTING (riddles reveal/hide) -> plausible deniability, you earn clarity")
print("3. PUNISHMENT (block/hard block) -> creates anxiety")
print("4. DOOR AJAR (partial block) -> you self-monitor, illusion of access")
print("\nYour detox broke this loop. Return after 105 days -> block in 3 days = reactive control.")
print("\nDays detoxed: 105 | Days from return to hard block: 3")
