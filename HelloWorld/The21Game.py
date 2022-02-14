import random


while True:
    current_number = 0
    if random.randint(0,1) == 0:
        current_player = "human"
        print("Bạn đánh trước:")
    else:
        current_player = "computer"
        print("Máy đánh trước:")
    
    while(current_number <= 21):
        if current_player == "human":
            print("Số hiện tại là: " + str(current_number))
            print()
            player_choice = ""
            while player_choice not in [1,2,3]:
                player_choice = int(input("Hãy thêm giá trị trong khoảng [1,2,3]: "))

            current_number = current_number + player_choice
            if current_number >= 21: 
                print("số hiện tại là: " + str(current_number) +". Bạn đã thua rồi.")
                break
            else:
                current_player = "computer"
                print("Tới lượt máy: ")
        else:
            computer_choice = random.randint(1,3)
            print("Giá trị mà máy chọn là: " + str(computer_choice))
            current_number = current_number + computer_choice
            if current_number >= 21:
                print("Số hiện tại là: " + str(current_number))
                print("Bạn đã chiến thắng")
                break
            else:
                current_player = "human"
                print("Tới lượt bạn: ")
        
    play_again = input("Bạn có muốn chơi lại không. Nhấn Y nếu đồng ý, nhấn phím bất kỳ để thoát:")
    if play_again.lower().startswith("y"):
        continue
    else:
        print("Thanks! Goodbye!")
        break
