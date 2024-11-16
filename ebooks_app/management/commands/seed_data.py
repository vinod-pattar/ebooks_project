from django.core.management.base import BaseCommand
from ebooks_app.models import CustomUser, Category, Book, Review, Cart, CartItem, Order, OrderItem
from django.utils import timezone
from faker import Faker
import random
from django.contrib.auth.models import Group

class Command(BaseCommand):
    help = 'Seed database with initial data'

    def handle(self, *args, **kwargs):
        fake = Faker()

        authors_group, created = Group.objects.get_or_create(name="Authors")
        customers_group, created = Group.objects.get_or_create(name="Customers")

        # Create Users
        user_types = ['author', 'customer']
        users = []
        for _ in range(25):  # Creating 25 users
            user_type = random.choice(user_types)
            user = CustomUser.objects.create_user(
                username=fake.user_name(),
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                email=fake.email(),
                bio=fake.text(max_nb_chars=200),
                date_of_birth=fake.date_of_birth(minimum_age=18, maximum_age=65),
                location=fake.city(),
                website=fake.url(),
                user_type=user_type,
                phone=fake.phone_number(),
                profile_picture=fake.image_url(),
            )
            user.set_password("password")  # Set a generic password
            user.save()

            if user_type == 'author':
                authors_group.user_set.add(user)
            else:
                customers_group.user_set.add(user)
            users.append(user)

        # Create Categories
        categories = []
        for _ in range(10):  # Creating 10 categories
            category = Category.objects.create(
                name=fake.word().capitalize(),
                description=fake.text(max_nb_chars=200)
            )
            categories.append(category)

        # Create Books
        authors = CustomUser.objects.filter(user_type='author')
        books = []
        for _ in range(50):  # Creating 50 books
            author = random.choice(authors)
            category = random.choice(categories)
            book = Book.objects.create(
                title=fake.sentence(nb_words=3),
                author=author,
                description=fake.text(max_nb_chars=500),
                published_date=fake.date_this_decade(),
                price=round(random.uniform(10.99, 99.99), 2),
                status=random.choice(['draft', 'published']),
                category=category,
                cover_image=fake.image_url()
            )
            books.append(book)

        # Create Reviews
        customers = CustomUser.objects.filter(user_type='customer')
        for _ in range(50):  # Creating 50 reviews
            book = random.choice(books)
            user = random.choice(users)
            Review.objects.create(
                book=book,
                user=user,
                rating=random.randint(1, 5),
                comment=fake.text(max_nb_chars=300)
            )

        # Create Carts and CartItems
        for user in customers:
            cart = Cart.objects.create(user=user)
            for _ in range(random.randint(1, 5)):  # Random 1-5 items per cart
                book = random.choice(books)
                quantity = random.randint(1, 3)
                CartItem.objects.create(cart=cart, book=book, quantity=quantity)

        # Create Orders and OrderItems
        for user in customers:
            if random.choice([True, False]):  # Randomly assign some users an order
                order = Order.objects.create(
                    user=user,
                    status=random.choice(['pending', 'shipped', 'delivered', 'cancelled']),
                    receipt_id=fake.uuid4(),
                    payment_method=random.choice(['COD', 'Pay online']),
                    amount_due=round(random.uniform(20.99, 200.99), 2),
                    amount_paid=round(random.uniform(20.99, 200.99), 2),
                    total_price=round(random.uniform(50.99, 500.99), 2),
                    shipping_address=fake.address()
                )
                for _ in range(random.randint(1, 3)):  # Random 1-3 items per order
                    book = random.choice(books)
                    quantity = random.randint(1, 3)
                    OrderItem.objects.create(order=order, book=book, quantity=quantity)

        self.stdout.write(self.style.SUCCESS("Database seeded successfully!"))
