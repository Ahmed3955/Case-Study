books=[
    {"Title":"book0","author":'author0','genre':'fiction','year':2000},
    {"Title":"book1","author":'author1','genre':'fiction','year':2001},
    {"Title":"book2","author":'author2','genre':'non-fiction','year':2002},
    {"Title":"book3","author":'author3','genre':'non-fiction','year':2003},
    {"Title":"book4","author":'author4','genre':'fiction','year':2004},
    {"Title":"book5","author":'author5','genre':'fiction','year':2005},
    {"Title":"book6","author":'author6','genre':'n0n-fiction','year':2006},
    {"Title":"book7","author":'author7','genre':'non-fiction','year':2007},
    {"Title":"book8","author":'author8','genre':'fiction','year':2008},
    {"Title":"book9","author":'author9','genre':'fiction','year':2009},
    {"Title":"book10","author":'author10','genre':'non-fiction','year':2010},    
]

class BookIterator:
    def __init__(self,books):
        self.books=books
        self.index=0

    def __iter__(self):
        return self
    def __next__(self):
        if self.index < len(self.books):
            book=self.books[self.index]
            self.index +=1
            return book
        else:
            raise StopIteration
        
book_iter=iter(BookIterator(books))
for _ in range(5):
    print(next(book_iter))



from itertools import islice

page2=islice(BookIterator(books), 5,10)
print("page2:")
for book in page2:
    print(book)


from itertools import chain
fiction=[b for b in books if book["genre"]=='fiction']
non_fiction=[b for b in books if book["genre"]=='non-fiction']

merged=(fiction,non_fiction)
for book in merged:
    print(book)

