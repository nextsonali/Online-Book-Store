from books.models import Book

books = [
    {
        "title": "The Silent Patient",
        "author": "Alex Michaelides",
        "description": "A gripping psychological thriller about a woman’s act of violence against her husband—and the therapist obsessed with uncovering her motive.",
        "genre": "Thriller",
        "price": 12.99,
        "stock": 15
    },
    {
        "title": "Atomic Habits",
        "author": "James Clear",
        "description": "An easy & proven way to build good habits and break bad ones.",
        "genre": "Self-Help",
        "price": 10.99,
        "stock": 20
    },
    {
        "title": "The Alchemist",
        "author": "Paulo Coelho",
        "description": "A philosophical book about following your dreams.",
        "genre": "Fiction",
        "price": 8.50,
        "stock": 18
    },
    {
        "title": "Educated",
        "author": "Tara Westover",
        "description": "A memoir about growing up in a survivalist family and pursuing education.",
        "genre": "Biography",
        "price": 14.00,
        "stock": 10
    },
    {
        "title": "1984",
        "author": "George Orwell",
        "description": "A dystopian novel set in a totalitarian regime.",
        "genre": "Classic",
        "price": 9.75,
        "stock": 25
    },
    {
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "description": "A novel about racial injustice in the Deep South.",
        "genre": "Classic",
        "price": 11.25,
        "stock": 22
    },
    {
        "title": "The Subtle Art of Not Giving a F*ck",
        "author": "Mark Manson",
        "description": "A counterintuitive approach to living a good life.",
        "genre": "Self-Help",
        "price": 13.50,
        "stock": 12
    },
    {
        "title": "The Midnight Library",
        "author": "Matt Haig",
        "description": "A story about the choices that go into a life well lived.",
        "genre": "Fantasy",
        "price": 12.25,
        "stock": 14
    },
    {
        "title": "Sapiens: A Brief History of Humankind",
        "author": "Yuval Noah Harari",
        "description": "An exploration of humanity’s creation and evolution.",
        "genre": "History",
        "price": 16.00,
        "stock": 10
    },
    {
        "title": "Dune",
        "author": "Frank Herbert",
        "description": "Epic science fiction saga set on a desert planet.",
        "genre": "Science Fiction",
        "price": 15.99,
        "stock": 8
    }
]

for book in books:
    Book.objects.create(**book)

print("10 books added successfully.")
