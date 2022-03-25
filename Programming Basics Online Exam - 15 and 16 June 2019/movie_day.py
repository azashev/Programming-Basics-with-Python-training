time_shooting = int(input())
number_scenes = int(input())
scene_length = int(input())

preparation = (time_shooting * 15) / 100

scenes_total_length = number_scenes * scene_length

total = scenes_total_length + preparation
diff = abs(total - time_shooting)

if total <= time_shooting:
    print(f"You managed to finish the movie on time! You have {round(diff)} minutes left!")
else:
    print(f"Time is up! To complete the movie you need {round(diff)} minutes.")