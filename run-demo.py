from squad.demo_prepro import prepro
from basic.demo_cli import Demo
import json

demo = Demo()

def getAnswer(paragraph, question):
    print("CMG: prepro with paragraph and question {}".format(question))
    pq_prepro = prepro(paragraph, question)
    if len(pq_prepro['x'])>1000:
        return "[Error] Sorry, the number of words in paragraph cannot be more than 1000." 
    if len(pq_prepro['q'])>100:
        return "[Error] Sorry, the number of words in question cannot be more than 100."
    print("CMG: Preprocessed paragraph and question: x = {} q = {}".format(pq_prepro['x'], pq_prepro['q']));
    return demo.run(pq_prepro)

def submit(paragraph, question):
    answer = getAnswer(paragraph, question)
    print("\nANSWER:\n{}".format(answer))

if __name__ == "__main__":
    print("CMG: Running run-demo as main")
    file = open("/home/cgreivel/work/demo_input/paragraph", "r")
    paragraph = file.read()
    question = "How tall is Darko Milicic?"
    print("Submitting question {}".format(question))
    submit(paragraph, question)
