# having issues seeding file thru the terminal, ask mentor

"""Create sample data for db"""

from models import User, Post, Tag, PostTag, db
from app import app

# create all tables
db.drop_all()
db.create_all()

# create sample users
juan = User(first_name="Juan", last_name="Rojas", image_url="http://placeimg.com/640/360/any")
carolina = User(first_name="Carolina", last_name="Alvarado", image_url="http://placeimg.com/640/360/any")
martina = User(first_name="Martina", last_name="Rojas-Alvarado", image_url="http://placeimg.com/640/360/any")
lili = User(first_name="Lili", last_name="Wood", image_url="http://placeimg.com/640/360/any")
jose = User(first_name="Joseluis", last_name="Salamando", image_url="http://placeimg.com/640/360/any")
lucas = User(first_name="Lucas", last_name="Wood", image_url="http://placeimg.com/640/360/any")
colin = User(first_name="Colin", last_name="Wood", image_url="http://placeimg.com/640/360/any")

# create sample posts
post1 = Post(title="Lorem Ipsum Dolor", content="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.", user_id=1)
post2 = Post(title="Las Margaritas De Los Cantares", content="Nulla facilisi morbi tempus iaculis urna id volutpat. Neque aliquam vestibulum morbi blandit cursus risus at. Diam sollicitudin tempor id eu nisl nunc. Eu lobortis elementum nibh tellus molestie. Massa vitae tortor condimentum lacinia quis. Pellentesque elit eget gravida cum sociis natoque penatibus et magnis. Nunc sed id semper risus in. Cursus sit amet dictum sit. Mauris in aliquam sem fringilla ut morbi tincidunt augue interdum. Turpis egestas pretium aenean pharetra magna. Sit amet nisl purus in mollis. Rutrum quisque non tellus orci ac auctor augue mauris augue. Congue nisi vitae suscipit tellus mauris. Ut morbi tincidunt augue interdum velit. Vel orci porta non pulvinar neque laoreet suspendisse interdum consectetur. Amet facilisis magna etiam tempor orci eu lobortis elementum nibh. Nisl tincidunt eget nullam non nisi. Ornare lectus sit amet est placerat. Leo duis ut diam quam nulla. Quis risus sed vulputate odio ut enim.", user_id=3)
post3 = Post(title="Rivolina La Machina De Los Calacantes", content="Posuere sollicitudin aliquam ultrices sagittis orci a. Justo nec ultrices dui sapien eget mi proin sed. Id diam maecenas ultricies mi eget mauris pharetra. Eget sit amet tellus cras. Tempor orci eu lobortis elementum nibh tellus molestie nunc. Vestibulum mattis ullamcorper velit sed ullamcorper morbi tincidunt ornare. Quis commodo odio aenean sed adipiscing diam donec adipiscing. Ac feugiat sed lectus vestibulum mattis ullamcorper velit. Nisl nisi scelerisque eu ultrices vitae auctor eu augue. Egestas dui id ornare arcu. Odio morbi quis commodo odio aenean sed. Proin fermentum leo vel orci porta. Nunc sed augue lacus viverra. Lectus mauris ultrices eros in cursus turpis massa tincidunt dui.", user_id=2)
post4 = Post(title="Arrieros Buenos Arrieros Malos", content="Lacus suspendisse faucibus interdum posuere lorem ipsum dolor sit amet. Nulla facilisi nullam vehicula ipsum a. Pellentesque adipiscing commodo elit at imperdiet dui. Odio morbi quis commodo odio aenean. Egestas pretium aenean pharetra magna ac placerat vestibulum. Blandit massa enim nec dui nunc mattis enim. Amet facilisis magna etiam tempor orci eu lobortis elementum. Blandit libero volutpat sed cras ornare arcu. Luctus venenatis lectus magna fringilla. Tempor nec feugiat nisl pretium fusce. Egestas maecenas pharetra convallis posuere morbi leo urna molestie at. Diam ut venenatis tellus in metus vulputate eu. Imperdiet sed euismod nisi porta lorem mollis aliquam ut. Eu turpis egestas pretium aenean.", user_id=7)
post5 = Post(title="Kalisto El Polocuredi Yo Cantares", content="Porttitor rhoncus dolor purus non enim praesent. Proin sed libero enim sed. Porttitor lacus luctus accumsan tortor posuere ac ut consequat semper. Dictum fusce ut placerat orci nulla pellentesque dignissim enim sit. Aliquet enim tortor at auctor urna nunc id cursus metus. Sollicitudin nibh sit amet commodo. Vel orci porta non pulvinar neque laoreet suspendisse. Arcu dui vivamus arcu felis bibendum ut tristique et egestas. Placerat vestibulum lectus mauris ultrices eros in cursus. Egestas diam in arcu cursus. Aliquet eget sit amet tellus cras. In iaculis nunc sed augue. Vitae justo eget magna fermentum iaculis. Amet massa vitae tortor condimentum lacinia quis. Eget egestas purus viverra accumsan in nisl nisi. Aenean sed adipiscing diam donec.", user_id=4)
post6 = Post(title="Palutio Marcante Yito Yundante", content="Quam adipiscing vitae proin sagittis nisl rhoncus mattis. Mauris vitae ultricies leo integer. Vitae congue eu consequat ac felis donec. Lacinia quis vel eros donec ac odio tempor orci. Adipiscing vitae proin sagittis nisl rhoncus mattis rhoncus urna. Quis risus sed vulputate odio ut enim blandit volutpat. Etiam tempor orci eu lobortis. Elementum tempus egestas sed sed risus. Fermentum leo vel orci porta non. Tellus orci ac auctor augue.", user_id=6)
post7 = Post(title="Camelisto Parrenteris Los Manjares", content="Non tellus orci ac auctor augue. Felis eget velit aliquet sagittis id consectetur purus ut faucibus. Sed euismod nisi porta lorem mollis. Faucibus turpis in eu mi. Ipsum dolor sit amet consectetur adipiscing elit. Est pellentesque elit ullamcorper dignissim. In hac habitasse platea dictumst quisque sagittis purus sit. Dui nunc mattis enim ut tellus elementum sagittis vitae et. Ac odio tempor orci dapibus ultrices in iaculis nunc sed. At elementum eu facilisis sed odio morbi quis. Aenean euismod elementum nisi quis eleifend quam adipiscing vitae proin. Posuere lorem ipsum dolor sit. At erat pellentesque adipiscing commodo elit at. Est lorem ipsum dolor sit amet consectetur adipiscing elit.", user_id=5)

# save tags
tag1 = Tag(name="news")
tag2 = Tag(name="nature")
tag3 = Tag(name="technology")
tag4 = Tag(name="international")
tag5 = Tag(name="design")
tag6 = Tag(name="home")

# save post tags
post_tag1 = PostTag(tag_id=1, post_id=2)
post_tag2 = PostTag(tag_id=2, post_id=1)
post_tag3 = PostTag(tag_id=3, post_id=2)
post_tag4 = PostTag(tag_id=4, post_id=6)
post_tag5 = PostTag(tag_id=6, post_id=5)
post_tag6 = PostTag(tag_id=4, post_id=2)

# save users first
db.session.add_all([juan, carolina, martina, lili, jose, lucas, colin])
db.session.commit()

# save posts second
db.session.add_all([post1, post2, post3, post4, post5, post6, post7])
db.session.commit()

# save tags
db.session.add_all([tag1, tag2, tag3, tag4, tag5, tag6])
db.session.commit()

# save post tags
db.session.add_all([post_tag1, post_tag2, post_tag3, post_tag4, post_tag5, post_tag6])
db.session.commit()
