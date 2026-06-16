borrows = {
    "Ali": {"books": ["1984", "Dune"]},
    "Ayşe": {"books": ["Sefiller"]}
}
def borrow_book(borrows, user, book):
    if user not in borrows:          
        borrows[user] = {"books": []}
    
    if book not in borrows[user]["books"]:   
        borrows[user]["books"].append(book)

borrow_book(borrows, "Ali", "Şeker Portakalı") 
borrow_book(borrows, "Mehmet", "Dune")  
print(borrows)



