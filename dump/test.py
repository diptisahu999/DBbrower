user_detail_data = {
  "user_data": 11,
  "first_name": "rahul",
  "last_name": "pandav",
  "phone_no": "8975643232",
  "dob": "2023-05-18",
  "wallet_balance": "12321",
  "has_vehicle": "YES",
  "locker_data": 3,
  "address": None,
  "id_proof": None,
  "visiting_card": None,
  "is_deleted": None
}
user_detail_data = {k: v for k, v in user_detail_data.items() if v is not None}
print(user_detail_data)