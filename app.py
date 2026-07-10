import gradio as gr

from chatbot import Chatbot


def ask_question(file, question):

    if file is None:
        return "Please upload a PDF."

    return Chatbot.answer(file, question)


demo = gr.Interface(
    fn=ask_question,
    inputs=[
        gr.File(
            label="Upload PDF",
            file_types=[".pdf"],
            type="filepath"
        ),
        gr.Textbox(
            label="Ask a Question"
        )
    ],
    outputs=gr.Textbox(label="Answer"),
    title="SmartDoc Chatbot",
    description="Upload a PDF and ask questions about its contents."
)

if __name__ == "__main__":
    demo.launch()
