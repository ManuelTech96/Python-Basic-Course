import db
import Models.clients as clients

clients = db.session.query(clients.Client).all()

print(clients)