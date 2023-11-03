from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"

# ------------------------GENERATE NEW FLASHES----------------------------------------
random_word_meaning_pair={}
french_words_list={}
try:
    words_to_learn_df=pandas.read_csv('words_to_learn.csv')
except FileNotFoundError:
    french_words_df=pandas.read_csv('french_words.csv')
    french_words_list=french_words_df.to_dict(orient='records', index=False)
else:
    french_words_list=words_to_learn_df.to_dict(orient='records', index=False)

def generate_word():
    global random_word_meaning_pair
    random_word_meaning_pair=random.choice(french_words_list)
    random_word=random_word_meaning_pair['French']
    random_word_meaning=random_word_meaning_pair['English']
    flash_card_canva.itemconfig(flash_card_language_text, text=f"{random_word}", fill="black")
    flash_card_canva.itemconfig(flash_card_language, text=f"French", fill="black")
    flash_card_canva.itemconfig(canva_img, image=card_front_img)
    window.after(3000, generate_meaning, random_word_meaning)




# ------------------------GENERATE MEANINGS----------------------------------------
def generate_meaning(meaning):

    flash_card_canva.itemconfig(canva_img, image=card_back_img)
    flash_card_canva.itemconfig(flash_card_language_text, text=f"{meaning}", fill="white")
    flash_card_canva.itemconfig(flash_card_language, text=f"English", fill="white")

def is_word_known():
    french_words_list.remove(random_word_meaning_pair)
    words_to_learn_df=pandas.DataFrame(french_words_list)
    words_to_learn_df.to_csv("words_to_learn.csv")
    generate_word()
    
    


# ------------------------UI SETUP----------------------------------------
window=Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

card_front_img=PhotoImage(file='card_front.png')
card_back_img=PhotoImage(file="card_back.png")
flash_card_canva=Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canva_img=flash_card_canva.create_image(400, 264, image=card_front_img)


flash_card_language= flash_card_canva.create_text(400, 164, text="", fill="black", font=('Arial', 24, "italic"))
flash_card_language_text= flash_card_canva.create_text(400, 264, text="", fill="black", font=('Arial', 32, "bold"))

flash_card_canva.grid(row=0, column=0, columnspan=2)

cross_button_img=PhotoImage(file='wrong.png')
cross_button=Button(image=cross_button_img, highlightthickness=0, command=generate_word)
cross_button.grid(row=1, column=0)

check_button_img=PhotoImage(file='right.png')
cross_button=Button(image=check_button_img, highlightthickness=0, command=is_word_known)
cross_button.grid(row=1, column=1)
generate_word()


window.mainloop()




