import gradio as gr
from collections import Counter
import re
def text_analyzer(text):
    text_clean = text.lower()
    text_clean = re.sub(r"[^\w\s]", "", text_clean)
    words = text_clean.split()
    char_count = len(text)
    word_count = len(words)
    most_common = Counter(words).most_common(1)
    if text == "":
        return "No words entered"
    elif most_common:
         common_word = most_common[0][0]
    else:
        common_word = "None"
    return f"Words:{word_count}\nCharacters:{char_count}\nMost common: {common_word}"
def clear():
    return "", ""
with gr.Blocks() as app:
    gr.Markdown("WORD ANALYZER")
    inputs = gr.Textbox(label="Enter Text")
    outputs = gr.Textbox(label="Result")
    btn = gr.Button("CHECK")
    btnc = gr.ClearButton(value="CLEAR", components=[inputs , outputs])

    btn.click(fn=text_analyzer, inputs=inputs, outputs=outputs)
   

app.launch()

