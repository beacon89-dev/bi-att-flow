from squad.demo_prepro import prepro
from basic.demo_cli import Demo
import json
import time

print("Starting to allocate demo at " + time.strftime("%H:%M:%S"))
demo = Demo()
print("Finished allocating demo at " + time.strftime("%H:%M:%S"))

def getAnswer(paragraph, question):
    print("CMG ({}): prepro".format(time.strftime("%H:%M:%S")))
    pq_prepro = prepro(paragraph, question)
    if len(pq_prepro['x'])>1000:
        return "[Error] Sorry, the number of words in paragraph cannot be more than 1000." 
    if len(pq_prepro['q'])>100:
        return "[Error] Sorry, the number of words in question cannot be more than 100."
    print("CMG ({}): Finished preprocessing paragraph and question".format(time.strftime("%H:%M:%S")));
    return demo.run(pq_prepro)

def submit(paragraph, question):
    answer = getAnswer(paragraph, question)
    print("\nANSWER ({}):\n{}".format(time.strftime("%H:%M:%S"), answer))

if __name__ == "__main__":
    print("CMG ({}): Running run-demo as main".format(time.strftime("%H:%M:%S")))

    filename = input("Enter path to file with text: ")
    file = open(filename, "r")
    paragraph = file.read()
    file.close()
    question = input("Enter your question ('done' to stop, 'new passage' for new text): ")
    while question != "done":
        if question == "new passage":
            filename = input("Enter path to file with text: ")
            file = open(filename, "r")
            paragraph = file.read()
            file.close()
            question = input("Enter your question ('done' to stop, 'new passage' for new text): ")

        print("({}) Submitting question {}".format(time.strftime("%H:%M:%S"), question))
        submit(paragraph, question)
        question = input("Enter your question ('done' to stop, 'new passage' for new text): ")
