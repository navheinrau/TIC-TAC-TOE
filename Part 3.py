# TO CHECK FOR O's Win
	elif b1["text"] == "O" and b2["text"] == "O" and b3["text"]  == "O":
		b1.config(bg="Red")
		b2.config(bg="Red")
		b3.config(bg="Red")
		winner = True
		messagebox.showinfo("Tic Tac Toe", f"CONGRATULATIONS!