from random import randint

print("How many episodes of Rick and Morty exist in your present dimension?")
episodes = int(input())

episode_list = list()

while len(episode_list) < episodes:
    number = randint(1, episodes)
    if number not in episode_list:
        episode_list.append(number)

print()
for i in episode_list :
    if i <= 11 :
        seasonNumber = 1
        episodeNumber = i
    else :
        episodeNumber = ((i - 1) % 10)
        seasonNumber = 1 + (i - 1) // 10

    print("Episode", i, "of Rick and Morty AKA Episode", episodeNumber, "Season", seasonNumber)
    input("Input anything to continue.\n")

print("You're done, Wubba Lubba Dub Dub...")
