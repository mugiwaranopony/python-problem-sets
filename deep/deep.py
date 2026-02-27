#შოკი, როცა დავალება შენს ერთ-ერთ ყველაზე საყვარელ ფილმს ეხება 😱 

answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
answer = answer.strip().lower()

# if answer == "42":
#     print("Correct. You may now proceed to the Restaurant at the End of the Universe.")
# if answer == "forty-two":
#     print("Yes")
# if answer == "forty two":
#     print(Yes)
#თავიდან ერთად დავწერე, მაგრამ მირჩევნია if-ები გავაერთიანო.

if answer == "42" or answer == "forty-two" or answer == "forty two":
    print("Correct. You may now proceed to the Restaurant at the End of the Universe.")
else:
    print("I've calculated your answer's probability of being right. It's approximately zero.")
    print("Go buy a towel and try again. You're making the supercomputer depressed.")