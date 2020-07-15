# Define four Python functions named run, swing, slide, and hide_and_seek. Each 
# function should take varying number of children's names as the argument.
def run(*kids):
    for kid in kids:
        print(f'{kid}, why you runnin?!?!?')

def swing(*kids):
    for kid in kids:
        print(f'{kid} get off dat swing, its a death trap!!!')

def slide(*kids):
    for kid in kids:
        print(f'{kid} burned your butt on dat slide, eh?')

def hide_and_seek(*kids):
    for kid in kids:
        print(f'{kid} did you find the other H kids that are hiding?')

run("Joe", "Jenna", "Pam", "Sam", "Andrea", "Will")
swing("Marybeth", "Ariel", "Kevin", "Courtney")
slide("Mike", "Jack", "Jennifer", "Earl",)
hide_and_seek("Henry", "Heather", "Hayley", "Hugh")
